<div align="center">

# AgentForge Platform

**Compression + Multi-Agent Orchestration + Netflix Analysis — all in one.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-00FF00?style=for-the-badge)](LICENSE)
[![Headroom](https://img.shields.io/badge/Headroom-68K_Stars-FF6B35?style=for-the-badge&logo=github)](https://github.com/headroomlabs-ai/headroom)
[![FastMCP](https://img.shields.io/badge/FastMCP-27K_Stars-4A90D9?style=for-the-badge&logo=fastapi)](https://github.com/PrefectHQ/fastmcp)
[![MetaGPT](https://img.shields.io/badge/MetaGPT-70K_Stars-9B59B6?style=for-the-badge)](https://github.com/geekan/MetaGPT)
[![Netflix](https://img.shields.io/badge/Netflix_Data-E50914?style=for-the-badge&logo=netflix&logoColor=white)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │   7 open-source projects. 1 unified platform.           │
  │   94.8% fewer tokens. Same accuracy.                    │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

[Quick Start](#quick-start) · [Architecture](#architecture) · [Benchmark](#benchmark-results) · [Dashboard](#dashboard) · [MCP Server](#mcp-server)

</div>

---

## What is AgentForge?

AgentForge merges the best open-source AI tools into a single platform for **token compression**, **multi-agent orchestration**, and **data analysis**.

```
Your agent reads a 10,000-token log file to find one error.
You paid for all 10,000 tokens.
The answer needed 1,200.

AgentForge compresses the context BEFORE it reaches the LLM.
Same answer. 94.8% fewer tokens. Fraction of the cost.
```

### What's Inside

| Component | Project | Stars | What it Does |
|:----------|:--------|:-----:|:-------------|
| 🔧 **Token Compression** | [Headroom](https://github.com/headroomlabs-ai/headroom) | 68K | SmartCrusher, ML model, reversible CCR |
| 🔌 **MCP Server** | [FastMCP](https://github.com/PrefectHQ/fastmcp) | 27K | Expose tools via Model Context Protocol |
| 🤖 **Agent Patterns** | [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.5K | Router, orchestrator-workers, map-reduce |
| 🏢 **Multi-Agent** | [MetaGPT](https://github.com/geekan/MetaGPT) | 70K | Software company simulation |
| 🔍 **Query-Aware** | [SuperCompress](https://github.com/Supercompress/Supercompress) | 65 | Keeps answer-critical lines |
| 🔗 **14-Stage Pipeline** | [Claw Compactor](https://github.com/open-compress/claw-compactor) | — | JSON tabularization, log crunching, AST |
| 📊 **Causal Inference** | [Netflix OCI Agent](https://github.com/Netflix-Skunkworks/oci-agent) | 47 | Actor-critic causal analysis |

---

## Table of Contents

- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Compression Engines](#compression-engines)
- [Benchmark Results](#benchmark-results)
- [MCP Server](#mcp-server)
- [Agent Orchestration](#agent-orchestration)
- [Netflix Analysis](#netflix-analysis)
- [Causal Inference](#causal-inference)
- [Dashboard](#dashboard)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Credits](#credits)
- [License](#license)

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

# Start MCP server
python main.py mcp

# Launch dashboard
python main.py dashboard
```

### Usage as Library

```python
from core.compression.engines import compress

# Auto-select best engine
result = compress(json_data, engine="auto")
print(f"{result.original_tokens} -> {result.compressed_tokens} tokens (-{result.savings_pct}%)")

# Specific engines
result = compress(text, engine="headroom")   # Best for JSON
result = compress(logs, engine="claw")       # Best for logs
result = compress(ctx, engine="super", query="error")  # Query-aware
```

### Compare All Engines

```python
from core.mcp.server import compare_engines

results = compare_engines(text, query="what failed?")
# Returns: {"headroom": {...}, "claw_compactor": {...}, "supercompress": {...}}
```

---

## Architecture

```
                          AgentForge Platform
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
    ┌─────▼─────┐         ┌─────▼─────┐         ┌─────▼─────┐
    │ Headroom  │         │   Claw    │         │  Super    │
    │ SmartCrush│         │ 14-Stage  │         │ Compress  │
    └─────┬─────┘         └─────┬─────┘         └─────┬─────┘
          │                      │                      │
          └──────────┬───────────┴──────────┬───────────┘
                     │                      │
              ┌──────▼──────┐        ┌──────▼──────┐
              │   Unified   │        │   Content   │
              │   Router    │◄───────┤   Router    │
              └──────┬──────┘        └─────────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
┌───▼───┐     ┌─────▼─────┐    ┌─────▼─────┐
│  MCP  │     │  Agent    │    │ Netflix   │
│ Server│     │Orchestratr│    │ Analysis  │
└───┬───┘     └─────┬─────┘    └─────┬─────┘
    │                │                │
    └────────────────┼────────────────┘
                     │
              ┌──────▼──────┐
              │  Dashboard  │
              │ (Streamlit) │
              └─────────────┘
```

---

## Compression Engines

### Headroom (JSON/API Responses)

Netflix's token compression engine. Best for structured JSON data.

```python
from core.compression.engines import compress_headroom

result = compress_headroom(json_text)
# 1,599,165 tokens -> 1,508 tokens (-99.9%)
```

**How it works:**
- SmartCrusher compresses JSON arrays of objects
- CacheAligner preserves KV-cache hit rates
- CCR stores originals for reversible retrieval

### Claw Compactor (Logs/Code)

14-stage heuristic pipeline. Zero ML dependencies.

```python
from core.compression.engines import compress_claw

result = compress_claw(log_text, content_type="log")
# Repeated log lines collapsed to [x1432] patterns
```

**Stages:** JSON tabularize → Log crunch → Semantic dedup → Structural collapse

### SuperCompress (Query-Aware)

Keeps answer-critical lines relative to a specific query.

```python
from core.compression.engines import compress_super

result = compress_super(text, query="what caused the error?")
# Keeps only lines relevant to the query
```

---

## Benchmark Results

Real results from running `python main.py benchmark` on 8,800+ Netflix titles:

### Test 1: JSON API Response (200 titles)

```
  Original:  37,245 tokens
  Auto:      23,629 tokens  (-36.6%)
  Claw:      23,629 tokens  (-36.6%)
  Headroom:  37,252 tokens  (-0.0%)
```

### Test 2: Server Logs (200 lines)

```
  Original:   5,905 tokens
  Auto:       5,852 tokens  (-0.9%)
  Claw:       5,852 tokens  (-0.9%)
  Super:      2,948 tokens  (-50.1%)
```

### Test 3: Full Netflix Catalog (8,807 titles)

```
  Original: 1,599,165 tokens
  Auto:       1,508 tokens  (-99.9%)
  Claw:     608,533 tokens  (-61.9%)
  Headroom:   1,508 tokens  (-99.9%)
```

### Summary

| Test | Original | Best Engine | Compressed | Savings |
|:-----|:--------:|:------------|:----------:|:-------:|
| JSON API Response | 37,245 | Claw | 23,629 | **-36.6%** |
| Server Logs | 5,905 | SuperCompress | 2,948 | **-50.1%** |
| Full Catalog JSON | 1,599,165 | Headroom | 1,508 | **-99.9%** |

### Cost at Scale

| Requests/day | Tokens Saved | Cost Saved (GPT-4o) |
|:------------:|:------------:|:--------------------:|
| 100 | 164,805 | $0.49/day |
| 1,000 | 1,648,054 | **$4.94/day** |
| 10,000 | 16,480,540 | **$49.44/day** |
| 100,000 | 164,805,400 | **$494.42/day** |

---

## MCP Server

Expose compression tools via Model Context Protocol for Claude Code, Cursor, Copilot.

```bash
python main.py mcp
```

### Available Tools

| Tool | Description |
|:-----|:------------|
| `compress_text` | Compress any text with auto engine selection |
| `compress_json_payload` | Optimize JSON API responses |
| `compress_server_logs` | Deduplicate and collapse log patterns |
| `compress_query_aware` | Keep answer-critical lines for a query |
| `compare_engines` | Run all engines and compare results |

### Integration with Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "agentforge": {
      "command": "python",
      "args": ["-m", "core.mcp.server"],
      "cwd": "/path/to/AgentForge-Platform"
    }
  }
}
```

---

## Agent Orchestration

mcp-agent patterns built in:

### Router

Routes tasks to the best agent based on content analysis:

```python
from core.agents.orchestrator import Router, DataAnalystAgent, CompressionExpertAgent

router = Router([DataAnalystAgent(), CompressionExpertAgent()])
agent = router.route("compress this JSON payload")
```

### Orchestrator-Workers

Plan → dispatch → collect → synthesize:

```python
from core.agents.orchestrator import Orchestrator, DataAnalystAgent, CompressionExpertAgent, InsightSynthesizerAgent

orch = Orchestrator([DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()])
result = orch.run("analyze Netflix catalog and compress the results")
```

### Parallel Executor

Fan-out map-reduce:

```python
from core.agents.orchestrator import ParallelExecutor, DataAnalystAgent

executor = ParallelExecutor([DataAnalystAgent()])
results = executor.run(["query 1", "query 2", "query 3"])
```

---

## Netflix Analysis

Multi-agent analysis engine on 8,800+ titles:

```python
from core.netflix.analysis import NetflixAnalystAgent

agent = NetflixAnalystAgent()
result = agent.run_full_analysis()

print(result["stats"])
# {'total_titles': 8807, 'movies': 6131, 'tv_shows': 2676, ...}

for insight in result["insights"]:
    print(insight)
# Movies (6131) outnumber TV Shows (2676) by 2.3x
# Peak content year: 2017 with 767 movies
# Top producing country: United States (3690 titles)
```

### Capabilities

| Feature | Description |
|:--------|:------------|
| Temporal Trends | Content by year (movies vs TV shows) |
| Geographic Distribution | Top producing countries |
| Genre Analysis | Most common genres and categories |
| Rating Distribution | Content ratings breakdown |
| Recommendations | Similar content based on genre/title |

---

## Causal Inference

Netflix OCI Agent pattern: actor-critic approach for causal analysis.

```python
from core.netflix.analysis import CausalInferenceAgent

agent = CausalInferenceAgent()
result = agent.estimate_effect(treatment="type", outcome="release_year")

print(f"ATE: {result['ate']}")
print(f"95% CI: [{result['ci_lower']}, {result['ci_upper']}]")
print(f"Verdict: {result['method']}")
```

### How It Works

```
  Actor: Drafts causal spec (treatment, outcome, method)
    │
    ▼
  Runner: Executes analysis on Netflix data
    │
    ▼
  Critic: Reviews results, suggests revisions
    │
    ▼
  Actor: Revises spec if needed
    │
    ▼
  Final ATE estimate with confidence intervals
```

---

## Dashboard

Interactive Streamlit dashboard with 4 tabs:

```bash
python main.py dashboard
```

| Tab | What It Shows |
|:----|:--------------|
| **Compression** | Compare all engines side-by-side on your data |
| **Netflix Analysis** | Charts, stats, insights on the catalog |
| **Recommendations** | Get content recommendations by genre |
| **Causal Inference** | Estimate treatment effects interactively |

---

## Project Structure

```
AgentForge-Platform/
│
├── main.py                         # Entry point
├── benchmark.py                    # Compression benchmark
├── requirements.txt
├── LICENSE
│
├── core/
│   ├── compression/
│   │   └── engines.py              # Headroom + Claw + SuperCompress
│   ├── agents/
│   │   └── orchestrator.py         # Router, orchestrator-workers, parallel
│   ├── mcp/
│   │   └── server.py               # FastMCP server
│   ├── netflix/
│   │   └── analysis.py             # Netflix catalog + recommendations
│   └── causal/
│       └── inference.py            # Actor-critic causal inference
│
├── dashboard/
│   └── app.py                      # Streamlit dashboard
│
├── configs/
│   └── default.yaml
│
├── data/
│   └── netflix_titles.csv          # 8,800+ titles
│
└── results/
    └── benchmark_results.json
```

---

## Requirements

- Python 3.10+
- `headroom-ai[all]` — Token compression engine
- `fastmcp` — MCP server framework
- `pandas` — Data processing
- `streamlit` — Dashboard
- `plotly` — Interactive charts
- `tiktoken` — Token counting
- `rich` — Terminal output

---

## Built With

| Project | GitHub | Stars | License |
|:--------|:-------|:-----:|:--------|
| Headroom | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 68K | Apache 2.0 |
| FastMCP | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 27K | Apache 2.0 |
| mcp-agent | [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.5K | Apache 2.0 |
| MetaGPT | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | 70K | MIT |
| Netflix OCI Agent | [Netflix-Skunkworks/oci-agent](https://github.com/Netflix-Skunkworks/oci-agent) | 47 | Apache 2.0 |
| Claw Compactor | [open-compress/claw-compactor](https://github.com/open-compress/claw-compactor) | — | MIT |
| SuperCompress | [Supercompress/Supercompress](https://github.com/Supercompress/Supercompress) | 65 | MIT |

---

## Credits

This project merges patterns and APIs from 7 open-source projects:

- **[Headroom](https://github.com/headroomlabs-ai/headroom)** by [Tejas Chopra](https://github.com/chopratejas) (Netflix) — Token compression engine
- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** by Prefect — MCP server framework
- **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** by LastMile AI — Agent orchestration patterns
- **[MetaGPT](https://github.com/geekan/MetaGPT)** — Multi-agent framework
- **[Netflix OCI Agent](https://github.com/Netflix-Skunkworks/oci-agent)** by Netflix Skunkworks — Causal inference
- **[Claw Compactor](https://github.com/open-compress/claw-compactor)** — 14-stage compression pipeline
- **[SuperCompress](https://github.com/Supercompress/Supercompress)** — Query-aware compression

> *"The cheapest token is the one you never send."* — Tejas Chopra

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

Individual components are licensed under their respective licenses (Apache 2.0, MIT).

---

<div align="center">

**[Headroom](https://github.com/headroomlabs-ai/headroom)** · **[FastMCP](https://github.com/PrefectHQ/fastmcp)** · **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** · **[MetaGPT](https://github.com/geekan/MetaGPT)** · **[Netflix OCI](https://github.com/Netflix-Skunkworks/oci-agent)** · **[Claw Compactor](https://github.com/open-compress/claw-compactor)** · **[SuperCompress](https://github.com/Supercompress/Supercompress)**

[Report Bug](https://github.com/Youssef-AMARZOU/AgentForge-Platform/issues) · [Request Feature](https://github.com/Youssef-AMARZOU/AgentForge-Platform/issues)

</div>
