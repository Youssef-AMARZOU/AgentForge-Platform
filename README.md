<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a1a,50:0f3460,100:1a1a3e&height=200&section=header&text=AgentForge%20Platform&fontSize=48&fontColor=ffffff&animation=fadeIn" alt="AgentForge Platform"/>

<div align="center">

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&pause=1000&color=00d4aa&width=600&lines=Token+Compression+%2B+Multi-Agent+Orchestration;Netflix+Data+Analysis+%2B+Causal+Inference;7+Open-Source+Projects+Unified+in+One+Platform&fontColor=00d4aa&center=true&vCenter=true&duration=2500&repeat=true" alt="Typing SVG" /></a>

<br>
<br>

<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform">
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</a>
<a href="https://github.com/headroomlabs-ai/headroom">
<img src="https://img.shields.io/badge/Headroom-68k%20Stars-FF6B35?style=for-the-badge&logo=github" alt="Headroom">
</a>
<a href="https://github.com/PrefectHQ/fastmcp">
<img src="https://img.shields.io/badge/FastMCP-27k%20Stars-4A90D9?style=for-the-badge&logo=fastapi" alt="FastMCP">
</a>
<a href="https://github.com/geekan/MetaGPT">
<img src="https://img.shields.io/badge/MetaGPT-70k%20Stars-9B59B6?style=for-the-badge" alt="MetaGPT">
</a>
<a href="https://github.com/lastmile-ai/mcp-agent">
<img src="https://img.shields.io/badge/mcp--agent-8.5k%20Stars-2ECC71?style=for-the-badge" alt="mcp-agent">
</a>
<a href="https://github.com/Netflix-Skunkworks/oci-agent">
<img src="https://img.shields.io/badge/Netflix_OCI-E50914?style=for-the-badge&logo=netflix&logoColor=white" alt="Netflix OCI">
</a>

<br>
<br>

<img src="https://skillicons.dev/icons?i=python,fastapi,streamlit,docker,github,git,vscode,linux&theme=dark" alt="Tech Stack" />

<br>
<br>

<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform/blob/main/LICENSE">
<img src="https://img.shields.io/badge/License-MIT-00d4aa?style=for-the-badge" alt="License">
</a>
<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform/stargazers">
<img src="https://img.shields.io/github/stars/Youssef-AMARZOU/AgentForge-Platform?style=for-the-badge&logo=github&color=FF6B35" alt="Stars">
</a>
<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform/network/members">
<img src="https://img.shields.io/github/forks/Youssef-AMARZOU/AgentForge-Platform?style=for-the-badge&logo=github&color=3498DB" alt="Forks">
</a>
<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform/issues">
<img src="https://img.shields.io/github/issues/Youssef-AMARZOU/AgentForge-Platform?style=for-the-badge&logo=github&color=E74C3C" alt="Issues">
</a>
<a href="https://github.com/Youssef-AMARZOU/AgentForge-Platform/commits/main">
<img src="https://img.shields.io/github/last-commit/Youssef-AMARZOU/AgentForge-Platform?style=for-the-badge&logo=github&color=9B59B6" alt="Last Commit">
</a>

</div>

---

<br>

## Table of Contents

- [What is AgentForge](#what-is-agentforge)
- [Benchmark Results](#benchmark-results)
- [Quick Start](#quick-start)
- [Integrated Projects](#integrated-projects)
- [Architecture](#architecture)
- [Compression Engines](#compression-engines)
- [Engine Comparison](#engine-comparison)
- [Agent Orchestration](#agent-orchestration)
- [MCP Server](#mcp-server)
- [Netflix Analysis](#netflix-analysis)
- [Causal Inference](#causal-inference)
- [Landing Page](#landing-page)
- [Project Structure](#project-structure)
- [Tests](#tests)
- [Examples](#examples)
- [Cost Analysis](#cost-analysis)
- [API Reference](#api-reference)
- [License](#license)

---

<br>

## What is AgentForge

AgentForge is a unified platform that merges **7 open-source AI projects** into one cohesive system. It provides token compression, multi-agent orchestration, MCP server integration, Netflix-scale data analysis, and causal inference — all in a single installable Python package.

### The Problem

LLM API costs scale linearly with token count. A 15,000-token JSON response costs **$0.045 per request**. At 1,000 requests/day, that is **$135/month**. AgentForge reduces token usage by **50-99%** while preserving data accuracy.

### The Solution

AgentForge combines three compression engines, a multi-agent orchestrator, and a causal inference engine. One call compresses your data. One router dispatches to the right agent. One platform replaces five separate tools.

---

<br>

## Benchmark Results

<table>
<tr>
<td align="center">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:FF6B35,100:FF6B35&height=80&width=200&text=JSON+API&fontSize=12&fontColor=ffffff" alt="JSON API">
<br><br>
<b>15,553  ->  8,105 tokens</b>
<br><span style="color:#2ecc71;font-size:20px"><b>-47.9%</b></span>
<br><sub>Best engine: headroom</sub>
</td>
<td align="center">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:E74C3C,100:E74C3C&height=80&width=200&text=Server+Logs&fontSize=12&fontColor=ffffff" alt="Server Logs">
<br><br>
<b>31,899  ->  8,450 tokens</b>
<br><span style="color:#2ecc71;font-size:20px"><b>-73.5%</b></span>
<br><sub>Best engine: claw_compactor</sub>
</td>
<td align="center">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:2ECC71,100:2ECC71&height=80&width=200&text=Source+Code&fontSize=12&fontColor=ffffff" alt="Source Code">
<br><br>
<b>28,200  ->  9,300 tokens</b>
<br><span style="color:#2ecc71;font-size:20px"><b>-67.0%</b></span>
<br><sub>Best engine: claw_compactor</sub>
</td>
</tr>
</table>

### Detailed Comparison

| Test Case | Original | Auto | Headroom | Claw | SuperCompress | Best Engine | Savings |
|-----------|----------|------|----------|------|---------------|-------------|---------|
| JSON API (200 records) | 15,553 | 8,105 | 8,105 | 15,553 | 15,553 | headroom | **-47.9%** |
| Server Logs (500 lines) | 31,899 | 8,450 | 16,449 | 8,450 | 16,449 | claw | **-73.5%** |
| Source Code (100 funcs) | 28,200 | 9,300 | 14,100 | 9,300 | 18,800 | claw | **-67.0%** |
| Full Catalog (8,807 titles) | 1,599,165 | 1,508 | 1,508 | 1,508 | 1,508 | headroom | **-99.9%** |

---

<br>

## Quick Start

```bash
# Clone
git clone https://github.com/Youssef-AMARZOU/AgentForge-Platform.git
cd AgentForge-Platform

# Install
pip install -e .

# Run
python main.py benchmark    # Compression benchmark
python main.py analyze      # Netflix catalog analysis
python main.py mcp          # Start MCP server
python main.py dashboard    # Launch Streamlit UI
```

### Verify Installation

```bash
# Run all tests (85 tests)
pytest

# Run showcase
python examples/showcase.py
```

---

<br>

## Integrated Projects

<table>
<tr>
<td align="center">
<a href="https://github.com/headroomlabs-ai/headroom">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:FF6B35,100:FF6B35&height=80&width=160&text=Headroom&fontSize=11&fontColor=ffffff" alt="Headroom"/>
<br><sub><b>68k Stars</b></sub>
<br><sub>Token Compression</sub>
<br><sub>SmartCrusher + ML</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/PrefectHQ/fastmcp">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:3498DB,100:3498DB&height=80&width=160&text=FastMCP&fontSize=11&fontColor=ffffff" alt="FastMCP"/>
<br><sub><b>27k Stars</b></sub>
<br><sub>MCP Server</sub>
<br><sub>Tool Integration</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/lastmile-ai/mcp-agent">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:9B59B6,100:9B59B6&height=80&width=160&text=mcp-agent&fontSize=11&fontColor=ffffff" alt="mcp-agent"/>
<br><sub><b>8.5k Stars</b></sub>
<br><sub>Agent Patterns</sub>
<br><sub>Orchestration</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/geekan/MetaGPT">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:2ECC71,100:2ECC71&height=80&width=160&text=MetaGPT&fontSize=11&fontColor=ffffff" alt="MetaGPT"/>
<br><sub><b>70k Stars</b></sub>
<br><sub>Multi-Agent</sub>
<br><sub>Role-Based</sub>
</a>
</td>
</tr>
<tr>
<td align="center">
<a href="https://github.com/open-compress/claw-compactor">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:E74C3C,100:E74C3C&height=80&width=160&text=Claw&fontSize=11&fontColor=ffffff" alt="Claw"/>
<br><sub><b>14-Stage</b></sub>
<br><sub>Heuristic</sub>
<br><sub>Compression</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/Supercompress/Supercompress">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:F39C12,100:F39C12&height=80&width=160&text=SuperCompress&fontSize=11&fontColor=ffffff" alt="SuperCompress"/>
<br><sub><b>Query-Aware</b></sub>
<br><sub>Extractive</sub>
<br><sub>Compression</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/Netflix-Skunkworks/oci-agent">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1ABC9C,100:1ABC9C&height=80&width=160&text=Netflix+OCI&fontSize=11&fontColor=ffffff" alt="Netflix OCI"/>
<br><sub><b>Causal</b></sub>
<br><sub>Inference</sub>
<br><sub>Actor-Critic</sub>
</a>
</td>
</tr>
</table>

---

<br>

## Architecture

```
                            AgentForge Platform
                                   |
            +----------------------+----------------------+
            |                      |                      |
      +-----v-----+         +-----v-----+         +-----v-----+
      | Headroom   |         |   Claw    |         |  Super    |
      | SmartCrush |         | 14-Stage  |         | Compress  |
      | + ML Model |         | Heuristic |         | Query-    |
      | + CCR      |         | Pipeline  |         | Aware     |
      +-----+------+         +-----+-----+         +-----+-----+
            |                      |                      |
            +----------+-----------+----------+-----------+
                       |                      |
                +------v------+        +------v------+
                |   Unified   |        |   Content   |
                |   Router    |<-------+   Detector  |
                +------+------+        +-------------+
                       |
       +---------------+---------------+
       |               |               |
   +---v---+     +----v----+     +----v----+
   |  MCP  |     |  Agent  |     | Netflix |
   | Server|     |Orchestr.|     | Analysis|
   +---+---+     +----+----+     +----+----+
       |               |               |
       |         +-----+-----+         |
       |         |           |         |
       |    +----v----+ +----v----+    |
       |    |Parallel | |Causal   |    |
       |    |Executor | |Inference|    |
       |    +---------+ +---------+    |
       |               |               |
       +-------+-------+-------+-------+
               |               |
        +------v------+ +------v------+
        |  Dashboard  | |  Landing    |
        | (Streamlit) | | (HTML)      |
        +-------------+ +-------------+
```

---

<br>

## Compression Engines

### Headroom (ML-Powered)

Uses a trained ML model to detect removable tokens. Best for structured JSON and API responses.

```python
from core.compression.engines import compress_headroom

result = compress_headroom(json_data, content_type="json")
print(result.compressed_tokens)   # 8,105
print(result.savings_pct)         # -47.9%
print(result.engine)              # "headroom"
```

### Claw Compactor (14-Stage Heuristic)

Applies 14 sequential compression stages: deduplication, whitespace removal, stopword filtering, pattern compression, etc. Best for logs and code.

```python
from core.compression.engines import compress_claw

result = compress_claw(server_logs, content_type="log")
print(result.compressed_tokens)   # 8,450
print(result.savings_pct)         # -73.5%
print(result.engine)              # "claw_compactor"
```

### SuperCompress (Query-Aware)

Extractive compression that keeps only lines relevant to a query. Best when you need to filter large contexts.

```python
from core.compression.engines import compress_super

result = compress_super(large_context, query="error patterns")
print(result.compressed_tokens)   # varies
print(result.savings_pct)         # varies
print(result.engine)              # "supercompress_style"
```

### Auto Engine Selection

```python
from core.compression.engines import compress

# Automatically selects the best engine
result = compress(data, engine="auto")
print(result.engine)  # "headroom", "claw_compactor", or "supercompress_style"
```

---

<br>

## Engine Comparison

| Feature | Headroom | Claw Compactor | SuperCompress |
|---------|----------|----------------|---------------|
| **Method** | ML model + CCR | 14-stage heuristic | Query-aware extractive |
| **Best for** | JSON, API responses | Logs, code, tabular | Large contexts, filtering |
| **Speed** | ~1000ms | ~20ms | ~20ms |
| **Compression** | 40-50% | 60-75% | 30-90% (query dependent) |
| **Accuracy** | High (ML-guided) | High (rule-based) | High (keeps relevant lines) |
| **Dependencies** | Headroom ML model | None (pure Python) | None (pure Python) |
| **Star Count** | 68k | N/A | N/A |
| **Type** | Token-level | Line-level | Line-level |

### When to Use Each

| Use Case | Recommended Engine | Why |
|----------|-------------------|-----|
| JSON API responses | Headroom | ML model understands JSON structure |
| Server logs | Claw | 14-stage pipeline excels at log dedup |
| Source code | Claw | Pattern compression removes boilerplate |
| Large document + query | SuperCompress | Keeps only query-relevant lines |
| Unknown content type | Auto | Tests all and picks the best |

---

<br>

## Agent Orchestration

### Router

Routes queries to the best agent based on keyword matching.

```python
from core.agents.orchestrator import Router, CompressionExpertAgent, DataAnalystAgent

router = Router([CompressionExpertAgent(), DataAnalystAgent()])

# Routes to CompressionExpert
agent = router.route("compress this JSON payload")
print(agent.__class__.__name__)  # "CompressionExpertAgent"

# Routes to DataAnalyst
agent = router.route("analyze the Netflix catalog")
print(agent.__class__.__name__)  # "DataAnalystAgent"
```

### Routing Rules

| Keywords | Routes To |
|----------|-----------|
| compress, token, reduce, optimize | CompressionExpert |
| analyze, stat, pattern, trend, data | DataAnalyst |
| summary, combine, synthesize, report | InsightSynthesizer |

### Orchestrator-Workers

Plans, dispatches, collects, and synthesizes results from multiple agents.

```python
from core.agents.orchestrator import Orchestrator, CompressionExpertAgent, DataAnalystAgent, InsightSynthesizerAgent

orch = Orchestrator([
    CompressionExpertAgent(),
    DataAnalystAgent(),
    InsightSynthesizerAgent()
])

result = orch.run("analyze Netflix catalog and compress the results")
print(result["routed_to"])  # "DataAnalystAgent"
print(result["status"])     # "ok"
print(result["tokens"])     # token count
```

### Parallel Executor

Fan-out map-reduce across multiple queries.

```python
from core.agents.orchestrator import ParallelExecutor, DataAnalystAgent

executor = ParallelExecutor([DataAnalystAgent()])

queries = [
    "analyze Netflix catalog",
    "compute content statistics",
    "find top countries"
]

results = executor.run(queries)
# Returns list of results, one per query
```

---

<br>

## MCP Server

Start the MCP server to expose compression tools via the Model Context Protocol.

```bash
python main.py mcp
```

### Available Tools

| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| `compress_text` | Auto engine selection | text, content_type | compressed text, tokens |
| `compress_json_payload` | Optimize JSON responses | json_string | compressed JSON, savings |
| `compress_server_logs` | Deduplicate log patterns | log_string | compressed logs, savings |
| `compress_query_aware` | Keep query-relevant lines | text, query | filtered text, savings |
| `compare_engines` | Run all engines, return comparison | text, content_type | per-engine results |
| `analyze_netflix` | Netflix catalog analysis | none | stats, insights |
| `get_stats` | Platform statistics | none | engine counts, test count |

### Example MCP Call

```python
from core.mcp.server import compress_text

result = compress_text(
    text='{"users": [{"id": 1, "name": "Alice"}, ...]}',
    content_type="json"
)
print(result["compressed"])   # compressed text
print(result["tokens_before"])  # 15553
print(result["tokens_after"])   # 8105
print(result["engine"])         # "headroom"
```

---

<br>

## Netflix Analysis

### Full Analysis

```python
from core.netflix.analysis import NetflixAnalystAgent

agent = NetflixAnalystAgent()
result = agent.run_full_analysis()

# Stats
print(result["stats"])
# {
#   "total_titles": 8807,
#   "movies": 6131,
#   "tv_shows": 2676,
#   "countries": 748,
#   "year_range": "1925 - 2021",
#   "top_country": "United States (3690)"
# }

# Insights
for insight in result["insights"]:
    print(insight)
# Movies (6131) outnumber TV Shows (2676) by 2.3x
# Peak content year: 2017 with 767 movies
# Top producing country: United States (3690 titles)
```

### Search and Filter

```python
from core.netflix.analysis import NetflixCatalog

catalog = NetflixCatalog()

# Search by title
results = catalog.search("Breaking Bad")
print(len(results))  # number of matches

# Filter by country
us_shows = catalog.filter_by(country="United States")
print(len(us_shows))

# Filter by year
recent = catalog.filter_by(year=2020)
print(len(recent))
```

### Content Recommendations

```python
from core.netflix.analysis import NetflixRecommendationEngine

engine = NetflixRecommendationEngine()
recs = engine.recommend(title_id=1, n=5)
# Returns 5 similar titles
```

### Dataset

| Property | Value |
|----------|-------|
| File | `data/netflix_titles.csv` |
| Total Titles | 8,807 |
| Movies | 6,131 (69.6%) |
| TV Shows | 2,676 (30.4%) |
| Countries | 748 |
| Year Range | 1925 - 2021 |
| Top Country | United States (3,690) |
| Peak Year | 2017 (767 movies) |

---

<br>

## Causal Inference

Actor-Critic pattern for causal reasoning.

```python
from core.causal.inference import ActorCriticCausalAgent

agent = ActorCriticCausalAgent()

# Run causal inference
result = agent.run({
    "data": netflix_data,
    "treatment": "type",
    "outcome": "release_year"
})

print(result["ate"])      # Average Treatment Effect
print(result["critique"])  # Critic's review
```

### How It Works

1. **Actor** generates a treatment specification (what to test)
2. **Critic** reviews and validates the specification
3. Iterates until a valid causal estimate is produced
4. Returns ATE (Average Treatment Effect) with confidence

---

<br>

## Landing Page

The platform includes a modern landing page with Baseline-style animations.

```bash
# Generate the HTML report
python examples/generate_report.py

# Open in browser
open site/index.html
```

### Features

- Dark navy/teal/purple gradient theme
- Animated loader with progress bar
- Hero with gradient title and KPI cards
- Compression benchmark cards
- Chart.js bar and doughnut charts
- Cost at scale table
- Agent orchestration section
- Netflix analysis section
- Contact modal with form stub
- Fullscreen menu overlay
- Lenis smooth scroll
- IntersectionObserver reveals
- Adaptive rem scaling

---

<br>

## Project Structure

```
AgentForge-Platform/
|-- main.py                              # Entry point (benchmark|mcp|dashboard|analyze)
|-- benchmark.py                         # Compression benchmark runner
|-- pyproject.toml                       # Package config (pip install -e .)
|-- pytest.ini                           # Pytest configuration
|-- LICENSE                              # MIT License
|
|-- core/
|   |-- compression/
|   |   |-- engines.py                   # Headroom + Claw + SuperCompress
|   |
|   |-- agents/
|   |   |-- orchestrator.py              # Router, Orchestrator-Workers, Parallel
|   |
|   |-- mcp/
|   |   |-- server.py                    # FastMCP server with 7 tools
|   |
|   |-- netflix/
|   |   |-- analysis.py                  # Catalog, search, filter, recommendations
|   |
|   |-- causal/
|       |-- inference.py                 # Actor-Critic causal inference
|
|-- dashboard/
|   |-- app.py                           # Streamlit dashboard (4 tabs)
|
|-- examples/
|   |-- showcase.py                      # Before/after KPIs, cost savings
|   |-- basic_compression.py             # All compression engines
|   |-- agent_orchestration.py           # Router, orchestrator, parallel
|   |-- netflix_analysis.py             # Catalog, recommendations, causal
|   |-- mcp_server.py                   # All MCP tools
|   |-- causal_inference.py             # Actor-critic pattern
|   |-- dashboard_demo.py               # Launch Streamlit dashboard
|   |-- generate_report.py              # HTML report generator
|   |-- README.md                        # Examples documentation
|
|-- tests/
|   |-- test_compression.py             # 19 tests: engines, router, edge cases
|   |-- test_agents.py                  # 22 tests: router, orchestrator, parallel
|   |-- test_netflix.py                 # 21 tests: catalog, search, filter, causal
|   |-- test_causal.py                  # 15 tests: actor, critic, full agent
|   |-- test_mcp.py                     # 8 tests: all MCP tools + stats
|
|-- site/
|   |-- index.html                       # Landing page (47KB, dark theme)
|
|-- vendor/                              # Git subtree imports
|   |-- headroom/                        # Token compression (68k stars)
|   |-- fastmcp/                         # MCP server (27k stars)
|   |-- mcp-agent/                       # Agent patterns (8.5k stars)
|   |-- MetaGPT/                         # Multi-agent (70k stars)
|
|-- data/
|   |-- netflix_titles.csv               # 8,807 Netflix titles
|
|-- results/
    |-- report.html                      # Generated HTML report
```

---

<br>

## Tests

### Run All Tests

```bash
pytest
# 85 tests passed
```

### Test Suites

| Suite | Tests | Coverage |
|-------|-------|----------|
| `test_compression.py` | 19 | Token counting, all 3 engines, router, edge cases |
| `test_agents.py` | 22 | Router, Orchestrator, ParallelExecutor, all agent types |
| `test_netflix.py` | 21 | Catalog, search, filter, analyst, recommendations, causal |
| `test_causal.py` | 15 | Actor, Critic, full actor-critic agent |
| `test_mcp.py` | 8 | All 5 MCP tools + stats resource |

### Run Specific Suite

```bash
pytest tests/test_compression.py -v
pytest tests/test_agents.py -v
pytest tests/test_netflix.py -v
pytest tests/test_causal.py -v
pytest tests/test_mcp.py -v
```

### With Coverage

```bash
pytest --cov=core --cov-report=term-missing
```

---

<br>

## Examples

### Showcase (Before/After KPIs)

```bash
python examples/showcase.py
```

```
+----------------------------------------------------------------------+
| AgentForge Platform                                                  |
| Before vs After - Token Compression Comparison                       |
+----------------------------------------------------------------------+

 JSON API Response (200 records)
+------------------------------------------------------------------+
| Metric              |   Before  |    After   |      Savings |
|---------------------+-----------+------------+--------------|
| Tokens              |    15,553 |      8,105 |       -47.9% |
| Cost / request      |   $0.0467 |    $0.0243 |       -47.9% |
| Cost / 1K req       |    $46.66 |     $24.32 |   $22.34/day |

 Server Logs (500 lines)
+------------------------------------------------------------------+
| Tokens              |    31,899 |      8,450 |       -73.5% |
| Cost / 1K req       |    $95.70 |     $25.35 |   $70.35/day |

 Cost Savings at Scale
+--------------------------------------------------------------------+
| 100 req/day   |   $14.24  |   $4.97  |     $278/mo saved |
| 1,000 req/day |  $142.36  |  $49.66  |   $2,781/mo saved |
| 10,000 req/day| $1,423.56 | $496.65  |  $27,807/mo saved |
| 50,000 req/day| $7,117.80 | $2,483.25| $139,037/mo saved |
```

### Basic Compression

```bash
python examples/basic_compression.py
```

Tests all three engines on JSON, logs, and source code.

### Agent Orchestration

```bash
python examples/agent_orchestration.py
```

Demonstrates Router, Orchestrator-Workers, and Parallel executor.

### Netflix Analysis

```bash
python examples/netflix_analysis.py
```

Full catalog analysis, search, filter, recommendations, and causal inference.

### MCP Server

```bash
python examples/mcp_server.py
```

Tests all 5 MCP tools and the stats resource.

### Causal Inference

```bash
python examples/causal_inference.py
```

Actor-Critic pattern: Actor drafts specs, Critic reviews, iterates to ATE.

### Dashboard

```bash
python examples/dashboard_demo.py
```

Launches Streamlit dashboard with 4 tabs.

### HTML Report

```bash
python examples/generate_report.py
# Open results/report.html
```

Generates a modern dark-theme HTML report with charts.

---

<br>

## Cost Analysis

### Token Pricing (GPT-4o)

| Metric | Value |
|--------|-------|
| Input cost per 1K tokens | $0.003 |
| Output cost per 1K tokens | $0.015 |
| Average compression | -65.1% |

### Savings at Scale

| Requests / Day | Before | After | Saved / Day | Saved / Month |
|----------------|--------|-------|-------------|---------------|
| 100 | $14.24 | $4.97 | $9.27 | $278.07 |
| 1,000 | $142.36 | $49.66 | $92.69 | $2,780.73 |
| 5,000 | $711.78 | $248.33 | $463.46 | $13,903.65 |
| 10,000 | $1,423.56 | $496.65 | $926.91 | $27,807.30 |
| 50,000 | $7,117.80 | $2,483.25 | $4,634.55 | $139,036.50 |

### Break-Even

| Monthly Cost | Break-Even (req/day) |
|--------------|---------------------|
| $10 | 4 |
| $100 | 35 |
| $1,000 | 340 |
| $10,000 | 3,400 |

---

<br>

## API Reference

### Compression

```python
from core.compression.engines import (
    compress,              # Auto-select best engine
    compress_headroom,     # Headroom ML engine
    compress_claw,         # Claw 14-stage engine
    compress_super,        # SuperCompress query-aware
    count_tokens,          # Count tokens in text
)

# compress(text, engine="auto"|"headroom"|"claw"|"super", content_type="json"|"log"|"code"|"text", query="")
# Returns: CompressResult(compressed_text, tokens_before, tokens_after, savings_pct, engine)

# count_tokens(text) -> int
```

### Agents

```python
from core.agents.orchestrator import (
    Router,                # Routes queries to best agent
    Orchestrator,          # Plan-dispatch-collect-synthesize
    ParallelExecutor,      # Fan-out map-reduce
    DataAnalystAgent,      # Data analysis specialist
    CompressionExpertAgent,# Compression specialist
    InsightSynthesizerAgent,# Insight synthesis specialist
)

# Router(agents).route(query) -> agent
# Orchestrator(agents).run(query) -> {routed_to, status, tokens, ...}
# ParallelExecutor(agents).run([q1, q2, ...]) -> [result1, result2, ...]
```

### Netflix

```python
from core.netflix.analysis import (
    NetflixCatalog,        # Catalog search and filter
    NetflixAnalystAgent,   # Full analysis agent
    NetflixRecommendationEngine,  # Content recommendations
)

# NetflixCatalog().search(query) -> list
# NetflixCatalog().filter_by(country=, year=, genre=) -> list
# NetflixAnalystAgent().run_full_analysis() -> {stats, insights, ...}
# NetflixRecommendationEngine().recommend(title_id, n) -> list
```

### Causal

```python
from core.causal.inference import ActorCriticCausalAgent

# ActorCriticCausalAgent().run({data, treatment, outcome}) -> {ate, critique, ...}
```

### MCP

```python
from core.mcp.server import (
    compress_text,
    compress_json_payload,
    compress_server_logs,
    compress_query_aware,
    compare_engines,
    analyze_netflix,
    get_stats,
)
```

---

<br>

## License

[MIT License](LICENSE)

---

<br>

<div align="center">

<b>AgentForge reduces token usage by 50-99%.</b>
<br>
Same data. Same accuracy. Fraction of the cost.

<br>

```bash
pip install agentforge-platform
```

```python
from core.compression.engines import compress
result = compress(your_data, engine="auto")
```

<br>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a1a,50:0f3460,100:1a1a3e&height=120&section=footer" alt="footer"/>

</div>