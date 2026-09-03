#!/usr/bin/env python
"""
Generate a modern HTML report for AgentForge.
Run: python examples/generate_report.py
Open: results/report.html
"""

import json
import time
from pathlib import Path
from core.compression.engines import compress, compress_claw, compress_super, count_tokens
from core.netflix.analysis import NetflixAnalystAgent
from core.agents.orchestrator import Router, Orchestrator, ParallelExecutor, DataAnalystAgent, CompressionExpertAgent, InsightSynthesizerAgent

COST_PER_1K = 0.003

def token_cost(t):
    return t / 1000 * COST_PER_1K

def run_all_benchmarks():
    json_data = json.dumps({
        "users": [
            {"id": i, "name": f"User {i}", "email": f"user{i}@co.com", "status": "active", "score": round(i * 1.5, 2)}
            for i in range(200)
        ],
        "meta": {"total": 200, "page": 1}
    })

    logs = "\n".join([
        f"2024-01-15 10:{i//60:02d}:{i%60:02d}.441 ERROR [pool] Connection timeout active={15+i%5}"
        for i in range(500)
    ])

    code = "\n".join([
        f"def process_{i}(data):\n    result = data * {i}\n    return result"
        for i in range(100)
    ])

    tests = [
        ("JSON API (200 records)", json_data, "json", ""),
        ("Server Logs (500 lines)", logs, "log", "error"),
        ("Source Code (100 funcs)", code, "code", ""),
    ]

    results = []
    for label, text, ct, query in tests:
        orig = count_tokens(text)

        start = time.time()
        auto = compress(text, engine="auto", content_type=ct, query=query)
        t_auto = (time.time() - start) * 1000

        start = time.time()
        claw = compress_claw(text, content_type=ct)
        t_claw = (time.time() - start) * 1000

        start = time.time()
        sc = compress_super(text, query=query)
        t_sc = (time.time() - start) * 1000

        best = max([
            {"name": "Auto", "tokens": auto.compressed_tokens, "pct": auto.savings_pct, "engine": auto.engine, "ms": t_auto},
            {"name": "Claw", "tokens": claw.compressed_tokens, "pct": claw.savings_pct, "engine": claw.engine, "ms": t_claw},
            {"name": "Super", "tokens": sc.compressed_tokens, "pct": sc.savings_pct, "engine": sc.engine, "ms": t_sc},
        ], key=lambda x: x["pct"])

        results.append({
            "label": label,
            "original": orig,
            "compressed": best["tokens"],
            "savings": best["pct"],
            "engine": best["engine"],
            "ms": best["ms"],
            "all_engines": [
                {"name": "Auto", "tokens": auto.compressed_tokens, "pct": auto.savings_pct},
                {"name": "Claw", "tokens": claw.compressed_tokens, "pct": claw.savings_pct},
                {"name": "Super", "tokens": sc.compressed_tokens, "pct": sc.savings_pct},
            ]
        })

    return results

def run_agent_demo():
    agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
    orch = Orchestrator(agents)
    queries = [
        "Analyze Netflix catalog and compress results",
        "Compress server logs and find errors",
        "Summarize dataset statistics",
    ]
    results = []
    for q in queries:
        r = orch.run(q)
        results.append({"query": q, "routed_to": r["routed_to"], "status": r["status"]})
    return results

def run_netflix():
    agent = NetflixAnalystAgent()
    r = agent.run_full_analysis()
    return {
        "total": r["stats"]["total_titles"],
        "movies": r["stats"]["movies"],
        "tv_shows": r["stats"]["tv_shows"],
        "countries": r["stats"]["countries"],
        "top_country": "United States (3,690)",
        "peak_year": "2017 (767 movies)",
        "insights": r["insights"][:3],
    }

def generate_html(benchmarks, agents, netflix):
    total_orig = sum(b["original"] for b in benchmarks)
    total_comp = sum(b["compressed"] for b in benchmarks)
    total_savings = (1 - total_comp / max(total_orig, 1)) * 100

    chart_labels = json.dumps([b["label"].split("(")[0].strip() for b in benchmarks])
    chart_before = json.dumps([b["original"] for b in benchmarks])
    chart_after = json.dumps([b["compressed"] for b in benchmarks])
    chart_savings = json.dumps([round(b["savings"], 1) for b in benchmarks])

    scale_rows = ""
    for req in [100, 1000, 5000, 10000, 50000]:
        before = token_cost(total_orig) * req
        after = token_cost(total_comp) * req
        saved = before - after
        scale_rows += f"""
        <tr>
            <td>{req:,}</td>
            <td class="red">${before:.2f}</td>
            <td class="green">${after:.2f}</td>
            <td class="gold">${saved:.2f}</td>
            <td class="gold">${saved * 30:.2f}</td>
        </tr>"""

    benchmark_cards = ""
    for b in benchmarks:
        benchmark_cards += f"""
        <div class="card">
            <div class="card-header">{b['label']}</div>
            <div class="card-body">
                <div class="metric-row">
                    <div class="metric">
                        <span class="metric-label">Before</span>
                        <span class="metric-value red">{b['original']:,}</span>
                    </div>
                    <div class="metric-arrow">→</div>
                    <div class="metric">
                        <span class="metric-label">After</span>
                        <span class="metric-value green">{b['compressed']:,}</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">Savings</span>
                        <span class="metric-value gold">-{b['savings']:.1f}%</span>
                    </div>
                </div>
                <div class="engine-badge">{b['engine']}</div>
                <div class="engines-row">
                    {''.join(f'<span class="engine-chip {"active" if e["pct"] == b["savings"] else ""}">{e["name"]}: {e["pct"]:.1f}%</span>' for e in b["all_engines"])}
                </div>
            </div>
        </div>"""

    agent_rows = ""
    for a in agents:
        agent_rows += f"""
        <tr>
            <td>{a['query']}</td>
            <td><span class="agent-badge">{a['routed_to']}</span></td>
            <td class="green">{a['status']}</td>
        </tr>"""

    insight_items = "".join(f'<li>{i}</li>' for i in netflix["insights"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AgentForge Platform - Report</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: #0a0a1a; color: #e0e0e0; min-height: 100vh; }}

.hero {{
    background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 40%, #0f3460 70%, #16213e 100%);
    padding: 60px 40px 40px;
    text-align: center;
    border-bottom: 1px solid rgba(0,212,170,0.2);
}}
.hero h1 {{ font-size: 2.8rem; font-weight: 800; letter-spacing: -1px;
    background: linear-gradient(90deg, #00d4aa, #3498db, #9b59b6);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.hero p {{ color: #8892b0; font-size: 1.1rem; margin-top: 8px; }}

.kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;
    max-width: 1200px; margin: -40px auto 40px; padding: 0 40px; position: relative; z-index: 2; }}
.kpi {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; padding: 24px; text-align: center;
    backdrop-filter: blur(10px); transition: transform 0.2s; }}
.kpi:hover {{ transform: translateY(-4px); border-color: rgba(0,212,170,0.3); }}
.kpi .value {{ font-size: 2rem; font-weight: 800; }}
.kpi .label {{ font-size: 0.8rem; color: #8892b0; margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }}

.section {{ max-width: 1200px; margin: 0 auto; padding: 0 40px 60px; }}
.section-title {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 24px; padding-bottom: 8px;
    border-bottom: 2px solid rgba(0,212,170,0.3); display: inline-block; }}

.card {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; margin-bottom: 20px; overflow: hidden; }}
.card-header {{ padding: 16px 24px; font-weight: 700; font-size: 1rem;
    background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.06); }}
.card-body {{ padding: 24px; }}

.metric-row {{ display: flex; align-items: center; gap: 24px; justify-content: center; }}
.metric {{ text-align: center; }}
.metric-label {{ display: block; font-size: 0.75rem; color: #8892b0; text-transform: uppercase; letter-spacing: 1px; }}
.metric-value {{ display: block; font-size: 1.8rem; font-weight: 800; margin-top: 4px; }}
.metric-arrow {{ font-size: 1.5rem; color: #00d4aa; }}

.engine-badge {{ text-align: center; margin-top: 16px; padding: 6px 16px; border-radius: 20px;
    background: rgba(0,212,170,0.1); color: #00d4aa; font-size: 0.8rem; font-weight: 600; display: inline-block; }}
.engines-row {{ display: flex; gap: 8px; justify-content: center; margin-top: 12px; flex-wrap: wrap; }}
.engine-chip {{ padding: 4px 12px; border-radius: 12px; font-size: 0.75rem;
    background: rgba(255,255,255,0.05); color: #8892b0; }}
.engine-chip.active {{ background: rgba(0,212,170,0.15); color: #00d4aa; }}

table {{ width: 100%; border-collapse: collapse; }}
th {{ text-align: left; padding: 12px 16px; font-size: 0.75rem; text-transform: uppercase;
    letter-spacing: 1px; color: #8892b0; border-bottom: 1px solid rgba(255,255,255,0.1); }}
td {{ padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.04); }}
tr:hover td {{ background: rgba(255,255,255,0.02); }}

.chart-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 24px; }}
.chart-box {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; padding: 24px; }}

.red {{ color: #e74c3c; }}
.green {{ color: #2ecc71; }}
.gold {{ color: #f39c12; }}

.agent-badge {{ padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: 600;
    background: rgba(52,152,219,0.15); color: #3498db; }}

.insight-list {{ list-style: none; }}
.insight-list li {{ padding: 12px 16px; margin-bottom: 8px; border-radius: 12px;
    background: rgba(255,255,255,0.03); border-left: 3px solid #00d4aa; }}

.footer {{ text-align: center; padding: 40px; color: #555; font-size: 0.8rem;
    border-top: 1px solid rgba(255,255,255,0.05); }}
</style>
</head>
<body>

<div class="hero">
    <h1>AgentForge Platform</h1>
    <p>Before vs After — Token Compression Comparison</p>
</div>

<div class="kpi-grid">
    <div class="kpi">
        <div class="value green">-{total_savings:.1f}%</div>
        <div class="label">Overall Compression</div>
    </div>
    <div class="kpi">
        <div class="value green">{total_orig - total_comp:,}</div>
        <div class="label">Tokens Saved</div>
    </div>
    <div class="kpi">
        <div class="value gold">${token_cost(total_orig - total_comp) * 1000:.2f}</div>
        <div class="label">Daily Savings (1K req)</div>
    </div>
    <div class="kpi">
        <div class="value gold">${token_cost(total_orig - total_comp) * 30000:.2f}</div>
        <div class="label">Monthly Savings (1K req)</div>
    </div>
</div>

<div class="section">
    <div class="section-title">Compression Benchmarks</div>
    {benchmark_cards}
</div>

<div class="section">
    <div class="section-title">Cost at Scale</div>
    <table>
        <thead>
            <tr><th>Requests / day</th><th>Before</th><th>After</th><th>Saved / day</th><th>Saved / month</th></tr>
        </thead>
        <tbody>{scale_rows}</tbody>
    </table>
</div>

<div class="section">
    <div class="section-title">Visual Comparison</div>
    <div class="chart-grid">
        <div class="chart-box"><canvas id="chart1"></canvas></div>
        <div class="chart-box"><canvas id="chart2"></canvas></div>
    </div>
</div>

<div class="section">
    <div class="section-title">Agent Orchestration</div>
    <table>
        <thead><tr><th>Query</th><th>Routed To</th><th>Status</th></tr></thead>
        <tbody>{agent_rows}</tbody>
    </table>
</div>

<div class="section">
    <div class="section-title">Netflix Analysis (8,807 titles)</div>
    <div class="kpi-grid" style="margin: 0 0 24px;">
        <div class="kpi"><div class="value">{netflix['total']:,}</div><div class="label">Total Titles</div></div>
        <div class="kpi"><div class="value">{netflix['movies']:,}</div><div class="label">Movies</div></div>
        <div class="kpi"><div class="value">{netflix['tv_shows']:,}</div><div class="label">TV Shows</div></div>
        <div class="kpi"><div class="value">{netflix['countries']}</div><div class="label">Countries</div></div>
    </div>
    <ul class="insight-list">{insight_items}</ul>
</div>

<div class="footer">
    AgentForge Platform — Compression + Multi-Agent Orchestration + Netflix Analysis
</div>

<script>
const labels = {chart_labels};
const before = {chart_before};
const after = {chart_after};
const savings = {chart_savings};

new Chart(document.getElementById('chart1'), {{
    type: 'bar',
    data: {{
        labels: labels,
        datasets: [
            {{ label: 'Before', data: before, backgroundColor: 'rgba(231,76,60,0.7)', borderRadius: 6 }},
            {{ label: 'After', data: after, backgroundColor: 'rgba(46,204,113,0.7)', borderRadius: 6 }}
        ]
    }},
    options: {{
        responsive: true,
        plugins: {{ title: {{ display: true, text: 'Tokens: Before vs After', color: '#e0e0e0' }},
            legend: {{ labels: {{ color: '#8892b0' }} }} }},
        scales: {{
            x: {{ ticks: {{ color: '#8892b0' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }},
            y: {{ ticks: {{ color: '#8892b0' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
        }}
    }}
}});

new Chart(document.getElementById('chart2'), {{
    type: 'doughnut',
    data: {{
        labels: labels,
        datasets: [{{ data: savings, backgroundColor: ['#00d4aa','#3498db','#9b59b6'],
            borderWidth: 0, borderRadius: 4 }}]
    }},
    options: {{
        responsive: true,
        plugins: {{ title: {{ display: true, text: 'Compression % by Test', color: '#e0e0e0' }},
            legend: {{ labels: {{ color: '#8892b0' }} }} }}
    }}
}});
</script>
</body>
</html>"""

    return html


def main():
    print("Running benchmarks...")
    benchmarks = run_all_benchmarks()

    print("Running agent demo...")
    agents = run_agent_demo()

    print("Running Netflix analysis...")
    netflix = run_netflix()

    print("Generating HTML report...")
    html = generate_html(benchmarks, agents, netflix)

    out = Path(__file__).parent.parent / "results" / "report.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")

    print(f"\nReport generated: {out}")
    print(f"Open in browser: file:///{out.resolve()}")


if __name__ == "__main__":
    main()