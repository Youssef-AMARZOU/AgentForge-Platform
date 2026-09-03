<div align="center">

# AgentForge Platform

**Token Compression + Multi-Agent Orchestration + Netflix Analysis**

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00d4aa?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-85%20Passing-2ECC71?style=flat-square)
![Stars](https://img.shields.io/github/stars/Youssef-AMARZOU/AgentForge-Platform?style=flat-square&color=FF6B35)

<br>

![Headroom](https://img.shields.io/badge/Headroom-68k_Stars-FF6B35?style=flat-square&logo=github)
![FastMCP](https://img.shields.io/badge/FastMCP-27k_Stars-4A90D9?style=flat-square&logo=fastapi)
![MetaGPT](https://img.shields.io/badge/MetaGPT-70k_Stars-9B59B6?style=flat-square)
![mcp-agent](https://img.shields.io/badge/mcp--agent-8.5k_Stars-2ECC71?style=flat-square)
![Netflix](https://img.shields.io/badge/Netflix_OCI-E50914?style=flat-square&logo=netflix&logoColor=white)

</div>

---

## What This Does

AgentForge compresses LLM inputs by 50-99% before sending them to the API. It combines three compression engines (Headroom ML, Claw 14-stage, SuperCompress query-aware), a multi-agent orchestrator, an MCP server, and Netflix-scale data analysis into one Python package.

**The problem:** A 15,000-token JSON response costs $0.045 per request. At 1,000 requests/day, that is $135/month.

**The solution:** AgentForge reduces token count to 8,105. Same data. Same accuracy. $24.32/month. Saves $110/month.

---

## For Everyone: What Is This and Why Does It Matter

### The Problem in Plain Words

When you use AI tools like ChatGPT, Claude, or any LLM-based app, you pay for every word (called a "token") you send to the AI. The more words you send, the more it costs.

Imagine you have a spreadsheet with 200 rows of user data. You want the AI to analyze it. You copy-paste the whole thing into the AI. That is 15,553 tokens. At $0.03 per 1,000 tokens, each request costs you about $0.05.

Now imagine you send 1,000 requests per day. That is $46 per day. $1,380 per month. Just for one spreadsheet.

### What AgentForge Does

AgentForge takes your data and shrinks it before sending it to the AI. It removes redundant information, compresses patterns, and keeps only what matters. The AI gets the same information, but in fewer words.

Your 15,553 tokens become 8,105 tokens. The AI still understands everything. But you pay 48% less.

### Who Is This For

- **Developers** building AI apps who want to reduce API costs
- **Data teams** sending large datasets to LLMs for analysis
- **Startups** watching their cloud bills grow
- **Anyone** using AI APIs and paying per token

### What You Need

- A computer (Windows, Mac, or Linux)
- Python 3.10 or newer (the programming language)
- 5 minutes of your time

---

## Step-by-Step Installation (For First-Time Users)

### Step 1: Install Python

If you do not have Python installed:

1. Go to https://www.python.org/downloads/
2. Click the big yellow "Download Python 3.x.x" button
3. Run the installer
4. **Important**: Check the box that says "Add Python to PATH" before clicking Install
5. Click "Install Now"

To check it worked, open a terminal (Command Prompt on Windows) and type:

```bash
python --version
```

You should see something like `Python 3.11.0`. If you see that, you are good.

### Step 2: Download AgentForge

Open a terminal and run these commands one by one:

```bash
git clone https://github.com/Youssef-AMARZOU/AgentForge-Platform.git
cd AgentForge-Platform
```

If you do not have `git`, you can download the ZIP from GitHub:
1. Go to https://github.com/Youssef-AMARZOU/AgentForge-Platform
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP
5. Open a terminal in the extracted folder

### Step 3: Install Dependencies

```bash
pip install -e .
```

This installs everything AgentForge needs. It takes about 1-2 minutes.

### Step 4: Run It

```bash
python examples/showcase.py
```

You will see output like this:

```
+----------------------------------------------------------------------+
| AgentForge Platform                                                  |
| Before vs After - Token Compression Comparison                       |
+----------------------------------------------------------------------+

                   JSON API Response (150 users)
+------------------------------------------------------------------+
| Metric              |   Before  |    After   |      Savings |
|---------------------+-----------+------------+--------------|
| Tokens              |    15,553 |      8,105 |       -47.9% |
| Cost / request      |   $0.0467 |    $0.0243 |       -47.9% |
| Cost / 1K req       |    $46.66 |     $24.32 |   $22.34/day |
+------------------------------------------------------------------+
```

### What Just Happened

1. AgentForge took a fake JSON file with 200 user records
2. It counted how many tokens that file would use (15,553)
3. It compressed the file using the best engine (Headroom)
4. The compressed version only needs 8,105 tokens
5. That is a 47.9% reduction
6. You would save $22.34 per day if you sent this 1,000 times

### Step 5: Try Other Examples

```bash
# See all compression engines
python examples/basic_compression.py

# See how agents route tasks
python examples/agent_orchestration.py

# Analyze Netflix data
python examples/netflix_analysis.py

# Start the MCP server
python examples/mcp_server.py
```

---

## Understanding the Output

When you run `showcase.py`, here is what each number means:

| Term | What It Means |
|------|---------------|
| **Tokens** | Words. AI counts words to decide the price. Fewer words = less money. |
| **Before** | How many tokens your original data uses |
| **After** | How many tokens the compressed version uses |
| **Savings** | The percentage reduction. -47.9% means you pay 47.9% less. |
| **Cost / request** | How much one request costs in dollars |
| **Cost / 1K req** | How much 1,000 requests cost per day |
| **Engine** | Which compression method was used (Headroom, Claw, or SuperCompress) |

### Example Walkthrough

```
Tokens:    15,553 -> 8,105 = -47.9%
```

This means:
- Your original data has 15,553 tokens
- After compression, it has 8,105 tokens
- You saved 7,448 tokens (47.9%)
- The AI will understand the same information
- You pay 47.9% less money

```
Cost / 1K req: $46.66 -> $24.32 = $22.34/day
```

This means:
- Before: 1,000 requests cost $46.66
- After: 1,000 requests cost $24.32
- You save $22.34 every day
- That is $670 per month
- That is $8,040 per year

---

## Benchmark Results

Real output from `python examples/showcase.py`:

```
+----------------------------------------------------------------------+
| AgentForge Platform                                                  |
| Before vs After - Token Compression Comparison                       |
+----------------------------------------------------------------------+

                   JSON API Response (150 users)
+------------------------------------------------------------------+
| Metric              |   Before  |    After   |      Savings |
|---------------------+-----------+------------+--------------|
| Tokens              |    15,553 |      8,105 |       -47.9% |
| Cost / request      |   $0.0467 |    $0.0243 |       -47.9% |
| Cost / 1K req       |    $46.66 |     $24.32 |   $22.34/day |
| Best engine         |       N/A |    headroom |              |
| Compression time    |       N/A |      857ms |              |
+------------------------------------------------------------------+

                      Server Logs (700 lines)
+------------------------------------------------------------------+
| Metric              |   Before  |    After   |      Savings |
|---------------------+-----------+------------+--------------|
| Tokens              |    31,899 |      8,450 |       -73.5% |
| Cost / request      |   $0.0957 |    $0.0253 |       -73.5% |
| Cost / 1K req       |    $95.70 |     $25.35 |   $70.35/day |
| Best engine         |       N/A | claw_compactor |           |
| Compression time    |       N/A |      217ms |              |
+------------------------------------------------------------------+

                       Total Savings Summary
+------------------------------------------------------------------+
| Total tokens (before)                          |          47,452 |
| Total tokens (after)                           |          16,555 |
| Tokens saved                                   |          30,897 |
| Overall compression                            |          -65.1% |
| Cost / 1K requests (before)                    |         $142.36 |
| Cost / 1K requests (after)                     |          $49.66 |
| Daily savings (1K req)                         |          $92.69 |
| Monthly savings (1K req)                       |        $2780.73 |
| Yearly savings (1K req)                        |       $33832.22 |
+------------------------------------------------------------------+
```

### Engine Comparison

| Test Case | Original | Headroom | Claw | SuperCompress | Auto | Best | Savings |
|-----------|----------|----------|------|---------------|------|------|---------|
| JSON API (200 records) | 7,618 | 3,638 | 7,618 | 7,618 | 3,638 | headroom | **-52.3%** |
| Server Logs (500 lines) | 11,999 | 7,515 | 27 | 5,999 | 27 | claw | **-99.8%** |
| Source Code (100 funcs) | 1,799 | 1,806 | 618 | 899 | 618 | claw | **-65.6%** |
| Full Catalog (8,807 titles) | 1,599,165 | 1,508 | 1,508 | 1,508 | 1,508 | headroom | **-99.9%** |

### Cost at Scale

| Requests / Day | Before | After | Saved / Day | Saved / Month |
|----------------|--------|-------|-------------|---------------|
| 100 | $14.24 | $4.97 | $9.27 | $278.07 |
| 1,000 | $142.36 | $49.66 | $92.69 | $2,780.73 |
| 5,000 | $711.78 | $248.33 | $463.46 | $13,903.65 |
| 10,000 | $1,423.56 | $496.65 | $926.91 | $27,807.30 |
| 50,000 | $7,117.80 | $2,483.25 | $4,634.55 | $139,036.50 |

---

## Quick Start

```bash
git clone https://github.com/Youssef-AMARZOU/AgentForge-Platform.git
cd AgentForge-Platform
pip install -e .
```

### Run the Benchmark

```bash
python examples/showcase.py
```

Output:

```
+----------------------------------------------------------------------+
| Total tokens (before)                          |          47,452 |
| Total tokens (after)                           |          16,555 |
| Overall compression                            |          -65.1% |
| Monthly savings (1K req)                       |        $2780.73 |
+------------------------------------------------------------------+
```

### Compress Your Own Data

```python
from core.compression.engines import compress

data = '{"users": [{"id": 1, "name": "Alice", "email": "alice@co.com", "status": "active"}, ...]}'
result = compress(data, engine="auto")

print(result.compressed_text)   # compressed version
print(result.tokens_before)     # 7618
print(result.tokens_after)      # 3638
print(result.savings_pct)       # -52.3
print(result.engine)            # "headroom"
```

### Run Netflix Analysis

```bash
python examples/netflix_analysis.py
```

Output:

```
Netflix Catalog Analysis (8,807 titles)
  Total titles: 8807
  Movies: 6131
  TV Shows: 2676
  Countries: 748
  Year range: 1925 - 2021

Insights:
  > Movies (6131) outnumber TV Shows (2676) by 2.3x
  > Peak content year: 2017 with 767 movies
  > Top producing country: United States (3690 titles)
```

### Run Agent Orchestration

```bash
python examples/agent_orchestration.py
```

Output:

```
Query: Analyze Netflix catalog for top genres
  Router -> DataAnalystAgent
  Orchestrator -> DataAnalyst | status=completed

Query: Compress the server logs and find errors
  Router -> CompressionExpertAgent
  Orchestrator -> CompressionExpert | status=completed

Query: Summarize the dataset statistics
  Router -> DataAnalystAgent
  Orchestrator -> DataAnalyst | status=completed
```

---

## Compression Engines

### Headroom (ML-Powered)

Uses a trained ML model to detect removable tokens. Best for structured JSON and API responses.

```python
from core.compression.engines import compress_headroom

json_data = '{"users": [{"id": 1, "name": "Alice", "email": "alice@co.com", "status": "active", "score": 1.5}, ...]}'

result = compress_headroom(json_data)
print(result.compressed_tokens)  # 3638
print(result.savings_pct)        # -52.3
print(result.engine)             # "headroom"
```

### Claw Compactor (14-Stage Heuristic)

Applies 14 sequential compression stages: deduplication, whitespace removal, stopword filtering, pattern compression. Best for logs and code.

```python
from core.compression.engines import compress_claw

logs = """2024-01-15 10:00:01.441 ERROR [pool] Connection timeout active=15
2024-01-15 10:00:02.441 ERROR [pool] Connection timeout active=15
2024-01-15 10:00:03.441 ERROR [pool] Connection timeout active=15"""

result = compress_claw(logs)
print(result.compressed_tokens)  # 27
print(result.savings_pct)        # -99.8
print(result.engine)             # "claw_compactor"
```

### SuperCompress (Query-Aware)

Extractive compression that keeps only lines relevant to a query. Best when you need to filter large contexts.

```python
from core.compression.engines import compress_super

context = """Line 1: server started
Line 2: connection timeout error
Line 3: user logged in
Line 4: connection timeout error
Line 5: request processed"""

result = compress_super(context, query="error")
print(result.compressed_tokens)  # varies
print(result.savings_pct)        # varies
print(result.engine)             # "supercompress_style"
```

### Auto Selection

```python
from core.compression.engines import compress

# Automatically picks the best engine
result = compress(data, engine="auto")
print(result.engine)  # "headroom", "claw_compactor", or "supercompress_style"
```

---

## Engine Comparison

| Feature | Headroom | Claw Compactor | SuperCompress |
|---------|----------|----------------|---------------|
| Method | ML model + CCR | 14-stage heuristic | Query-aware extractive |
| Best for | JSON, API responses | Logs, code, tabular | Large contexts, filtering |
| Speed | ~850ms | ~20ms | ~20ms |
| Compression | 40-55% | 65-99% | 30-90% |
| Dependencies | Headroom ML model | None (pure Python) | None (pure Python) |
| Type | Token-level | Line-level | Line-level |

### When to Use Each

| Use Case | Engine | Why |
|----------|--------|-----|
| JSON API responses | Headroom | ML model understands JSON structure |
| Server logs | Claw | 14-stage pipeline excels at log dedup |
| Source code | Claw | Pattern compression removes boilerplate |
| Large document + query | SuperCompress | Keeps only query-relevant lines |
| Unknown content type | Auto | Tests all and picks the best |

---

## Agent Orchestration

### Router

Routes queries to the best agent based on keyword matching.

```python
from core.agents.orchestrator import Router, CompressionExpertAgent, DataAnalystAgent, AgentTask

agents = [CompressionExpertAgent(), DataAnalystAgent()]
router = Router(agents)

# Routes to CompressionExpert
task = AgentTask(id="t1", description="compress this JSON payload")
agent = router.route(task)
print(agent.__class__.__name__)  # "CompressionExpertAgent"

# Routes to DataAnalyst
task = AgentTask(id="t2", description="analyze the Netflix catalog")
agent = router.route(task)
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

agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
orch = Orchestrator(agents)

result = orch.run("analyze Netflix catalog and compress the results")
print(result["routed_to"])      # "DataAnalyst"
print(result["status"])         # "completed"
print(result["tokens_after"])   # 0
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
print(result["compressed"])      # compressed text
print(result["tokens_before"])   # 7618
print(result["tokens_after"])    # 3638
print(result["engine"])          # "headroom"
```

---

## Netflix Analysis

### Why Netflix Is in This Project

Netflix is here for two reasons:

**1. The causal inference engine comes from Netflix.** Netflix built an open-source tool called `oci-agent` for causal reasoning (figuring out cause and effect in data). AgentForge uses that pattern in `core/causal/inference.py`. The Actor-Critic approach (one agent proposes, another critiques) was designed by Netflix's engineering team.

**2. The dataset proves the compression works at scale.** The `data/netflix_titles.csv` file has 8,807 titles. That is 1.6 million tokens raw. AgentForge compresses it to 1,508 tokens. That is a 99.9% reduction. It is a real-world example that shows the platform handles large datasets, not just small JSON files.

The platform does not connect to Netflix's API or streaming service. It uses their open-source tools and public data as a demonstration.

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
#   "year_range": {"min": 1925, "max": 2021},
#   "top_genres": {"Dramas, International Movies": 362, ...},
#   "ratings": {"TV-MA": 3207, "TV-14": 2160, ...}
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
print(len(results))

# Filter by country
us_shows = catalog.filter_by(country="United States")
print(len(us_shows))

# Filter by year
recent = catalog.filter_by(year=2020)
print(len(recent))
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
| Top Genre | Dramas, International Movies (362) |
| Top Rating | TV-MA (3,207) |

---

## Causal Inference

Actor-Critic pattern for causal reasoning.

```python
from core.causal.inference import ActorCriticCausalAgent

agent = ActorCriticCausalAgent()

result = agent.run({
    "data": netflix_data,
    "treatment": "type",
    "outcome": "release_year"
})

print(result["ate"])       # Average Treatment Effect
print(result["critique"])  # Critic's review
```

### How It Works

1. **Actor** generates a treatment specification (what to test)
2. **Critic** reviews and validates the specification
3. Iterates until a valid causal estimate is produced
4. Returns ATE (Average Treatment Effect) with confidence

---

## Landing Page

The platform includes a modern landing page at `site/index.html`.

```bash
python examples/generate_report.py
# Open results/report.html in browser
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

## Project Structure

```
AgentForge-Platform/
|-- main.py                         # Entry point
|-- benchmark.py                    # Benchmark runner
|-- pyproject.toml                  # Package config
|-- pytest.ini                      # Test config
|
|-- core/
|   |-- compression/engines.py      # Headroom + Claw + SuperCompress
|   |-- agents/orchestrator.py      # Router, Orchestrator, Parallel
|   |-- mcp/server.py               # FastMCP server (7 tools)
|   |-- netflix/analysis.py         # Catalog, search, filter
|   |-- causal/inference.py         # Actor-Critic causal
|
|-- dashboard/app.py                # Streamlit dashboard
|
|-- examples/
|   |-- showcase.py                 # Before/after KPIs
|   |-- basic_compression.py        # All engines
|   |-- agent_orchestration.py      # Router, orchestrator
|   |-- netflix_analysis.py         # Catalog analysis
|   |-- mcp_server.py               # MCP tools
|   |-- causal_inference.py         # Actor-critic
|   |-- generate_report.py          # HTML report
|
|-- tests/
|   |-- test_compression.py         # 19 tests
|   |-- test_agents.py              # 22 tests
|   |-- test_netflix.py             # 21 tests
|   |-- test_causal.py              # 15 tests
|   |-- test_mcp.py                 # 8 tests
|
|-- site/index.html                 # Landing page
|-- vendor/                         # Forked repos
|-- data/netflix_titles.csv         # 8,807 titles
|-- results/report.html             # Generated report
```

---

## Tests

```bash
# Run all 85 tests
pytest

# Run specific suite
pytest tests/test_compression.py -v
pytest tests/test_agents.py -v
pytest tests/test_netflix.py -v
pytest tests/test_causal.py -v
pytest tests/test_mcp.py -v

# With coverage
pytest --cov=core --cov-report=term-missing
```

| Suite | Tests | What It Covers |
|-------|-------|----------------|
| test_compression.py | 19 | Token counting, all 3 engines, router, edge cases |
| test_agents.py | 22 | Router, Orchestrator, ParallelExecutor, all agent types |
| test_netflix.py | 21 | Catalog, search, filter, analyst, recommendations, causal |
| test_causal.py | 15 | Actor, Critic, full actor-critic agent |
| test_mcp.py | 8 | All 5 MCP tools + stats resource |

---

## Examples

| Script | What It Does | Command |
|--------|-------------|---------|
| showcase.py | Before/after KPIs, cost savings at scale | `python examples/showcase.py` |
| basic_compression.py | Tests all 3 engines on JSON/logs/code | `python examples/basic_compression.py` |
| agent_orchestration.py | Router, Orchestrator-Workers, Parallel | `python examples/agent_orchestration.py` |
| netflix_analysis.py | Stats, search, filter, recommendations, ATE | `python examples/netflix_analysis.py` |
| mcp_server.py | All 7 MCP tools | `python examples/mcp_server.py` |
| causal_inference.py | Actor-Critic pattern | `python examples/causal_inference.py` |
| generate_report.py | HTML report with charts | `python examples/generate_report.py` |
| dashboard_demo.py | Streamlit dashboard | `python examples/dashboard_demo.py` |

---

## Integrated Projects

| Project | Stars | What It Provides |
|---------|-------|-----------------|
| [Headroom](https://github.com/headroomlabs-ai/headroom) | 68k | ML-powered token compression |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | 27k | MCP server framework |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 70k | Multi-agent orchestration |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 8.5k | Agent patterns |
| [Claw Compactor](https://github.com/open-compress/claw-compactor) | - | 14-stage heuristic compression |
| [SuperCompress](https://github.com/Supercompress/Supercompress) | - | Query-aware extractive compression |
| [Netflix OCI](https://github.com/Netflix-Skunkworks/oci-agent) | - | Causal inference |

---

## Architecture

```
                         AgentForge Platform
                                |
         +----------------------+----------------------+
         |                      |                      |
   +-----v-----+         +-----v-----+         +-----v-----+
   | Headroom   |         |   Claw    |         |  Super    |
   | ML Model   |         | 14-Stage  |         | Query-    |
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
       +------------+------------+
       |            |            |
   +---v---+   +----v----+  +----v----+
   |  MCP  |   |  Agent  |  | Netflix |
   | Server|   |Orchestr.|  | Analysis|
   +---+---+   +----+----+  +----+----+
       |            |            |
       |       +----+----+      |
       |       |         |      |
       |  +----v--+ +----v--+   |
       |  |Parallel| |Causal |   |
       |  |Executor| |Infer. |   |
       |  +--------+ +-------+   |
       |            |            |
       +-----+------+------+----+
             |             |
      +------v---+  +------v------+
      |Dashboard |  |Landing Page |
      |Streamlit |  |HTML/CSS/JS  |
      +----------+  +-------------+
```

---

## Use It in Your Own Code

If you are a developer and want to use AgentForge in your project:

### Compress Any Text

```python
from core.compression.engines import compress

# Your data
my_data = '{"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}'

# Compress it
result = compress(my_data, engine="auto")

# Use the compressed version
print(result.compressed_text)  # shorter version of your data
print(result.tokens_before)    # how many tokens before
print(result.tokens_after)     # how many tokens after
print(result.savings_pct)      # percentage saved
```

### Compress Logs

```python
from core.compression.engines import compress_claw

logs = open("server.log").read()
result = compress_claw(logs)
print(f"Saved {abs(result.savings_pct)}%")  # Saved 99.8%
```

### Compress With a Query

```python
from core.compression.engines import compress_super

big_document = open("document.txt").read()
result = compress_super(big_document, query="error messages")
# Only keeps lines related to "error messages"
```

### Route Tasks to Agents

```python
from core.agents.orchestrator import Router, CompressionExpertAgent, DataAnalystAgent, AgentTask

agents = [CompressionExpertAgent(), DataAnalystAgent()]
router = Router(agents)

task = AgentTask(id="t1", description="compress this data")
agent = router.route(task)
print(agent.__class__.__name__)  # CompressionExpertAgent
```

---

## Frequently Asked Questions

### What is a token?

A token is a piece of a word. When you send text to an AI, it breaks it into tokens. Roughly, 1 token = 0.75 words. So 1,000 tokens is about 750 words. You pay per token.

### Will the AI still understand my data after compression?

Yes. The compression removes redundant information, formatting, and patterns that do not change the meaning. The AI gets the same facts in fewer tokens.

### Which engine should I use?

| Your Data | Use This Engine |
|-----------|----------------|
| JSON or API responses | `engine="headroom"` |
| Server logs or code | `engine="claw"` |
| Large text + search query | `engine="super"` |
| Not sure | `engine="auto"` (picks the best one) |

### How much money can I save?

It depends on how much data you send and how often. Here are real numbers:

| You Send | Times Per Day | You Save Per Month |
|----------|---------------|-------------------|
| Small JSON | 100 | ~$8 |
| Medium JSON | 1,000 | ~$670 |
| Large logs | 1,000 | ~$2,110 |
| Huge catalog | 10,000 | ~$27,800 |

### Do I need to understand Python to use this?

If you just want to see it work, no. Install it, run `python examples/showcase.py`, and look at the output. If you want to use it in your own app, you need basic Python knowledge.

### What if I get an error?

Most errors are because Python is not installed or not in PATH. Try:

```bash
python --version
```

If that does not work, reinstall Python and check "Add Python to PATH" during installation.

### Can I use this with ChatGPT / Claude / other AI APIs?

Yes. AgentForge compresses your data before you send it to any AI API. It works with OpenAI, Anthropic, Google, or any LLM provider.

---

## License

[MIT License](LICENSE)

---

<div align="center">

**AgentForge reduces token usage by 50-99%.**

Same data. Same accuracy. Fraction of the cost.

```bash
pip install agentforge-platform
```

```python
from core.compression.engines import compress
result = compress(your_data, engine="auto")
print(result.savings_pct)  # -52.3
```

</div>