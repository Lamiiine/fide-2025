# FIDE Chess Data Visualization Report

**Author:** Mohammed Lamine Abdellaoui  
**Course:** Information Visualization  
**Date:** January 2026

---

## 1. Introduction

This report presents the analysis of two interactive D3.js visualizations exploring **real FIDE chess data** from February 2015 to November 2025. 

**Dataset Statistics:**
- **465,876** unique players
- **5.17 million** monthly rating records
- **30** federations analyzed (top by player count)
- **129 months** of registration data

The visualizations address two research questions:

1. **The Magnus Effect**: Did Magnus Carlsen's dominance inspire chess growth in Norway?
2. **The COVID-19 Effect**: How did the pandemic affect FIDE chess registrations?

---

## 2. The Magnus Effect

*Did Magnus Carlsen's dominance change chess participation in Norway?*

Magnus Carlsen has been the world's highest-rated player throughout the dataset period (2015–2025), achieving a peak rating of 2882 [2]. The question is whether his success translated to increased FIDE participation in Norway.

### Data Analysis Results

**Top 10 Federations by Player Count (2025):**

| Rank | Federation | Players | Avg Rating |
|------|------------|---------|------------|
| 1 | India | 44,912 | 1,498 |
| 2 | Russia | 33,803 | 1,741 |
| 3 | France | 32,086 | 1,696 |
| 4 | Spain | 32,014 | 1,631 |
| 5 | Germany | 28,251 | 1,698 |
| 6 | Iran | 14,928 | 1,596 |
| 7 | Italy | 13,790 | 1,641 |
| 8 | Poland | 13,463 | 1,720 |
| 9 | Turkey | 10,788 | 1,566 |
| 10 | USA | 9,856 | 1,703 |

**Norway's Position:** 4,660 players (not in top 10 by absolute numbers, but notable for population size)

### Key Findings

**1. Norway's Growth (The Magnus Effect)**

| Metric | 2015 | 2025 | Change |
|--------|------|------|--------|
| Players | 1,258 | 4,660 | **+270%** |
| Avg Rating | 1,873 | 1,658 | **−215 pts** |

The **rating decline** is actually evidence of the Magnus Effect working as expected: mass adoption brings in many beginners, which lowers the national average. This is a healthy sign of growth.


**3. How the Visualization Answers the Question**

The animated bubble chart reveals:
- Norway moves **rightward** (more players) but **downward** (lower avg rating) over time
- This trajectory is consistent with mass adoption, new beginners enter the pool
- The "Follow Norway" trail feature shows this journey clearly
- Bubble size (titled player %) shows Norway maintains a strong elite despite growth

---

## 3. The COVID-19 Effect

*How did the pandemic affect FIDE chess registrations?*


### Data Analysis Results

**Monthly Registration Averages:**

| Period | Duration | Avg Registrations/Month | vs Pre-COVID |
|--------|----------|------------------------|--------------|
| Pre-COVID | Mar 2015 – Feb 2020 | 4,325 | baseline |
| COVID Era | Mar 2020 – Dec 2021 | 932 | **−78%** |
| Post-COVID | Jan 2022 – Nov 2025 | 3,317 | −23% |

### Key Findings

**1. Chess Collapsed During COVID**

- FIDE registrations **dropped 78%** during COVID
- This is because FIDE deals with **over-the-board** tournaments, which were cancelled worldwide
- The "Queen's Gambit boom" occurred on **online platforms** (Chess.com, Lichess), not in FIDE registrations [3][4]

**2. The Queen's Gambit Did NOT Spike FIDE Registrations**

| Month | Event | Registrations |
|-------|-------|---------------|
| Oct 2020 | Queen's Gambit Release | ~800 |
| Nov 2020 | Post-release | ~900 |
| Pre-COVID avg | — | ~4,300 |

The show released when tournaments were cancelled. New players joined **online platforms**, not FIDE [4].

**3. Recovery Has Been Partial**

Post-COVID registrations ( approx 3,317/month) remain **23% below** pre-COVID levels (~4,325/month), suggesting:
- Some players who left during COVID haven't returned
- Or: a generational shift toward online-first chess

**4. Gender Demographics (Actual Data)**

| Period | Female % |
|--------|----------|
| Pre-COVID | 10.6% |
| COVID | 10.8% |
| Post-COVID | 11.2% |

Female participation has remained stable at approximately **10-11%**, consistent with historical FIDE demographics [1]. The Queen's Gambit's impact on female participation occurred primarily on online platforms [3].

---

## 4. Conclusions

### The Magnus Effect — Confirmed with Nuance

| Finding | Evidence |
|---------|----------|
| Norway shows exceptional growth | **+270%** player growth (2015–2025) |
| Mass adoption lowers averages | Rating dropped from 1873 → 1658 (expected) |
| Per-capita impact significant | Norway's 5.5M population → 4,660 players is impressive |

### The COVID-19 Effect

| Finding | Evidence |
|---------|----------|
| chess collapsed during COVID | **−78%** registration drop |
| Queen's Gambit effect was online | FIDE registrations remained suppressed |
| Partial recovery post-2022 | Still **−23%** below pre-COVID |
| Demographics stable | Female participation steady at ~11% |

---

## 5. Limitations

This analysis has several important limitations that should be considered:

### Data Limitations

1. **Registration Timing**: We use first appearance in the ratings database as a proxy for registration. Players may have been registered earlier but not played rated games.

2. **Dataset Start (Feb 2015)**: The dataset begins with all existing players appearing in February 2015. We exclude this month from "new registration" analysis to avoid counting pre-existing players.

3. **Titled Player Tracking**: Title data tracks when titles were held, not when they were earned.

### Scope Limitations

1. FIDE data represents over-the-board tournament players. This excludes:
   - Online-only players (Chess.com, Lichess)
   - Casual players who never enter tournaments
   - Scholastic players in some federations

2. FIDE's minimum rating floor (historically 1000, raised to 1400) affects which players appear in the database [1].

3. Different federations have varying levels of tournament activity and FIDE reporting standards.

4.  While we observe correlations (e.g., Norway growth + Magnus success), we cannot prove direct causation. Other factors (economic, cultural, infrastructure) may contribute.

---

## 6. Technical Implementation

### Data Processing Pipeline

1. **Raw Data**: FIDE player list and rating history
2. **Processing **:  python to extract statistics
3. **Output**: `data/processed_data.json` consumed by visualization
4. **Visualization**: `visualizations.html` renders interactive D3.js charts

### Running the Visualization

```bash
# 1. Process the data (creates processed_data.json)
python3 process_real_data.py

# 2. Serve the files (required for JSON loading)
python3 -m http.server 8000

# 3. Open in browser
# Navigate to http://localhost:8000/visualizations.html
```

### File Structure

```
2025-fide/
├── data/
│   ├── players.tsv          # Raw player data
│   ├── ratings.tsv          # Rating history
│   ├── countries.tsv        # Federation mappings
│   ├── iso3.tsv             # Region mappings
│   ├── titles.tsv           # Title history
│   └── processed_data.json  # Generated statistics
├── process_real_data.py     # Data processing script
├── visualizations.html      # Interactive visualization
├── REPORT.md               # This report
└── README.md               # Quick start guide
```

---

## 7. References

[1] FIDE. "FIDE Rating Regulations." https://www.fide.com/

[2] ChessBase. "Magnus Carlsen and Norway Chess." https://chessbase.com/

[3] Chess.com. "The Queen's Gambit Effect." https://www.chess.com/article/view/the-queens-gambit-effect

[4] NPR. "The Queen's Gambit Is Causing A Surge In Online Chess Play." October 2020. https://www.npr.org/2020/11/29/939952836/the-queens-gambit-is-causing-a-surge-in-online-chess-play

---


