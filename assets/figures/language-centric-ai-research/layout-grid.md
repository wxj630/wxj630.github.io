# Layout Grid

- Canvas: 2280 x 1520 px, white background.
- External actor: x=20..230, y=210..420; label y=420..498.
- Explicit X axis: 3.4 px dark-teal eastward arrow x=330..2150 at y=174, labelled `X · RESEARCH LIFECYCLE`.
- Explicit Y axis: 3.4 px dark-teal southward arrow x=265 at y=340..1320, labelled `Y · RESEARCH DOMAINS`; colored ticks at the vertical centers of General, Finance, and Math Modeling.
- Research Agent label: x=330..760, y=202..230. The redundant whole-canvas dashed frame is intentionally removed.
- Lifecycle headers: y=235..325, with 56 px icons.
  - Data: x=330..680; data cards use x=430..690 to reserve the lane-label margin.
  - Models: x=730..1240.
  - Agent Harness: x=1290..1690.
  - Evaluation: x=1740..2150.
- Domain rows use whitespace rather than lane frames:
  - General cards: y=370..855.
  - Finance cards: y=950..1070; short neutral separators at y=902.
  - Math Modeling cards: y=1165..1285; short neutral separators at y=1117.
- General → Data cards: DataArc y=370, Envs-FORGE y=535, Select2Reason y=690; Data cards begin at x=450, leaving a dedicated feedback gutter at x=425.
- Project-card icons are 52 px, Agent Harness card icons 60 px, and adapter icons 46 px.
- Feedback route: from Evaluation to x=2245, down to y=1395, left to x=425, then up through the dedicated gutter and into the Data header from below.
- The only dashed structural frame is the labelled cross-domain Harness sub-container at x=1325..1685.
