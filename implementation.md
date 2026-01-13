Below is your content converted into clean, copy-ready Markdown, preserving structure, headings, tables, and lists.

Information Visualization: Visualisation Design

Mohammed Lamine Abdellaoui

1. Selected Questions
1.1 Q1: Global Insights — “The Magnus Effect”

Did Magnus Carlsen’s dominance change the ambitions of a generation?

Magnus Carlsen (born 1990, Norway) has been the world’s highest-rated player throughout the dataset period (2015–2025), achieving a peak rating of 2882 in August 2019.

This question explores whether his sustained dominance inspired:

More players to take up competitive chess

A specific “Magnus generation” of young players (born 2000–2010)

Higher ambition levels (peak ratings achieved)

A particular effect in Norway

1.2 Q2: Comparing Subsets — “The COVID-19 Effect”

How did the pandemic change chess?

The COVID-19 pandemic (March 2020+) combined with Netflix’s The Queen’s Gambit (October 2020) created unprecedented interest in chess.

This question compares:

Player registration rates: Pre-COVID vs. COVID-era vs. Post-COVID

Demographic shifts: gender and age distributions

Activity levels: games played per month

Geographic patterns in growth

2. Visualization 1: The Magnus Effect

Inspired by Hans Rosling’s Gapminder visualization, this design uses an animated bubble chart where each bubble represents a country’s chess ecosystem, and time is explored through animation.

2.1 Visual Mapping Table

Table 1: Visual Mapping for Magnus Effect

Name	D	F	X	Y	Z	T	R	CP
Number of Players	Q	>	P					
Average Rating	Q	>		P				
Titled Players (%)	Q	>					S	
Region / Continent	N	>					C	
Country	N	>						
Time (year)	Q	sl>				P		sl>
Norway (focus)	N	br>						br>

Legend

D (Data Type): Q = Quantitative, O = Ordered, N = Nominal

F (Function): > = direct mapping, sl> = slider, br> = buttons

X, Y, Z, T: Spatial / temporal axes, P = Position

R (Retinal): C = Color, S = Size, Sh = Shape, V = Value

CP (Control Panel): Interactive widget type

Encoding Details

X Position: Scaled range (1 to 50k players)

Y Position: Linear scale (1500–2200 average rating)

T Position: Animated timeline slider (2015–2025)

Size (S): Bubble area ∝ percentage of titled players

Color (C):

Europe = Blue

Asia = Green

Americas = Orange

Africa = Brown

Oceania = Purple

Slider (sl>): Time slider with Play/Pause button

Buttons (br>): “Follow Norway” toggle, region filter checkboxes

Marks: Circles (bubbles) representing countries
Axes:

X = Number of registered players

Y = Average peak rating

T = Time (animation)

2.2 Design Rationale

Bubble chart over line chart
Shows all countries simultaneously and avoids clutter from 150+ overlapping lines.

Position for quantitative axes
Position is the most accurate channel for quantitative data (Mackinlay, 1986).

Bubble size for titled player percentage
Encodes elite density using area (not radius) to avoid perceptual distortion (Stevens’ Law).

Color hue for geographic regions
Uses Bertin’s Hue for nominal grouping and regional pattern detection.

Animation for time
Uses Gestalt Common Fate to reveal temporal relationships.

Trails for temporal context
Optional trails show historical paths without cluttering the current state.

Norway highlight
Distinctive stroke ensures Norway remains visible during animation.

X-axis scaling
Prevents large countries from dominating the visual space.

2.3 Interaction Design

Table 2: Interaction Specification for Magnus Effect

Interaction Type	User Action	System Response	Purpose
Animation Controls	Play/Pause	Animate years (2015→2025)	Observe evolution
Scrub timeline	Drag slider	Jump to year	Explore specific moment
Speed control	Select 1x / 2x / 4x	Change animation speed	Overview vs. detail
Selection & Focus	Click bubble	Highlight country, show trail	Focus on one country
Search	Type country name	Bubble pulses and labels	Find specific country
Norway shortcut	Click “Norway”	Follow Norway	Track Magnus effect
Comparison	Shift+click bubbles	Multiple highlights	Compare trajectories
Region filter	Click legend	Filter regions	Reduce complexity
Details-on-demand	Hover bubble	Tooltip with stats	Quick lookup
Event marker	Click “2019: Peak”	Info panel	Historical context
2.4 Sketch

Figure 1: Magnus Effect animated bubble chart mockup

3. Visualization 2: The COVID-19 Effect Dashboard

A multi-view dashboard with three coordinated views and a shared control panel.

3.1 Visual Mapping Table
View 1: Timeline (Line Chart)
Name	D	F	X	Y	R	CP
Time (month)	Q	>	P			
New Players	Q	>		P		
Period	O	>			C	
Uncertainty	Q	>			V	
Events	N	>	P		Sh	
View 2: Before / After Comparison
Name	D	F	X	Y	R
Metric Category	N	>	P		
Value	Q	>		P	
Period	N	>			C
View 3: Age Distribution Shift
Name	D	F	X	Y	R
Age Group	O	>	P		
Percentage	Q	>		P	
Period	N	>			C
Control Panel (Shared)

Buttons (br>): Gender, Age Groups, Period selection

Slider (sl>): Time range (2018–2025)

Encoding Details

Color: Blue = Pre-COVID, Orange = COVID, Green = Post-COVID

Value: Semi-transparent uncertainty band (α = 0.3)

Shape: Event markers (lockdowns, Queen’s Gambit)

3.2 Design Rationale

Multi-view dashboard supports multi-dimensional comparison

Three-period background coloring reinforces temporal structure

Line chart with confidence band shows trends and variance

Grouped bars enable direct comparison

Explicit change annotations reduce cognitive load

Ordered age groups preserve meaningful progression

Callout annotations guide attention to key insights

Right-side control panel keeps controls visible and separate

3.3 Interaction Design

Table 3: Interaction Specification for COVID Effect Dashboard

Phase	Control	User Action	System Response
Overview	Initial load	View dashboard	All views displayed
Filter	Gender checkboxes	Toggle	Filter all views
Filter	Age group checkboxes	Toggle	Filter data
Filter	Period buttons	Select	Highlight period
Time	Range slider	Drag	Zoom timeline
Details	Hover timeline	Move cursor	Tooltip appears
Linking	Hover any view	Hover	Highlight others
Display	Options toggles	Toggle	Show/hide features
3.4 Sketch

Figure 2: COVID-19 Effect dashboard mockup

Outline Summary

Selected Questions

Q1: The Magnus Effect

Q2: The COVID-19 Effect

Visualization 1: The Magnus Effect

Visual Mapping Table

Design Rationale

Interaction Design

Sketch

Visualization 2: The COVID-19 Effect Dashboard

Visual Mapping Table

Design Rationale

Interaction Design

Sketch