#!/usr/bin/env python3
"""
Process real FIDE data to generate JSON for visualizations.
Outputs: data/processed_data.json
"""

import json
import csv
from collections import defaultdict
from datetime import datetime
import sys

def load_country_mappings():
    """Load federation code to country name and region mappings."""
    # IOC code to country name
    ioc_to_country = {}
    with open('data/countries.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            ioc_to_country[row['ioc']] = row['#country']
    
    # IOC code to region (via alpha3)
    ioc_to_alpha3 = {}
    with open('data/countries.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            ioc_to_alpha3[row['ioc']] = row['alpha3']
    
    alpha3_to_region = {}
    with open('data/iso3.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            alpha3_to_region[row['#alpha3']] = row['region']
    
    # Build final mapping: IOC -> (country_name, region)
    fed_info = {}
    for ioc, country in ioc_to_country.items():
        alpha3 = ioc_to_alpha3.get(ioc, ioc)
        region = alpha3_to_region.get(alpha3, 'Unknown')
        fed_info[ioc] = {'country': country, 'region': region}
    
    # Add common variations
    fed_info['ENG'] = {'country': 'England', 'region': 'Europe'}
    fed_info['SCO'] = {'country': 'Scotland', 'region': 'Europe'}
    fed_info['WLS'] = {'country': 'Wales', 'region': 'Europe'}
    
    return fed_info

def load_players():
    """Load player data with federation, sex, birth year."""
    print("Loading players...", file=sys.stderr)
    players = {}
    with open('data/players.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            players[row['#id']] = {
                'fed': row['fed'],
                'sex': row['sex'],
                'birthyear': int(row['birthyear']) if row['birthyear'] and row['birthyear'].isdigit() else None,
                'max_rating': int(row['max_rating']) if row['max_rating'] else None
            }
    print(f"  Loaded {len(players):,} players", file=sys.stderr)
    return players

def load_titles():
    """Load title data to count titled players per federation."""
    print("Loading titles...", file=sys.stderr)
    # Get unique player IDs with titles
    titled_players = set()
    with open('data/titles.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            titled_players.add(row['#id'])
    print(f"  Loaded {len(titled_players):,} titled players", file=sys.stderr)
    return titled_players

def process_ratings_for_timeline():
    """
    Process ratings to find:
    1. First appearance of each player (registration proxy)
    2. Player counts and avg ratings by federation by year
    """
    print("Processing ratings (this may take a minute)...", file=sys.stderr)
    
    # Track first appearance of each player
    first_appearance = {}
    # Track yearly stats: fed -> year -> {players: set, ratings: list}
    yearly_stats = defaultdict(lambda: defaultdict(lambda: {'players': set(), 'ratings': []}))
    
    line_count = 0
    with open('data/ratings.tsv', 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            line_count += 1
            if line_count % 1000000 == 0:
                print(f"  Processed {line_count:,} rating records...", file=sys.stderr)
            
            player_id = row['#id']
            month = row['month']
            rating = int(row['rating']) if row['rating'] else 0
            
            # Track first appearance
            if player_id not in first_appearance:
                first_appearance[player_id] = month
    
    print(f"  Total: {line_count:,} rating records", file=sys.stderr)
    return first_appearance

def calculate_registrations_by_month(first_appearance, players):
    """Calculate new registrations by month with demographics."""
    print("Calculating monthly registrations...", file=sys.stderr)
    
    monthly = defaultdict(lambda: {
        'total': 0, 'male': 0, 'female': 0,
        'youth': 0, 'adult': 0, 'senior': 0
    })
    
    for player_id, month in first_appearance.items():
        if player_id not in players:
            continue
        
        player = players[player_id]
        monthly[month]['total'] += 1
        
        # Gender
        if player['sex'] == 'M':
            monthly[month]['male'] += 1
        elif player['sex'] == 'F':
            monthly[month]['female'] += 1
        
        # Age at registration (approximate)
        if player['birthyear']:
            reg_year = int(month.split('-')[0])
            age = reg_year - player['birthyear']
            if age < 18:
                monthly[month]['youth'] += 1
            elif age < 40:
                monthly[month]['adult'] += 1
            else:
                monthly[month]['senior'] += 1
    
    return monthly

def calculate_country_yearly_stats(players, first_appearance, fed_info, titled_players):
    """Calculate player counts and ratings by country by year."""
    print("Calculating country yearly stats...", file=sys.stderr)
    
    # Accumulate players by fed and registration year
    # year -> fed -> {count, ratings, titled}
    yearly = defaultdict(lambda: defaultdict(lambda: {'count': 0, 'ratings': [], 'titled': 0}))
    
    for player_id, player in players.items():
        fed = player['fed']
        if player_id not in first_appearance:
            continue
        
        first_month = first_appearance[player_id]
        first_year = int(first_month.split('-')[0])
        
        # Add to all subsequent years (cumulative count)
        for year in range(first_year, 2026):
            yearly[year][fed]['count'] += 1
            if player['max_rating']:
                yearly[year][fed]['ratings'].append(player['max_rating'])
            if player_id in titled_players:
                yearly[year][fed]['titled'] += 1
    
    return yearly

def main():
    fed_info = load_country_mappings()
    players = load_players()
    titled_players = load_titles()
    first_appearance = process_ratings_for_timeline()
    
    # Monthly registrations for COVID analysis
    monthly_regs = calculate_registrations_by_month(first_appearance, players)
    
    # Country yearly stats for Magnus analysis
    yearly_stats = calculate_country_yearly_stats(players, first_appearance, fed_info, titled_players)
    
    # Build output
    output = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'total_players': len(players),
            'date_range': '2015-02 to 2025-11'
        },
        'monthly_registrations': [],
        'country_yearly': []
    }
    
    # Monthly registrations (skip Feb 2015 - it's the dataset start, not real registrations)
    for month in sorted(monthly_regs.keys()):
        if month == '2015-02':
            continue  # Skip initial dump
        data = monthly_regs[month]
        year, mon = month.split('-')
        
        # Determine period
        if int(year) < 2020 or (int(year) == 2020 and int(mon) < 3):
            period = 'Pre-COVID'
        elif int(year) < 2022:
            period = 'COVID'
        else:
            period = 'Post-COVID'
        
        output['monthly_registrations'].append({
            'month': month,
            'year': int(year),
            'mon': int(mon),
            'period': period,
            'total': data['total'],
            'male': data['male'],
            'female': data['female'],
            'youth': data['youth'],
            'adult': data['adult'],
            'senior': data['senior']
        })
    
    # Country yearly stats - focus on top countries
    # Get top 30 federations by total players
    fed_totals = defaultdict(int)
    for player in players.values():
        fed_totals[player['fed']] += 1
    
    top_feds = sorted(fed_totals.items(), key=lambda x: -x[1])[:30]
    top_fed_codes = {f[0] for f in top_feds}
    
    for year in range(2015, 2026):
        for fed in top_fed_codes:
            if fed not in yearly_stats[year]:
                continue
            
            stats = yearly_stats[year][fed]
            if stats['count'] == 0:
                continue
            
            info = fed_info.get(fed, {'country': fed, 'region': 'Unknown'})
            ratings = stats['ratings']
            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            titled_pct = (stats['titled'] / stats['count'] * 100) if stats['count'] > 0 else 0
            
            output['country_yearly'].append({
                'year': year,
                'fed': fed,
                'country': info['country'],
                'region': info['region'],
                'players': stats['count'],
                'avg_rating': round(avg_rating),
                'titled_count': stats['titled'],
                'titled_pct': round(titled_pct, 2)
            })
    
    # Write output
    with open('data/processed_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print("\n=== SUMMARY ===", file=sys.stderr)
    print(f"Output written to: data/processed_data.json", file=sys.stderr)
    print(f"Monthly records: {len(output['monthly_registrations'])}", file=sys.stderr)
    print(f"Country-year records: {len(output['country_yearly'])}", file=sys.stderr)
    
    # Print some key stats
    print("\n=== KEY STATISTICS ===", file=sys.stderr)
    
    # Norway growth
    norway_2015 = next((x for x in output['country_yearly'] if x['fed'] == 'NOR' and x['year'] == 2015), None)
    norway_2025 = next((x for x in output['country_yearly'] if x['fed'] == 'NOR' and x['year'] == 2025), None)
    if norway_2015 and norway_2025:
        growth = (norway_2025['players'] / norway_2015['players'] - 1) * 100
        print(f"Norway: {norway_2015['players']:,} (2015) → {norway_2025['players']:,} (2025) = {growth:.1f}% growth", file=sys.stderr)
        print(f"Norway avg rating: {norway_2015['avg_rating']} (2015) → {norway_2025['avg_rating']} (2025)", file=sys.stderr)
    
    # India growth
    india_2015 = next((x for x in output['country_yearly'] if x['fed'] == 'IND' and x['year'] == 2015), None)
    india_2025 = next((x for x in output['country_yearly'] if x['fed'] == 'IND' and x['year'] == 2025), None)
    if india_2015 and india_2025:
        growth = (india_2025['players'] / india_2015['players'] - 1) * 100
        print(f"India: {india_2015['players']:,} (2015) → {india_2025['players']:,} (2025) = {growth:.1f}% growth", file=sys.stderr)
    
    # COVID stats
    pre_covid = [x for x in output['monthly_registrations'] if x['period'] == 'Pre-COVID']
    covid = [x for x in output['monthly_registrations'] if x['period'] == 'COVID']
    post_covid = [x for x in output['monthly_registrations'] if x['period'] == 'Post-COVID']
    
    if pre_covid:
        pre_avg = sum(x['total'] for x in pre_covid) / len(pre_covid)
        print(f"\nPre-COVID avg monthly: {pre_avg:.0f}", file=sys.stderr)
    if covid:
        covid_avg = sum(x['total'] for x in covid) / len(covid)
        print(f"COVID avg monthly: {covid_avg:.0f}", file=sys.stderr)
    if post_covid:
        post_avg = sum(x['total'] for x in post_covid) / len(post_covid)
        print(f"Post-COVID avg monthly: {post_avg:.0f}", file=sys.stderr)
    
    # Female participation
    total_female = sum(p['sex'] == 'F' for p in players.values())
    total_players = len(players)
    print(f"\nFemale participation: {total_female:,} / {total_players:,} = {total_female/total_players*100:.1f}%", file=sys.stderr)

if __name__ == '__main__':
    main()

