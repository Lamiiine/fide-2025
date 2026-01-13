# Info Vis Implementation

**Author:** Mohammed Lamine Abdellaoui  
**Course:** Information Visualization

## Description

This project contains two interactive D3.js visualizations exploring FIDE chess data:

1. **The Magnus Effect** — An animated bubble chart analyzing whether Magnus Carlsen's dominance inspired a generation of chess players
2. **The COVID-19 Effect** — A multi-view dashboard examining how the pandemic changed chess participation patterns

## Dependencies

- **D3.js v7** — Loaded via CDN (no installation required)
- **Google Fonts (Inter)** — Loaded via CDN
- Modern web browser with JavaScript enabled

## How to Run

### Option 1: Direct File Open
Simply open `visualizations.html` in any modern web browser (Chrome, Firefox, Safari, Edge).

```bash
# On Linux
xdg-open visualizations.html

# On macOS
open visualizations.html

# On Windows
start visualizations.html
```

### Option 2: Local Server (Optional)
If you encounter any CORS issues, run a local server:

```bash
# Using Python 3
python -m http.server 8000

# Then open http://localhost:8000/visualizations.html
```

## File Structure

```
2025-fide/
├── visualizations.html  # Main visualization (single file)
├── REPORT.md           # Detailed implementation report
├── implementation.md   # Original design document
└── README.md          # This file
```

## Usage Instructions

### Visualization 1: The Magnus Effect

- **Play/Pause** — Animate through years 2015-2025
- **Speed** — Adjust animation speed (0.5x to 4x)
- **Year Slider** — Jump to specific year
- **Follow Norway** — Track Norway's trajectory with trail
- **Region Chips** — Filter by continent (click to toggle)
- **Hover** — View country details in tooltip

### Visualization 2: The COVID-19 Effect

- **Period Buttons** — Highlight Pre-COVID, COVID, or Post-COVID data
- **Gender Filter** — Filter timeline by gender
- **Age Group Filter** — Filter timeline by age group
- **Hover** — View detailed values in tooltips


