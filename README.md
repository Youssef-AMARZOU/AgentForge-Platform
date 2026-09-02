<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B35,25:9B59B6,50:3498DB,75:2ECC71,100:E74C3C&height=200&section=header&text=AgentForge%20Platform&fontSize=48&fontColor=F8FAFC&animation=fadeIn" alt="header"/>

<div align="center">

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=FF6B35&width=500&lines=Compression+%2B+Multi-Agent+%2B+Netflix+Analysis;7+Open-Source+Projects+Merged;94.8%25+Fewer+Tokens.+Same+Accuracy.&fontColor=FF6B35&center=true&vCenter=true&duration=2000&repeat=true&width=500" alt="Typing SVG" /></a>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00FF00?style=for-the-badge)
![Headroom](https://img.shields.io/badge/Headroom-68K_Stars-FF6B35?style=for-the-badge&logo=github)
![FastMCP](https://img.shields.io/badge/FastMCP-27K_Stars-4A90D9?style=for-the-badge&logo=fastapi)
![MetaGPT](https://img.shields.io/badge/MetaGPT-70K_Stars-9B59B6?style=for-the-badge)
![Netflix](https://img.shields.io/badge/Netflix_Data-E50914?style=for-the-badge&logo=netflix&logoColor=white)

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=slice&color=0:2C3E50,50:8E44AD,100:3498DB&height=80&section=header&text=WHY+AGENTFORGE&fontSize=28&fontColor=F8FAFC&animation=slideInLeft" alt="why"/>

<div align="center">

```
Your agent reads a 10,000-token log file to find one error.
You paid for all 10,000 tokens.
The answer needed 1,200.

AgentForge compresses the context BEFORE it reaches the LLM.
Same answer. 94.8% fewer tokens. Fraction of the cost.
```

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=rounded&color=0:E74C3C,50:F39C12,100:2ECC71&height=80&section=header&text=WHAT%27S+INSIDE&fontSize=28&fontColor=F8FAFC&animation=fadeIn" alt="inside"/>

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,streamlit,docker,github&theme=dark" alt="Tech Stack" />

<br><br>

</div>

<table align="center">
<tr>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:FF6B35,100:FF6B35&height=120&width=180&text=Headroom&fontSize=14&fontColor=F8FAFC" alt="Headroom"/><br><sub>68K Stars</sub><br><sub>Token Compression</sub></td>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:3498DB,100:3498DB&height=120&width=180&text=FastMCP&fontSize=14&fontColor=F8FAFC" alt="FastMCP"/><br><sub>27K Stars</sub><br><sub>MCP Server</sub></td>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:9B59B6,100:9B59B6&height=120&width=180&text=mcp-agent&fontSize=14&fontColor=F8FAFC" alt="mcp-agent"/><br><sub>8.5K Stars</sub><br><sub>Agent Patterns</sub></td>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:2ECC71,100:2ECC71&height=120&width=180&text=MetaGPT&fontSize=14&fontColor=F8FAFC" alt="MetaGPT"/><br><sub>70K Stars</sub><br><sub>Multi-Agent</sub></td>
</tr>
<tr>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:E74C3C,100:E74C3C&height=120&width=180&text=Claw+Compactor&fontSize=14&fontColor=F8FAFC" alt="Claw"/><br><sub>14-Stage</sub><br><sub>Compression Pipeline</sub></td>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:F39C12,100:F39C12&height=120&width=180&text=SuperCompress&fontSize=14&fontColor=F8FAFC" alt="SuperCompress"/><br><sub>Query-Aware</sub><br><sub>Extractive</sub></td>
<td align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:1ABC9C,100:1ABC9C&height=120&width=180&text=Netflix+OCI&fontSize=14&fontColor=F8FAFC" alt="Netflix OCI"/><br><sub>Causal</sub><br><sub>Inference</sub></td>
</tr>
</table>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=cylinder&color=0:1ABC9C,50:2980B9,100:8E44AD&height=80&section=header&text=ARCHITECTURE&fontSize=28&fontColor=F8FAFC&animation=slideInUp" alt="arch"/>

<div align="center">

```
                              AgentForge Platform
                                     |
          ┌──────────────────────────┼──────────────────────────┐
          │                          │                          │
    ┌─────▼─────┐             ┌─────▼─────┐             ┌─────▼─────┐
    │  Headroom │             │   Claw    │             │  Super    │
    │ SmartCrush│             │ 14-Stage  │             │ Compress  │
    └─────┬─────┘             └─────┬─────┘             └─────┬─────┘
          │                          │                          │
          └────────────┬─────────────┴─────────────┬────────────┘
                       │                            │
                ┌──────▼──────┐              ┌──────▼──────┐
                │   Unified   │              │   Content   │
                │   Router    │◄─────────────┤   Router    │
                └──────┬──────┘              └─────────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
    ┌─────▼─────┐ ┌────▼────┐ ┌────▼────┐
    │   MCP     │ │  Agent  │ │ Netflix │
    │  Server   │ │Orchestr.│ │ Analysis│
    └─────┬─────┘ └────┬────┘ └────┬────┘
          │            │            │
          └────────────┼────────────┘
                       │
                ┌──────▼──────┐
                │  Dashboard  │
                │ (Streamlit) │
                └─────────────┘
```

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:F39C12,100:E74C3C&height=80&section=header&text=BENCHMARK+RESULTS&fontSize=28&fontColor=F8FAFC&animation=fadeIn" alt="benchmark"/>

<div align="center">

<table>
<tr>
<td><img src="https://capsule-render.vercel.app/api?type=rounded&color=0:FF6B35,100:FF6B35&height=100&width=300&text=JSON+API+Response&fontSize=16&fontColor=F8FAFC" alt="JSON"/></td>
<td><img src="https://capsule-render.vercel.app/api?type=rounded&color=0:E74C3C,100:E74C3C&height=100&width=300&text=Server+Logs&fontSize=16&fontColor=F8FAFC" alt="Logs"/></td>
<td><img src="https://capsule-render.vercel.app/api?type=rounded&color=0:2ECC71,100:2ECC71&height=100&width=300&text=Full+Catalog+JSON&fontSize=16&fontColor=F8FAFC" alt="Catalog"/></td>
</tr>
</table>

</div>

<table align="center">
<tr>
<td align="center">

| Test | Original | Compressed | Savings |
|:-----|:--------:|:----------:|:-------:|
| JSON API Response | 37,245 | 23,629 | **-36.6%** |
| Server Logs | 5,905 | 2,948 | **-50.1%** |
| Full Catalog JSON | 1,599,165 | 1,508 | **-99.9%** |

</td>
<td align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:2ECC71,100:27AE60&height=150&width=300&text=-94.8%25+TOTAL&fontSize=32&fontColor=F8FAFC&animation=bounce" alt="savings"/>

</td>
</tr>
</table>

<div align="center">

| Requests/day | Tokens Saved | Cost Saved |
|:------------:|:------------:|:----------:|
| 100 | 164,805 | $0.49/day |
| 1,000 | 1,648,054 | **$4.94/day** |
| 10,000 | 16,480,540 | **$49.44/day** |
| 100,000 | 164,805,400 | **$494.42/day** |

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=soft-rect&color=0:3498DB,50:2C3E50,100:1ABC9C&height=80&section=header&text=QUICK+START&fontSize=28&fontColor=F8FAFC&animation=slideInDown" alt="quickstart"/>

```bash
# Clone
git clone https://github.com/Youssef-AMARZOU/AgentForge-Platform.git
cd AgentForge-Platform

# Install
pip install -r requirements.txt

# Run everything
python main.py

# Or individually
python main.py benchmark   # Compression benchmark
python main.py analyze     # Netflix analysis
python main.py mcp         # MCP server
python main.py dashboard   # Streamlit UI
```

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:8E44AD,50:2980B9,100:1ABC9C&height=80&section=header&text=USAGE&fontSize=28&fontColor=F8FAFC&animation=fadeIn" alt="usage"/>

### Compression Engine

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

### MCP Server

```bash
python main.py mcp
```

| Tool | Description |
|:-----|:------------|
| `compress_text` | Auto engine selection |
| `compress_json_payload` | Optimize JSON |
| `compress_server_logs` | Deduplicate logs |
| `compress_query_aware` | Query-aware compression |
| `compare_engines` | Compare all engines |

### Agent Orchestration

```python
from core.agents.orchestrator import Orchestrator, DataAnalystAgent, CompressionExpertAgent, InsightSynthesizerAgent

orch = Orchestrator([DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()])
result = orch.run("analyze Netflix catalog and compress the results")
```

### Netflix Analysis

```python
from core.netflix.analysis import NetflixAnalystAgent

agent = NetflixAnalystAgent()
result = agent.run_full_analysis()
print(result["stats"])
# {'total_titles': 8807, 'movies': 6131, 'tv_shows': 2676}
```

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:E74C3C,50:F39C12,100:2ECC71&height=80&section=header&text=NETFLIX+ANALYSIS&fontSize=28&fontColor=F8FAFC&animation=slideInLeft" alt="netflix"/>

<div align="center">

| Stat | Value |
|:-----|:-----:|
| Total Titles | 8,807 |
| Movies | 6,131 |
| TV Shows | 2,676 |
| Top Country | United States (3,690) |
| Peak Year | 2017 (767 movies) |

</div>

**Insights:**
- Movies outnumber TV Shows by 2.3x
- Peak content year: 2017 with 767 movies
- Top producing country: United States (3,690 titles)

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=cylinder&color=0:2C3E50,50:8E44AD,100:2980B9&height=80&section=header&text=PROJECT+STRUCTURE&fontSize=28&fontColor=F8FAFC&animation=fadeIn" alt="structure"/>

```
AgentForge-Platform/
|
+-- main.py                         # Entry point
+-- benchmark.py                    # Compression benchmark
+-- requirements.txt
+-- LICENSE
|
+-- core/
|   +-- compression/
|   |   +-- engines.py              # Headroom + Claw + SuperCompress
|   +-- agents/
|   |   +-- orchestrator.py         # Router, orchestrator-workers
|   +-- mcp/
|   |   +-- server.py               # FastMCP server
|   +-- netflix/
|   |   +-- analysis.py             # Netflix catalog analysis
|   +-- causal/
|       +-- inference.py            # Actor-critic causal inference
|
+-- dashboard/
|   +-- app.py                      # Streamlit dashboard
|
+-- vendor/
|   +-- headroom/                   # Tejas Chopra (Netflix)
|   +-- fastmcp/                    # PrefectHQ
|   +-- mcp-agent/                  # LastMile AI
|   +-- MetaGPT/                    # geekan
|
+-- data/
|   +-- netflix_titles.csv          # 8,800+ titles
|
+-- results/
    +-- benchmark_results.json
```

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=soft-rect&color=0:9B59B6,50:3498DB,100:1ABC9C&height=80&section=header&text=CREDITS&fontSize=28&fontColor=F8FAFC&animation=slideInUp" alt="credits"/>

<div align="center">

<a href="https://github.com/headroomlabs-ai/headroom">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:FF6B35,100:FF6B35&height=60&width=150&text=Headroom&fontSize=12&fontColor=F8FAFC" alt="Headroom"/>
</a>
<a href="https://github.com/PrefectHQ/fastmcp">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:3498DB,100:3498DB&height=60&width=150&text=FastMCP&fontSize=12&fontColor=F8FAFC" alt="FastMCP"/>
</a>
<a href="https://github.com/lastmile-ai/mcp-agent">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:9B59B6,100:9B59B6&height=60&width=150&text=mcp-agent&fontSize=12&fontColor=F8FAFC" alt="mcp-agent"/>
</a>
<a href="https://github.com/geekan/MetaGPT">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:2ECC71,100:2ECC71&height=60&width=150&text=MetaGPT&fontSize=12&fontColor=F8FAFC" alt="MetaGPT"/>
</a>
<a href="https://github.com/Netflix-Skunkworks/oci-agent">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:E74C3C,100:E74C3C&height=60&width=150&text=Netflix+OCI&fontSize=12&fontColor=F8FAFC" alt="Netflix OCI"/>
</a>
<a href="https://github.com/open-compress/claw-compactor">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:F39C12,100:F39C12&height=60&width=150&text=Claw&fontSize=12&fontColor=F8FAFC" alt="Claw"/>
</a>
<a href="https://github.com/Supercompress/Supercompress">
<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:1ABC9C,100:1ABC9C&height=60&width=150&text=SuperCompress&fontSize=12&fontColor=F8FAFC" alt="SuperCompress"/>
</a>

<br><br>

> *"The cheapest token is the one you never send."* — Tejas Chopra

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:1ABC9C,50:2ECC71,100:27AE60&height=80&section=header&text=CONTRIBUTING&fontSize=28&fontColor=F8FAFC&animation=fadeIn" alt="contributing"/>

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=rounded&color=0:2C3E50,50:3498DB,100:2ECC71&height=60&section=header&text=LICENSE&fontSize=28&fontColor=F8FAFC" alt="license"/>

MIT License — see [LICENSE](LICENSE) for details.

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B35,25:9B59B6,50:3498DB,75:2ECC71,100:E74C3C&height=150&section=footer&text=Thanks+for+visiting!&fontSize=32&fontColor=F8FAFC&animation=fadeIn" alt="footer"/>
