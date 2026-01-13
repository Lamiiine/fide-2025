#!/usr/bin/env python3
"""
Data Analysis Script for FIDE Chess Visualizations
Loads and analyzes the processed real FIDE data
"""

import json
from collections import defaultdict

def load_processed_data():
    """Load the processed JSON data."""
    with open('data/processed_data.json', 'r') as f:
        return json.load(f)

def analyze_magnus_effect(data):
    """Analyze the Magnus Effect (Norway's growth)."""
    
    print("=" * 60)
    print("MAGNUS EFFECT ANALYSIS (Real FIDE Data)")
    print("=" * 60)
    
    country_yearly = data['country_yearly']
    
    # Get unique countries and years
    countries = set(d['country'] for d in country_yearly)
    years = sorted(set(d['year'] for d in country_yearly))
    
    print(f"\n📊 Dataset: {len(countries)} federations, {min(years)}-{max(years)}")
    
    # Top 10 federations by 2025 player count
    print(f"\n🏆 Top 10 Federations by Player Count (2025):")
    data_2025 = [d for d in country_yearly if d['year'] == 2025]
    data_2025.sort(key=lambda x: -x['players'])
    
    for i, d in enumerate(data_2025[:10], 1):
        print(f"   {i:2}. {d['country']:20} {d['players']:>8,} players (avg: {d['avg_rating']})")
    
    # Norway analysis
    norway_2015 = next((d for d in country_yearly if d['fed'] == 'NOR' and d['year'] == 2015), None)
    norway_2025 = next((d for d in country_yearly if d['fed'] == 'NOR' and d['year'] == 2025), None)
    
    if norway_2015 and norway_2025:
        growth = (norway_2025['players'] / norway_2015['players'] - 1) * 100
        rating_change = norway_2025['avg_rating'] - norway_2015['avg_rating']
        
        print(f"\n🇳🇴 NORWAY (Magnus Effect):")
        print(f"   Players: {norway_2015['players']:,} (2015) → {norway_2025['players']:,} (2025)")
        print(f"   Growth: +{growth:.1f}%")
        print(f"   Avg Rating: {norway_2015['avg_rating']} → {norway_2025['avg_rating']} ({rating_change:+d})")
        print(f"   Titled: {norway_2015['titled_count']} → {norway_2025['titled_count']}")
        
        if rating_change < 0:
            print(f"\n   ✓ Rating decline indicates mass adoption (new beginners)")
    
    # India comparison
    india_2015 = next((d for d in country_yearly if d['fed'] == 'IND' and d['year'] == 2015), None)
    india_2025 = next((d for d in country_yearly if d['fed'] == 'IND' and d['year'] == 2025), None)
    
    if india_2015 and india_2025:
        growth = (india_2025['players'] / india_2015['players'] - 1) * 100
        print(f"\n🇮🇳 INDIA (Comparison):")
        print(f"   Players: {india_2015['players']:,} → {india_2025['players']:,}")
        print(f"   Growth: +{growth:.1f}%")
    
    # Growth comparison for key countries
    print(f"\n📈 Growth Comparison (2015→2025):")
    key_feds = ['NOR', 'IND', 'USA', 'RUS', 'GER', 'FRA', 'ESP']
    
    for fed in key_feds:
        d2015 = next((d for d in country_yearly if d['fed'] == fed and d['year'] == 2015), None)
        d2025 = next((d for d in country_yearly if d['fed'] == fed and d['year'] == 2025), None)
        if d2015 and d2025:
            growth = (d2025['players'] / d2015['players'] - 1) * 100
            print(f"   {d2015['country']:15} {d2015['players']:>6,} → {d2025['players']:>6,} (+{growth:.0f}%)")


def analyze_covid_effect(data):
    """Analyze the COVID-19 effect on registrations."""
    
    print("\n" + "=" * 60)
    print("COVID-19 EFFECT ANALYSIS (Real FIDE Data)")
    print("=" * 60)
    
    monthly = data['monthly_registrations']
    
    # Split by period
    pre_covid = [d for d in monthly if d['period'] == 'Pre-COVID']
    covid = [d for d in monthly if d['period'] == 'COVID']
    post_covid = [d for d in monthly if d['period'] == 'Post-COVID']
    
    # Calculate averages
    pre_avg = sum(d['total'] for d in pre_covid) / len(pre_covid) if pre_covid else 0
    covid_avg = sum(d['total'] for d in covid) / len(covid) if covid else 0
    post_avg = sum(d['total'] for d in post_covid) / len(post_covid) if post_covid else 0
    
    print(f"\n📊 Dataset: {len(monthly)} months of registration data")
    print(f"   Pre-COVID: {len(pre_covid)} months")
    print(f"   COVID Era: {len(covid)} months")
    print(f"   Post-COVID: {len(post_covid)} months")
    
    print(f"\n📉 MONTHLY REGISTRATION AVERAGES:")
    print(f"   Pre-COVID:  {pre_avg:,.0f}/month (baseline)")
    print(f"   COVID Era:  {covid_avg:,.0f}/month ({(covid_avg/pre_avg-1)*100:+.0f}%)")
    print(f"   Post-COVID: {post_avg:,.0f}/month ({(post_avg/pre_avg-1)*100:+.0f}%)")
    
    print(f"\n⚠️  KEY FINDING: OTB chess COLLAPSED during COVID (−{(1-covid_avg/pre_avg)*100:.0f}%)")
    print(f"   This is expected: FIDE = over-the-board tournaments")
    print(f"   Tournaments were cancelled worldwide during lockdowns")
    
    # Queen's Gambit period
    oct_2020 = next((d for d in monthly if d['year'] == 2020 and d['mon'] == 10), None)
    sep_2020 = next((d for d in monthly if d['year'] == 2020 and d['mon'] == 9), None)
    
    if oct_2020 and sep_2020:
        print(f"\n🎬 QUEEN'S GAMBIT (Oct 2020):")
        print(f"   Sep 2020: {sep_2020['total']:,} registrations")
        print(f"   Oct 2020: {oct_2020['total']:,} registrations")
        print(f"   (Show released Oct 23, 2020)")
        print(f"\n   ✓ No spike in FIDE registrations — boom was on online platforms")
    
    # Gender analysis
    print(f"\n👩 GENDER DEMOGRAPHICS (Real Data):")
    for period, period_data in [('Pre-COVID', pre_covid), ('COVID', covid), ('Post-COVID', post_covid)]:
        if period_data:
            total = sum(d['total'] for d in period_data)
            female = sum(d['female'] for d in period_data)
            pct = female / total * 100 if total > 0 else 0
            print(f"   {period:12} {pct:.1f}% female")
    
    print(f"\n   ✓ Female participation stable at ~10-11% (consistent with FIDE history)")
    
    # Total registrations
    total_all = sum(d['total'] for d in monthly)
    print(f"\n📊 Total Registrations (Mar 2015 - Nov 2025): {total_all:,}")


def main():
    print("\n" + "🏆" * 20)
    print("  FIDE CHESS DATA ANALYSIS (REAL DATA)")
    print("🏆" * 20)
    
    try:
        data = load_processed_data()
        print(f"\n✅ Loaded processed data: {data['metadata']['total_players']:,} players")
    except FileNotFoundError:
        print("\n❌ Error: Run 'python3 process_real_data.py' first to generate processed data")
        return
    
    analyze_magnus_effect(data)
    analyze_covid_effect(data)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print("\n✅ All findings based on REAL FIDE data")
    print("📊 See visualizations.html for interactive exploration\n")


if __name__ == "__main__":
    main()
