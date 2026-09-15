# Diagram Brief

## User Goal

- Output: an editable draw.io overview titled **Language-Centric AI Research of Xiaojun Wu**.
- Audience: research collaborators, homepage visitors, and academic presentation audiences.
- Must communicate: the horizontal research lifecycle `Data -> Models -> Agent Harness -> Evaluation`, the vertical domain split `General / Finance / Math Modeling`, and the feedback loop from evaluation back to data and model development.
- Must not do: imply paper authorship for task-only contributions, invent public links for working projects, or display GitHub stars at or below 50.

## Source Inventory

| id | source | type | role | priority | notes |
|---|---|---|---|---|---|
| S1 | User prompt, 2026-08-23 | content + structure | project inventory, axes, requested Agent style | must | User-supplied status overrides weaker inferences. |
| S2 | https://wxj630.github.io/ and local homepage repository | content | public profile, paper links, research focus | must | Confirms language/LLM, harness, data synthesis, benchmark focus. |
| S3 | Google Scholar profile nWK11zgAAAAJ | content | identity and research labels | should | Confirms Xiaojun Wu and NLP / LLM Agent / Mathematical Modeling labels. |
| S4 | arXiv API | content | paper IDs, titles, years, author membership | must | Exact IDs recorded in `source-notes.md`. |
| S5 | GitHub API/CLI | content | repository URLs and current star counts | must | Snapshot date: 2026-08-23. |
| S6 | drawio Agent Structure reference | style | external actor, Agent/Harness grouping, icon-cells, color-coded flows | must | Visual grammar only; the user-directed clean revision overrides hand-jiggled strokes and Comic Sans. |
| S7 | iconfont.cn multi-color icon search | asset + style | data/model/agent/evaluation/transfer/actor SVGs | must | Public query URLs and icon IDs are recorded in `asset-ledger.md`; raw and normalized SVGs are kept locally. |

## Requirement Traceability

| id | requirement | source evidence | level | planned visual encoding |
|---|---|---|---|---|
| R1 | Exact title | user prompt | must | Large title at top. |
| R2 | Lifecycle on horizontal axis | user prompt | must | Four aligned stage headers with directional arrows. |
| R3 | Domains on vertical axis | user prompt | must | Three colored swimlanes with left-side labels. |
| R4 | Clean Agent visual style | user prompt + Agent Structure reference + 2026-08-25 refinement | must | Precise Arial typography and clean strokes; external researcher actor, one dashed Harness region, icon-cells, and feedback trace retain the Agent grammar. |
| R5 | Accepted work shows conference; otherwise arXiv | user follow-up | must | Green conference line or blue arXiv ID line inside each project card. |
| R6 | Show GitHub only when stars >50 | user follow-up | must | Dark GitHub star line only for qualifying repositories. |
| R7 | Distinguish task contribution from paper authorship | verified sources + user clarification | must | `Task contributor` line and dagger legend. |
| R8 | Editable source and visual QA | selected skill | must | Primary `.drawio`, screenshot cycles, validators, and defect log. |
| R9 | DataArc is an ACL 2026 System Demonstration; Select2Reason is ACL 2026 Findings | user correction, 2026-08-23 | must | Correct green conference lines in General → Data. |
| R10 | Touchstone-Dataset and Touchstone-GPT are outputs of the same Golden-Touchstone paper | user clarification, 2026-08-23 | must | Prefix both cards with `Golden-Touchstone:` and link both to arXiv:2411.06272. |
| R11 | Replace glyph/emoji placeholders with multi-color iconfont SVGs and update the skill preference | user correction, 2026-08-23 | must | Flat 2-4 color SVGs embedded in bounded cells; workstation actor remains standalone. |
| R12 | Make the organization logic explicit with two prominent axes and larger icons | user correction, 2026-08-23 | must | A thick eastward `X · RESEARCH LIFECYCLE` arrow above the four stages; a thick southward `Y · RESEARCH DOMAINS` arrow beside the three domain lanes; enlarged actor, header, card, and adapter SVGs. |
| R13 | Make the figure orderly and remove overlapping frames | user correction, 2026-08-25 | must | Disable sketch jitter; remove the three lane frames and redundant whole-canvas Agent frame; use whitespace, two short row separators, one Harness boundary, and a dedicated feedback route. |
| R14 | Rename the Math Modeling evaluation benchmark | user correction, 2026-08-25 | must | Replace `Mathematical-Modeling-BAO-Bench` with `Terminal-Bench-Mathematical-Modeling`. |

## Semantic Model

| id | entity or relationship | direction / hierarchy | visual encoding | uncertainty |
|---|---|---|---|---|
| M1 | Data fuels Models | left to right | header arrow labelled `train` | none |
| M2 | Models are adapted by Agent Harnesses | left to right | header arrow labelled `reason & act` | none |
| M3 | Harnessed systems are evaluated | left to right | header arrow labelled `measure` | none |
| M4 | Evaluation failures, rewards, and traces drive the next cycle | Evaluation back to Data | large green feedback edge below the matrix | none |
| M5 | Bayesian-Agent and Think-on-Graph 3.0 transfer across domains | shared vertical layer | dashed harness sub-boundary plus domain adapter cells | diagrammatic abstraction |
| M6 | Terminal-Bench-Science and ALE participation | task contribution, not paper authorship | dagger-tagged evaluation cards | ALE participation is user-reported; not present in the public author list. |
| M7 | Golden-Touchstone spans dataset, model, and evaluation | one paper represented in three lifecycle columns | shared `Golden-Touchstone` naming and identical paper link | none |

## Style Extraction: Agent Structure Security Sketch

### Palette

| role | sampled hex | use in this figure |
|---|---|---|
| background | `#FCFCFC` | white paper canvas |
| border stroke | `#314548` | mapped to existing dark teal `#173B46` for Agent boundaries |
| normal arrow/body text | `#0D0D0C` / `#212A2C` | mapped to charcoal `#263238` |
| benign input blue | `#ADDEE6` / `#4E9DB0` | X-axis fill and user-input arrow |
| trusted green | `#75966D` | mapped to accepted/reuse green `#2F855A` |
| warning red | `#B34243` | not used: this portfolio figure has no attack semantics |
| accent amber | `#DCB744` | conference/evaluation accents |
| muted gray | `#91989B` / `#CFD0D0` | secondary labels and pale structure |

### Typography

- Heading: Arial, 20–30 pt, bold.
- Section/stage labels: Arial, 18–22 pt, bold.
- Component labels: Arial, 13–14 pt.
- Small annotations: Arial, 12–13 pt.
- Deliberate deviation from the reference: the user requested a more orderly result, so the clean font supersedes Comic Sans.

### Shape and Arrow Language

- Clean rounded cells with approximately 12–18 px visual radius and no sketch jitter.
- Component strokes: 1.15–1.45 px; the single dashed Harness boundary uses a `7 5` rhythm.
- Normal execution arrows are dark, orthogonal, and block-headed; benign input is blue; trusted reuse is green.
- The organization scaffold uses two explicit 3.4 px dark-teal arrows with large block heads. Domain identity remains on three colored Y-axis ticks.
- No shadow; white or transparent component fills.

### Layout Rhythm and Icon Language

- Reference composition: dense 2×2 interaction scenes with large standalone actors, central dashed Agent regions, and compact icon-label cells.
- Adopted composition traits: large unboxed researcher actor, prominent semantic arrows, one dashed cross-domain Harness region, large multi-color icons inside bounded cells, and tight 20–50 px inter-module gaps.
- Deliberate deviation: retain the lifecycle-by-domain matrix and use clean top-conference geometry; do not copy the security reference's attack panels, Comic Sans, or hand-jiggled line treatment.
- Icon targets: actor 210 px; lifecycle headers 56 px; project cards 52 px; Agent Harness cards 60 px to compensate for SVG whitespace; cross-domain adapters 46 px.

### Semantic Justification

| element | visual form | represented content | justified? |
|---|---|---|---|
| X axis | thick eastward clean arrow | chronological research lifecycle from Data to Evaluation | yes |
| Y axis | thick southward clean arrow | domain progression General, Finance, Math Modeling | yes |
| Y-axis ticks | three colored labelled crossbars | one tick for each domain lane | yes |
| stage icons | large multi-color SVG in header/card cells | Data, Model, Agent Harness, and Evaluation roles | yes |
| workstation actor | large standalone multi-color SVG | Xiaojun Wu as the research-program source | yes |
| transfer icon | green/amber loop SVG | harness reuse and domain adaptation | yes |
| attack/memory/tool icons from the reference | omitted | no matching semantic entity in this portfolio overview | omitted by anti-decoration rule |

## Style Contract

| id | font | palette | stroke | icon style | density | source |
|---|---|---|---|---|---|---|
| ST1 | Arial, 13-14 pt cards, 20-22 pt stages, 30 pt title | dark teal `#173B46`, general blue, finance amber, math violet, green accepted, blue arXiv | clean 1.15-1.45 px components, 3.4 px axes, one dashed Harness boundary | enlarged iconfont flat multi-color SVGs embedded inside bounded cells; standalone 210 px workstation actor | orderly but information-dense with explicit X/Y scaffold | Agent Structure object hierarchy + top-conference spacing discipline |

## Open Assumptions

| assumption | risk | handling |
|---|---|---|
| LightningMathModel remains `Working` | Local revision notes mention a Findings recommendation, but the user explicitly labelled it working. | Use `Working`; do not expose a conference or paper link. |
| Think-on-Graph 3.0 remains arXiv/under review for this figure | Local homepage says under review; private notes mention a Findings recommendation. | Use public arXiv status. |
| ALE contribution is task-level participation | Public arXiv author list does not include Xiaojun Wu. | Use `Task contributor`, never `co-author`. |
