"""
AgentForge Platform -- Main Entry Point

Usage:
    python main.py                    # Run everything
    python main.py benchmark          # Compression benchmark
    python main.py mcp                # Start MCP server
    python main.py dashboard          # Launch Streamlit dashboard
    python main.py analyze            # Netflix analysis
"""

import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()


def main():
    console.print(Panel.fit(
        "[bold magenta]AgentForge Platform[/bold magenta]\n"
        "[dim]Compression + Multi-Agent Orchestration + Netflix Analysis[/dim]\n\n"
        "[bold]Powered by:[/bold] Headroom, FastMCP, mcp-agent, MetaGPT, Netflix OCI, Claw Compactor, SuperCompress",
        border_style="magenta",
    ))

    mode = sys.argv[1] if len(sys.argv) > 1 else "all"

    if mode in ("all", "benchmark"):
        console.print("\n[bold cyan]PHASE 1: Compression Benchmark[/bold cyan]")
        from benchmark import run_benchmark
        run_benchmark()

    if mode in ("all", "analyze"):
        console.print("\n[bold cyan]PHASE 2: Netflix Analysis[/bold cyan]")
        from core.netflix.analysis import NetflixAnalystAgent
        agent = NetflixAnalystAgent()
        result = agent.run_full_analysis()
        console.print(f"  Titles: {result['stats']['total_titles']}")
        console.print(f"  Movies: {result['stats']['movies']}")
        console.print(f"  TV Shows: {result['stats']['tv_shows']}")
        for insight in result["insights"]:
            console.print(f"  [green]{insight}[/green]")

    if mode == "mcp":
        console.print("\n[bold cyan]Starting MCP Server...[/bold cyan]")
        from core.mcp.server import mcp
        mcp.run(transport="stdio")

    if mode == "dashboard":
        console.print("\n[bold cyan]Launching Dashboard...[/bold cyan]")
        import subprocess
        subprocess.run(["streamlit", "run", str(Path(__file__).parent / "dashboard" / "app.py")])

    console.print(Panel.fit(
        "[bold green]Done![/bold green]\n\n"
        "Built on: Headroom, FastMCP, mcp-agent, MetaGPT, Netflix OCI, Claw Compactor, SuperCompress",
        border_style="green",
    ))


if __name__ == "__main__":
    main()
