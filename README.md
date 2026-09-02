<div align="center">

# AgentForge Platform

### Compression + Multi-Agent Orchestration + Netflix Analysis -- all in one

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Netflix](https://img.shields.io/badge/Dataset-Netflix-E50914?style=flat-square&logo=netflix&logoColor=white)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Unified token compression engine + multi-agent orchestration + real Netflix data analysis.**

**7 open-source projects merged into one platform.**

</div>

---

## What Is This?

AgentForge combines the best open-source AI tools into a single platform:

| Component | Project | Stars | What it does |
|-----------|---------|-------|-------------|
| **Token Compression** | [Headroom](https://github.com/headroomlabs-ai/headroom) | 68K | SmartCrusher, ML model, reversible CCR |
| **MCP Server** | [FastMCP](https://github.com/PrefectHQ/fastmcp) | 27K | Expose tools via Model Context Protocol |
| **Agent Patterns** | [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.5K | Router, orchestrator-workers, map-reduce |
| **Multi-Agent** | [MetaGPT](https://github.com/geekan/MetaGPT) | 70K | Software company simulation |
| **Query-Aware** | [SuperCompress](https://github.com/Supercompress/Supercompress) | 65 | Keeps answer-critical lines |
| **14-Stage Pipeline** | [Claw Compactor](https://github.com/open-compress/claw-compactor) | -- | JSON tabularization, log crunching, AST |
| **Causal Inference** | [Netflix OCI Agent](https://github.com/Netflix-Skunkworks/oci-agent) | 47 | Actor-critic causal analysis |

---

## Architecture

```
+------------------------------------------------------------------+
|                      AgentForge Platform                          |
+------------------------------------------------------------------+
|                                                                    |
|  +------------------+  +------------------+  +------------------+ |
|  | Headroom Engine  |  | Claw Compactor   |  | SuperCompress    | |
|  | (SmartCrusher)   |  | (14-stage)       |  | (Query-aware)    | |
|  +--------+---------+  +--------+---------+  +--------+---------+ |
|           |                     |                     |            |
|           +----------+----------+----------+----------+            |
|                      |                                            |
|              +-------v--------+                                  |
|              | Unified Router |  (picks best engine)              |
|              +-------+--------+                                  |
|                      |                                            |
|  +-------------------v-----------------------------------------+ |
|  |                    MCP Server (FastMCP)                      | |
|  |  compress_text | compress_json | compress_logs | compare     | |
|  +-------------------+-----------------------------------------+ |
|                      |                                            |
|  +-------------------v-----------------------------------------+ |
|  |              Agent Orchestrator (mcp-agent)                  | |
|  |  Router -> DataAnalyst -> CompressionExpert -> Synthesizer  | |
|  +-------------------+-----------------------------------------+ |
|                      |                                            |
|  +-------------------v-----------------------------------------+ |
|  |            Netflix Analysis Engine (MetaGPT)                 | |
|  |  Catalog | Recommendations | Temporal | Geographic | Genre   | |
|  +-------------------+-----------------------------------------+ |
|                      |                                            |
|  +-------------------v-----------------------------------------+ |
|  |           Causal Inference (Netflix OCI Agent)               | |
|  |  Actor -> Critic -> Spec Revision -> ATE Estimation          | |
|  +------------------------------------------------------------+ |
|                                                                    |
|  +------------------------------------------------------------+ |
|  |               Streamlit Dashboard                           | |
|  |  Compression | Analysis | Recommendations | Causal          | |
|  +------------------------------------------------------------+ |
+------------------------------------------------------------------+
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/Youssef-AMARZOU/AgentForge-Platform.git
cd AgentForge-Platform

# Install
pip install -r requirements.txt

# Run benchmark
python main.py benchmark

# Run Netflix analysis
python main.py analyze

# Start MCP server (for Claude Code, Cursor, etc.)
python main.py mcp

# Launch dashboard
python main.py dashboard
```

---

## Project Structure

```
AgentForge-Platform/
|
+-- main.py                              # Main entry point
+-- benchmark.py                         # Compression benchmark
+-- requirements.txt
+-- LICENSE
|
+-- core/
|   +-- compression/
|   |   +-- engines.py                   # Headroom + Claw + SuperCompress
|   +-- agents/
|   |   +-- orchestrator.py              # Router, orchestrator-workers, parallel
|   +-- mcp/
|   |   +-- server.py                    # FastMCP server
|   +-- netflix/
|   |   +-- analysis.py                  # Netflix catalog analysis
|   +-- causal/
|       +-- inference.py                 # Actor-critic causal inference
|
+-- dashboard/
|   +-- app.py                           # Streamlit dashboard
|
+-- configs/
|   +-- default.yaml
|
+-- data/
|   +-- netflix_titles.csv               # 8,800+ Netflix titles
|
+-- results/
    +-- benchmark_results.json
```

---

## Features

### 1. Unified Compression Layer

Three engines, one API:

```python
from core.compression.engines import compress

result = compress(json_data, engine="auto")
# Headroom for JSON, Claw for logs, SuperCompress for query-aware
```

| Engine | Best For | Compression |
|--------|----------|-------------|
| Headroom | JSON, API responses | 40-99% |
| Claw Compactor | Logs, code, structured data | 15-82% |
| SuperCompress | Query-aware context | 60-67% |

### 2. MCP Server

Expose compression as MCP tools for Claude Code, Cursor, Copilot:

```bash
python main.py mcp
```

Tools: `compress_text`, `compress_json_payload`, `compress_server_logs`, `compare_engines`

### 3. Agent Orchestration

mcp-agent patterns built in:

- **Router** -- routes tasks to the best agent
- **Orchestrator-Workers** -- plan -> dispatch -> collect -> synthesize
- **Parallel Executor** -- fan-out map-reduce

### 4. Netflix Analysis

Multi-agent analysis engine:

- Temporal trends (movies vs TV by year)
- Geographic distribution (top countries)
- Genre analysis
- Rating distribution
- Content recommendations

### 5. Causal Inference

Netflix OCI Agent pattern:

- Actor drafts causal specs
- Critic reviews results
- Spec revision loop
- ATE estimation with confidence intervals

### 6. Streamlit Dashboard

Interactive visualization:

- Compression comparison (all engines side-by-side)
- Netflix catalog analysis with charts
- Content recommendations
- Causal inference explorer

---

## Requirements

- Python 3.10+
- `headroom-ai[all]` -- token compression
- `fastmcp` -- MCP server
- `pandas` -- data processing
- `streamlit` -- dashboard
- `plotly` -- charts
- `tiktoken` -- token counting
- `rich` -- terminal output

---

## Built With

| Project | GitHub | Stars |
|---------|--------|-------|
| Headroom | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 68K |
| FastMCP | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 27K |
| mcp-agent | [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.5K |
| MetaGPT | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | 70K |
| Netflix OCI Agent | [Netflix-Skunkworks/oci-agent](https://github.com/Netflix-Skunkworks/oci-agent) | 47 |
| Claw Compactor | [open-compress/claw-compactor](https://github.com/open-compress/claw-compactor) | -- |
| SuperCompress | [Supercompress/Supercompress](https://github.com/Supercompress/Supercompress) | 65 |

---

## Credits

This project merges patterns and APIs from 7 open-source projects:

- **[Headroom](https://github.com/headroomlabs-ai/headroom)** by [Tejas Chopra](https://github.com/chopratejas) (Netflix) -- token compression engine
- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** by Prefect -- MCP server framework
- **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** by LastMile AI -- agent orchestration patterns
- **[MetaGPT](https://github.com/geekan/MetaGPT)** -- multi-agent framework
- **[Netflix OCI Agent](https://github.com/Netflix-Skunkworks/oci-agent)** by Netflix Skunkworks -- causal inference
- **[Claw Compactor](https://github.com/open-compress/claw-compactor)** -- 14-stage compression pipeline
- **[SuperCompress](https://github.com/Supercompress/Supercompress)** -- query-aware compression

---

## License

MIT -- see [LICENSE](LICENSE) for details.

Individual components are licensed under their respective licenses (Apache 2.0, MIT, AGPL).
