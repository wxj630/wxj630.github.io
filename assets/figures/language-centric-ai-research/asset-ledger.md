# Asset / Provenance Ledger

## Iconfont multi-color SVGs

All visible semantic icons are local SVGs sourced from [iconfont.cn](https://www.iconfont.cn/) on 2026-08-23. The original downloads are preserved under `assets/iconfont/raw/`; paper-palette versions under `assets/iconfont/normalized/` retain separate body, accent, status, and highlight fills. The iconfont search pages did not expose author/project metadata without login, so provenance records the public query URL and icon ID.

| asset id | iconfont source | role | local files | palette treatment |
|---|---|---|---|---|
| data_icon | [数据库, ID 7088596](https://www.iconfont.cn/search/index?searchType=icon&q=%E6%95%B0%E6%8D%AE%E5%BA%93&page=1&fills=1) | Data headers and cards | `raw/data-database-chart.svg`; `normalized/data-database-chart.svg` | dark teal frame; blue, coral, and amber bars |
| model_icon | [大模型, ID 47835891](https://www.iconfont.cn/search/index?searchType=icon&q=%E5%A4%A7%E6%A8%A1%E5%9E%8B&page=1&fills=1) | Model headers and cards | `raw/model-cube-spark.svg`; `normalized/model-cube-spark.svg` | slate cube with amber highlight |
| harness_icon | [智能体, ID 41703724](https://www.iconfont.cn/search/index?searchType=icon&q=%E6%99%BA%E8%83%BD%E4%BD%93&page=1&fills=1) | Agent Harness headers and cards | `raw/agent-harness.svg`; `normalized/agent-harness.svg` | layered blue/teal body with green state accents |
| evaluation_icon | [靶心, ID 10454597](https://www.iconfont.cn/search/index?searchType=icon&q=%E9%9D%B6%E5%BF%83&page=1&fills=1) | Evaluation headers and cards | `raw/evaluation-target.svg`; `normalized/evaluation-target.svg` | blue target, coral arrow, amber center |
| transfer_icon | [循环, ID 23949535](https://www.iconfont.cn/search/index?searchType=icon&q=%E5%BE%AA%E7%8E%AF&page=1&fills=1) | Cross-domain adapters | `raw/transfer-loop.svg`; `normalized/transfer-loop.svg` | green/orange loop with dark-teal anchor |
| xiaojun_actor | [程序员, ID 23763302](https://www.iconfont.cn/search/index?searchType=icon&q=%E7%A8%8B%E5%BA%8F%E5%91%98&page=1&fills=1) | Standalone researcher-at-laptop actor | `raw/researcher-programmer.svg`; `normalized/researcher-programmer.svg` | retained skin layers; mapped clothing/laptop neutrals to the paper palette |

The normalized selection contact sheet is `assets/iconfont/iconfont-selected-normalized.png`. SVGs are embedded as vector data URIs in the `.drawio`; no raster icon is embedded.

## Approximations

- Project-specific logos are not used. Shared multi-color lifecycle icons keep the figure coherent and avoid implying brand approval.
- GitHub is represented by text (`GitHub ★N`) rather than the GitHub logo.
