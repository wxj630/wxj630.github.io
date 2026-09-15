from __future__ import annotations

from pathlib import Path
from urllib.parse import quote
import xml.etree.ElementTree as ET


WORKDIR = Path(__file__).resolve().parent
ICONFONT_DIR = WORKDIR / "assets" / "iconfont" / "normalized"
OUT = WORKDIR / "language-centric-ai-research-xiaojun-wu.drawio"

CANVAS_W = 2280
CANVAS_H = 1520
CARD_Y_SHIFT = 55

COLORS = {
    "ink": "#173B46",
    "charcoal": "#263238",
    "muted": "#667085",
    "general": "#2B6F92",
    "general_fill": "#F1F8FC",
    "finance": "#B9770E",
    "finance_fill": "#FFF7E8",
    "math": "#7B4FB3",
    "math_fill": "#F8F1FF",
    "accepted": "#16835C",
    "arxiv": "#2563EB",
    "working": "#6B7280",
    "github": "#364152",
    "feedback": "#2F855A",
    "blue_input": "#1677A8",
}

def svg_uri(filename: str) -> str:
    svg = (ICONFONT_DIR / filename).read_text(encoding="utf-8")
    return "data:image/svg+xml," + quote(svg, safe="")


ICONS = {
    "data": svg_uri("data-database-chart.svg"),
    "model": svg_uri("model-cube-spark.svg"),
    "harness": svg_uri("agent-harness.svg"),
    "eval": svg_uri("evaluation-target.svg"),
    "transfer": svg_uri("transfer-loop.svg"),
    "actor": svg_uri("researcher-programmer.svg"),
}


mxfile = ET.Element(
    "mxfile",
    {
        "host": "app.diagrams.net",
        "agent": "Codex",
        "version": "26.0.9",
        "pages": "1",
    },
)
diagram = ET.SubElement(mxfile, "diagram", {"id": "language-centric-ai", "name": "Research Lifecycle"})
model = ET.SubElement(
    diagram,
    "mxGraphModel",
    {
        "dx": "1800",
        "dy": "1200",
        "grid": "1",
        "gridSize": "10",
        "guides": "1",
        "tooltips": "1",
        "connect": "1",
        "arrows": "1",
        "fold": "1",
        "page": "1",
        "pageScale": "1",
        "pageWidth": str(CANVAS_W),
        "pageHeight": str(CANVAS_H),
        "math": "0",
        "shadow": "0",
    },
)
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", {"id": "0"})
ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})


def vertex(
    cell_id: str,
    value: str,
    style: str,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    parent: str = "1",
    link: str | None = None,
    tooltip: str | None = None,
) -> ET.Element:
    attrs = {
        "id": cell_id,
        "value": value,
        "style": style,
        "vertex": "1",
        "parent": parent,
    }
    if link:
        attrs["link"] = link
    if tooltip:
        attrs["tooltip"] = tooltip
    cell = ET.SubElement(root, "mxCell", attrs)
    ET.SubElement(
        cell,
        "mxGeometry",
        {"x": str(x), "y": str(y), "width": str(width), "height": str(height), "as": "geometry"},
    )
    return cell


def edge(
    cell_id: str,
    source: str,
    target: str,
    value: str,
    style: str,
    *,
    points: list[tuple[float, float]] | None = None,
) -> ET.Element:
    cell = ET.SubElement(
        root,
        "mxCell",
        {
            "id": cell_id,
            "value": value,
            "style": style,
            "edge": "1",
            "parent": "1",
            "source": source,
            "target": target,
        },
    )
    geo = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    if points:
        arr = ET.SubElement(geo, "Array", {"as": "points"})
        for px, py in points:
            ET.SubElement(arr, "mxPoint", {"x": str(px), "y": str(py)})
    return cell


def free_edge(
    cell_id: str,
    value: str,
    style: str,
    source_point: tuple[float, float],
    target_point: tuple[float, float],
    *,
    points: list[tuple[float, float]] | None = None,
) -> ET.Element:
    """Create a semantic axis/annotation edge with explicit endpoints."""
    source_id = f"{cell_id}_source"
    target_id = f"{cell_id}_target"
    anchor_style = (
        "ellipse;html=1;opacity=0;fillOpacity=0;strokeOpacity=0;"
        "pointerEvents=0;resizable=0;movable=0;connectable=0;"
    )
    vertex(source_id, "", anchor_style, source_point[0] - 0.5, source_point[1] - 0.5, 1, 1)
    vertex(target_id, "", anchor_style, target_point[0] - 0.5, target_point[1] - 0.5, 1, 1)
    cell = ET.SubElement(
        root,
        "mxCell",
        {
            "id": cell_id,
            "value": value,
            "style": style,
            "edge": "1",
            "parent": "1",
            "source": source_id,
            "target": target_id,
        },
    )
    geo = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    ET.SubElement(geo, "mxPoint", {"x": str(source_point[0]), "y": str(source_point[1]), "as": "sourcePoint"})
    ET.SubElement(geo, "mxPoint", {"x": str(target_point[0]), "y": str(target_point[1]), "as": "targetPoint"})
    if points:
        arr = ET.SubElement(geo, "Array", {"as": "points"})
        for px, py in points:
            ET.SubElement(arr, "mxPoint", {"x": str(px), "y": str(py)})
    return cell


FONT = "fontFamily=Arial;"
# The Agent reference supplies the object hierarchy and interaction grammar.
# The user prefers a precise, publication-style rendering, so edges and boxes
# are intentionally clean rather than hand-jiggled.
SKETCH = "sketch=0;"

text_style = (
    "text;html=1;strokeColor=none;fillColor=none;whiteSpace=wrap;overflow=visible;"
    + FONT
    + "align=left;verticalAlign=middle;"
)

# Title and subtitle.
vertex(
    "title",
    "<b>Language-Centric AI Research of Xiaojun Wu</b>",
    text_style + "fontSize=30;fontColor=#173B46;align=center;",
    275,
    20,
    1870,
    48,
)
vertex(
    "subtitle",
    "Data → Models → Agent Harness → Evaluation — a cross-domain learning loop",
    text_style + "fontSize=16;fontColor=#667085;align=center;",
    400,
    68,
    1620,
    30,
)

# Legend.
legend_base = (
    "rounded=1;whiteSpace=wrap;html=1;"
    + SKETCH
    + FONT
    + "fontSize=12;strokeWidth=1;arcSize=18;align=center;verticalAlign=middle;fillColor=#FFFFFF;strokeColor=#54707A;"
)
vertex("legend_paper", "↗ clickable paper", legend_base + "fontColor=#2563EB;", 985, 105, 170, 32)
vertex("legend_accept", "conference", legend_base + "fontColor=#16835C;", 1165, 105, 125, 32)
vertex("legend_arxiv", "arXiv", legend_base + "fontColor=#2563EB;", 1300, 105, 90, 32)
vertex("legend_work", "Working", legend_base + "fontColor=#6B7280;", 1400, 105, 100, 32)
vertex("legend_star", "GitHub ★ only if >50", legend_base + "fontColor=#364152;", 1510, 105, 190, 32)
vertex("legend_contrib", "† task contributor", legend_base + "fontColor=#8A5A0A;", 1710, 105, 155, 32)

# Explicit organization axes. These are semantic scaffold arrows, not decorative connectors.
axis_x_style = (
    "html=1;rounded=0;curved=0;endArrow=block;endFill=1;endSize=18;"
    + SKETCH
    + FONT
    + "fontSize=18;fontStyle=1;fontColor=#173B46;strokeColor=#173B46;strokeWidth=3.4;"
    + "labelBackgroundColor=#FCFCFC;labelBorderColor=none;spacing=6;"
)
free_edge("axis_x", "<b>X · RESEARCH LIFECYCLE</b>", axis_x_style, (330, 174), (2150, 174))

axis_y_style = (
    "html=1;rounded=0;curved=0;endArrow=block;endFill=1;endSize=18;horizontal=0;rotation=-90;"
    + SKETCH
    + FONT
    + "fontSize=18;fontStyle=1;fontColor=#173B46;strokeColor=#173B46;strokeWidth=3.4;"
    + "labelBackgroundColor=#FCFCFC;labelBorderColor=none;spacing=6;"
)
free_edge("axis_y", "<b>Y · RESEARCH DOMAINS</b>", axis_y_style, (265, 340), (265, 1320))

# External researcher actor: a standalone multi-color iconfont SVG.
vertex(
    "actor_icon",
    "",
    "shape=image;html=1;imageAspect=1;aspect=fixed;strokeColor=none;fillColor=none;"
    f"image={ICONS['actor']};",
    20,
    210,
    210,
    210,
)
vertex(
    "actor_label",
    "<b>Xiaojun Wu</b><br/><font color=\"#667085\">HKUST(GZ) × IDEA</font><br/><font color=\"#2B6F92\">Language-centric AI researcher</font>",
    text_style + "fontSize=14;align=center;verticalAlign=top;",
    0,
    420,
    230,
    78,
)

# A compact Agent label replaces the redundant whole-canvas dashed frame.
# The green feedback loop already encloses the lifecycle semantically, while
# the Harness keeps the reference's dashed internal Agent-region grammar.
vertex(
    "research_agent_label",
    "<b>LANGUAGE-CENTRIC RESEARCH AGENT</b>",
    text_style + "fontSize=14;fontColor=#173B46;align=left;",
    330,
    202,
    430,
    28,
)

# Domain rows use whitespace and two short neutral separators instead of three
# nested lane frames. The Harness column is deliberately left uninterrupted to
# read as a shared cross-domain layer.
separator_style = "rounded=1;html=1;strokeColor=none;fillColor=#DDE4E8;pointerEvents=0;"
vertex("separator_fin_left", "", separator_style, 450, 902, 820, 2)
vertex("separator_fin_right", "", separator_style, 1710, 902, 465, 2)
vertex("separator_math_left", "", separator_style, 450, 1117, 820, 2)
vertex("separator_math_right", "", separator_style, 1710, 1117, 465, 2)

domain_tick_base = (
    "html=1;rounded=0;curved=0;startArrow=none;endArrow=none;"
    + SKETCH
    + FONT
    + "fontSize=18;fontStyle=1;strokeWidth=2;labelBackgroundColor=#FCFCFC;spacing=5;"
)
free_edge("tick_general", "<b>GENERAL</b>", domain_tick_base + "fontColor=#2B6F92;strokeColor=#2B6F92;", (268.5, 615), (415, 615))
free_edge("tick_finance", "<b>FINANCE</b>", domain_tick_base + "fontColor=#8A5A0A;strokeColor=#B9770E;", (268.5, 1010), (415, 1010))
free_edge("tick_math", "<b>MATH MODELING</b>", domain_tick_base + "fontColor=#633892;strokeColor=#7B4FB3;", (268.5, 1225), (415, 1225))

# Stage headers.
header_style = (
    "shape=label;rounded=1;whiteSpace=wrap;html=1;imageAspect=1;"
    + SKETCH
    + FONT
    + "fontSize=22;fontStyle=1;strokeColor=#54707A;strokeWidth=1.35;arcSize=16;"
    + "align=left;verticalAlign=middle;imageAlign=left;imageVerticalAlign=middle;"
    + "imageWidth=56;imageHeight=56;spacingLeft=76;spacingRight=10;spacingTop=8;spacingBottom=8;"
)
vertex("data_header", "<b>1 · DATA</b><br/><font color=\"#667085\" size=\"3\">corpora · datasets · envs</font>", header_style + f"fillColor=#F1F8FC;image={ICONS['data']};", 330, 235, 350, 90)
vertex("model_header", "<b>2 · MODELS</b><br/><font color=\"#667085\" size=\"3\">pretrain · optimize · infer</font>", header_style + f"fillColor=#F1F8FC;image={ICONS['model']};", 730, 235, 510, 90)
vertex("harness_header", "<b>3 · AGENT HARNESS</b><br/><font color=\"#667085\" size=\"3\">skills · tools · graph reasoning</font>", header_style + f"fillColor=#EDF8F3;image={ICONS['harness']};", 1290, 235, 400, 90)
vertex("eval_header", "<b>4 · EVALUATION</b><br/><font color=\"#667085\" size=\"3\">benchmarks · real workflows</font>", header_style + f"fillColor=#FFF7E8;image={ICONS['eval']};", 1740, 235, 410, 90)

normal_edge = (
    "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;"
    + SKETCH
    + FONT
    + "fontSize=13;fontColor=#263238;strokeColor=#263238;strokeWidth=1.45;labelBackgroundColor=#FFFFFF;"
)
edge("edge_data_model", "data_header", "model_header", "train", normal_edge)
edge("edge_model_harness", "model_header", "harness_header", "act", normal_edge)
edge("edge_harness_eval", "harness_header", "eval_header", "test", normal_edge)

input_edge = (
    "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;"
    + SKETCH
    + FONT
    + "fontSize=13;fontColor=#1677A8;strokeColor=#1677A8;strokeWidth=1.8;labelBackgroundColor=#FFFFFF;"
)
actor_input_edge = edge(
    "edge_actor_input",
    "actor_icon",
    "data_header",
    "research questions",
    input_edge + "exitX=1;exitY=0.333;exitPerimeter=1;entryX=0;entryY=0.5;entryPerimeter=1;",
)
ET.SubElement(actor_input_edge.find("mxGeometry"), "mxPoint", {"x": "0", "y": "22", "as": "offset"})


def project_card(
    cell_id: str,
    title_html: str,
    status: str,
    status_kind: str,
    stage: str,
    domain: str,
    x: int,
    y: int,
    w: int,
    h: int,
    *,
    paper: str | None = None,
    github: str | None = None,
    stars: int | None = None,
    contributor: bool = False,
    full_title: str | None = None,
) -> None:
    status_color = COLORS[status_kind]
    domain_stroke = COLORS[domain]
    lines = [f"<b>{title_html}</b>"]
    if status:
        prefix = "↗ " if paper else ""
        lines.append(f"<font color=\"{status_color}\"><b>{prefix}{status}</b></font>")
    if contributor:
        lines.append("<font color=\"#8A5A0A\"><b>† Task contributor</b></font>")
    if github and stars is not None and stars > 50:
        lines.append(f"<font color=\"#364152\">GitHub ★{stars:,}</font>")
    value = "<br/>".join(lines)
    icon_size = 60 if stage == "harness" else 52
    icon_spacing = icon_size + 20
    style = (
        "shape=label;rounded=1;whiteSpace=wrap;html=1;dashed=0;imageAspect=1;"
        + SKETCH
        + FONT
        + f"fontSize=14;strokeColor={domain_stroke};strokeWidth=1.2;fillColor=#FFFFFF;arcSize=14;"
        + "align=left;verticalAlign=middle;imageAlign=left;imageVerticalAlign=middle;"
        + f"imageWidth={icon_size};imageHeight={icon_size};spacingLeft={icon_spacing};spacingRight=10;spacingTop=8;spacingBottom=8;"
        + f"image={ICONS[stage]};"
    )
    link = paper or github
    tooltip_bits = []
    if full_title:
        tooltip_bits.append("Title: " + full_title)
    if paper:
        tooltip_bits.append("Paper: " + paper)
    if github:
        tooltip_bits.append("GitHub: " + github)
    vertex(cell_id, value, style, x, y + CARD_Y_SHIFT, w, h, link=link, tooltip=" | ".join(tooltip_bits) or None)


# General — Data.
project_card(
    "card_syndata", "DataArc-SynData-<br/>Toolkit", "ACL 2026<br/>System Demonstration", "accepted", "data", "general", 450, 315, 260, 140,
    paper="https://arxiv.org/abs/2605.08138", github="https://github.com/DataArcTech/DataArc-SynData-Toolkit", stars=1777,
)
project_card(
    "card_envs_forge", "Envs-FORGE", "arXiv:2608.14312", "arxiv", "data", "general", 450, 480, 260, 120,
    paper="https://arxiv.org/abs/2608.14312",
)
project_card(
    "card_select2reason", "Select2Reason", "ACL Findings ’26", "accepted", "data", "general", 450, 635, 260, 115,
    paper="https://arxiv.org/abs/2505.17266", github="https://github.com/DataArcTech/Select2Reason", stars=1,
    full_title="Select2Reason: Efficient Instruction-Tuning Data Selection for Long-CoT Reasoning",
)

# General — Models.
project_card(
    "card_fengshen", "Fengshenbang 1.0", "arXiv:2209.02970", "arxiv", "model", "general", 770, 315, 230, 130,
    paper="https://arxiv.org/abs/2209.02970", github="https://github.com/IDEA-CCNL/Fengshenbang-LM", stars=4126,
)
project_card(
    "card_lazytrain", "Lazy-Train", "arXiv:2608.11919", "arxiv", "model", "general", 1020, 315, 230, 130,
    paper="https://arxiv.org/abs/2608.11919", github="https://github.com/DataArcTech/LazyTrain", stars=1,
)
project_card("card_lazyinfer", "Lazy-Infer", "Working", "working", "model", "general", 770, 475, 230, 110)
project_card("card_faro", "FARO-Optimizer", "Working", "working", "model", "general", 1020, 475, 230, 110)
project_card("card_r3l", "R³L (Return2Risk RL)", "Working", "working", "model", "general", 895, 620, 230, 110)

# Cross-domain Agent Harness region.
harness_region_style = (
    "rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;"
    + SKETCH
    + FONT
    + "dashed=1;dashPattern=7 5;strokeColor=#54707A;strokeWidth=1.35;fillColor=none;arcSize=12;"
    + "fontSize=14;fontStyle=1;fontColor=#173B46;align=center;verticalAlign=top;spacingTop=4;"
)
vertex("harness_region", "Cross-domain harness layer", harness_region_style, 1325, 355, 360, 930)
project_card(
    "card_bayesian", "Bayesian-Agent", "arXiv:2606.08348", "arxiv", "harness", "general", 1350, 350, 310, 130,
    paper="https://arxiv.org/abs/2606.08348", github="https://github.com/DataArcTech/Bayesian-Agent", stars=79,
)
project_card(
    "card_tog", "Think-on-Graph 3.0", "arXiv:2509.21710", "arxiv", "harness", "general", 1350, 525, 310, 135,
    paper="https://arxiv.org/abs/2509.21710", github="https://github.com/DataArcTech/ToG-3", stars=89,
)
adapter_style = (
    "shape=label;rounded=1;whiteSpace=wrap;html=1;imageAspect=1;"
    + SKETCH
    + FONT
    + "fontSize=13;fontStyle=1;strokeColor=#2F855A;strokeWidth=1.15;fillColor=#EDF8F3;arcSize=24;"
    + "align=center;verticalAlign=middle;imageAlign=left;imageVerticalAlign=middle;"
    + "imageWidth=46;imageHeight=46;spacingLeft=62;spacingRight=10;spacingTop=8;spacingBottom=8;"
    + f"image={ICONS['transfer']};"
)
vertex(
    "adapter_general",
    '<b>shared planning · skills · graph retrieval</b>',
    adapter_style,
    1360,
    760,
    290,
    66,
)
vertex(
    "adapter_finance",
    '<b>finance adaptation</b>',
    adapter_style,
    1380,
    970,
    250,
    64,
)
vertex(
    "adapter_math",
    '<b>math-modeling adaptation</b>',
    adapter_style,
    1380,
    1180,
    250,
    64,
)
transfer_edge = (
    "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;dashed=1;dashPattern=4 3;"
    + SKETCH
    + FONT
    + "fontSize=13;fontColor=#2F855A;strokeColor=#2F855A;strokeWidth=1.35;labelBackgroundColor=#FFFFFF;"
)
edge("edge_tog_adapter", "card_tog", "adapter_general", "compose", transfer_edge)
edge("edge_adapter_fin", "adapter_general", "adapter_finance", "reuse", transfer_edge)
edge("edge_adapter_math", "adapter_finance", "adapter_math", "reuse", transfer_edge)

# General — Evaluation.
project_card(
    "card_skillsbench", "SkillsBench", "arXiv:2602.12670", "arxiv", "eval", "general", 1760, 315, 370, 130,
    paper="https://arxiv.org/abs/2602.12670", github="https://github.com/benchflow-ai/skillsbench", stars=1707,
)
project_card(
    "card_tbsci", "Terminal-Bench-Science", "GitHub benchmark", "github", "eval", "general", 1760, 485, 370, 135,
    github="https://github.com/harbor-framework/terminal-bench-science", stars=271, contributor=True,
)
project_card(
    "card_ale", "Agents’ Last Exam", "arXiv:2606.05405", "arxiv", "eval", "general", 1760, 660, 370, 140,
    paper="https://arxiv.org/abs/2606.05405", github="https://github.com/rdi-berkeley/agents-last-exam", stars=962, contributor=True,
)

# Finance lane.
project_card(
    "card_touchstone_data", "Golden-Touchstone:<br/>Touchstone-Dataset", "EMNLP Findings ’25", "accepted", "data", "finance", 450, 895, 260, 120,
    paper="https://arxiv.org/abs/2411.06272", github="https://github.com/DataArcTech/Golden-Touchstone", stars=8,
)
project_card(
    "card_touchstone_gpt", "Golden-Touchstone:<br/>Touchstone-GPT", "EMNLP Findings ’25", "accepted", "model", "finance", 810, 895, 400, 120,
    paper="https://arxiv.org/abs/2411.06272", github="https://github.com/DataArcTech/Golden-Touchstone", stars=8,
)
project_card(
    "card_golden_eval", "Golden-Touchstone", "EMNLP Findings ’25", "accepted", "eval", "finance", 1760, 895, 370, 120,
    paper="https://arxiv.org/abs/2411.06272", github="https://github.com/DataArcTech/Golden-Touchstone", stars=8,
)

# Math Modeling lane.
project_card(
    "card_bao_data", "Mathematical-Modeling-<br/>BAO-Dataset", "Working", "working", "data", "math", 450, 1110, 260, 120,
    github="https://github.com/wxj630/Math-Modeling-BAO", stars=13,
)
project_card("card_lightning", "LightningMathModel", "Working", "working", "model", "math", 810, 1115, 400, 110)
project_card(
    "card_tb_math", "Terminal-Bench-<br/>Mathematical-Modeling", "Working", "working", "eval", "math", 1760, 1110, 370, 120,
    github="https://github.com/wxj630/terminal-bench-math-modeling", stars=0,
)

# Evaluation feedback loop.
feedback_style = (
    "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;entryX=0.5;entryY=1;entryPerimeter=1;"
    + SKETCH
    + FONT
    + "fontSize=15;fontStyle=1;fontColor=#2F855A;strokeColor=#2F855A;strokeWidth=2;labelBackgroundColor=#FFFFFF;"
)
edge(
    "edge_feedback",
    "eval_header",
    "data_header",
    "evaluation gaps · rewards · task traces → next data &amp; model cycle",
    feedback_style,
    points=[(2245, 273), (2245, 1395), (425, 1395), (425, 330), (520, 330)],
)
vertex(
    "footnote",
    "† Task contribution is distinct from paper authorship. Star counts are a 2026-08-23 snapshot.",
    text_style + "fontSize=12;fontColor=#667085;align=center;",
    650,
    1457,
    1060,
    26,
)


ET.indent(mxfile, space="  ")
OUT.write_bytes(ET.tostring(mxfile, encoding="utf-8", xml_declaration=True))
print(OUT)
