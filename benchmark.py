"""
Benchmark Runner
Compares all compression engines on real data and saves results.
"""

import json
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.compression.engines import compress, compress_headroom, compress_claw, compress_super, count_tokens
from core.netflix.analysis import NetflixCatalog
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def run_benchmark(csv_path: str = None):
    console.print(Panel.fit(
        "[bold cyan]AgentForge Compression Benchmark[/bold cyan]\n"
        "[dim]Headroom + Claw Compactor + SuperCompress on Netflix data[/dim]",
        border_style="cyan",
    ))

    catalog = NetflixCatalog(csv_path)
    results = []

    # Test 1: JSON API Response
    console.print("\n[bold]Test 1: JSON API Response (200 titles)[/bold]")
    import pandas as pd
    import json as _json
    chunk = catalog.df.head(200).to_dict(orient="records")
    blob = {"status": "success", "metadata": {"request_id": "req_001", "api_version": "v2.1.3"}, "data": chunk}
    text = _json.dumps(blob, indent=2)
    orig = count_tokens(text)

    r_auto = compress(text, engine="auto")
    r_claw = compress_claw(text)
    r_hr = compress_headroom(text)

    console.print(f"  Original: {orig:,} tokens")
    for name, r in [("Auto", r_auto), ("Claw", r_claw), ("Headroom", r_hr)]:
        if r:
            console.print(f"  {name}: {r.compressed_tokens:,} tokens ([green]-{r.savings_pct}%[/green])")

    results.append({
        "test": "JSON API Response",
        "original_tokens": orig,
        "auto": r_auto.compressed_tokens if r_auto else None,
        "claw": r_claw.compressed_tokens if r_claw else None,
        "headroom": r_hr.compressed_tokens if r_hr else None,
    })

    # Test 2: Server Logs
    console.print("\n[bold]Test 2: Server Logs (200 lines)[/bold]")
    import random
    logs = []
    for i in range(200):
        level = random.choice(["INFO", "DEBUG", "WARN", "ERROR"])
        logs.append(f"[2026-09-02T19:{i%60:02d}:{i*3%60:02d}] {level} NetflixAPI - Request {i} status=200 latency={random.randint(5,2000)}ms")
    log_text = "\n".join(logs)
    orig = count_tokens(log_text)

    r_auto = compress(log_text, engine="auto")
    r_claw = compress_claw(log_text)
    r_sc = compress_super(log_text, query="error failures")

    console.print(f"  Original: {orig:,} tokens")
    for name, r in [("Auto", r_auto), ("Claw", r_claw), ("SuperCompress", r_sc)]:
        if r:
            console.print(f"  {name}: {r.compressed_tokens:,} tokens ([green]-{r.savings_pct}%[/green])")

    results.append({
        "test": "Server Logs",
        "original_tokens": orig,
        "auto": r_auto.compressed_tokens if r_auto else None,
        "claw": r_claw.compressed_tokens if r_claw else None,
        "super": r_sc.compressed_tokens if r_sc else None,
    })

    # Test 3: Full Catalog
    console.print("\n[bold]Test 3: Full Netflix Catalog JSON[/bold]")
    full = catalog.df.to_dict(orient="records")
    text = _json.dumps(full, indent=2)
    orig = count_tokens(text)

    r_auto = compress(text, engine="auto")
    r_claw = compress_claw(text)
    r_hr = compress_headroom(text)

    console.print(f"  Original: {orig:,} tokens")
    for name, r in [("Auto", r_auto), ("Claw", r_claw), ("Headroom", r_hr)]:
        if r:
            console.print(f"  {name}: {r.compressed_tokens:,} tokens ([green]-{r.savings_pct}%[/green])")

    results.append({
        "test": "Full Catalog JSON",
        "original_tokens": orig,
        "auto": r_auto.compressed_tokens if r_auto else None,
        "claw": r_claw.compressed_tokens if r_claw else None,
        "headroom": r_hr.compressed_tokens if r_hr else None,
    })

    # Summary
    table = Table(title="Benchmark Results", box=box.ROUNDED, border_style="cyan")
    table.add_column("Test", style="bold")
    table.add_column("Original", justify="right")
    table.add_column("Auto", justify="right", style="green")
    table.add_column("Claw", justify="right", style="green")
    table.add_column("Headroom", justify="right", style="green")

    for r in results:
        table.add_row(
            r["test"],
            f"{r['original_tokens']:,}",
            f"-{(1-r['auto']/r['original_tokens'])*100:.0f}%" if r["auto"] else "N/A",
            f"-{(1-r['claw']/r['original_tokens'])*100:.0f}%" if r["claw"] else "N/A",
            f"-{(1-r['headroom']/r['original_tokens'])*100:.0f}%" if r.get("headroom") else "N/A",
        )
    console.print(table)

    results_path = Path(__file__).parent / "results" / "benchmark_results.json"
    results_path.parent.mkdir(exist_ok=True)
    with open(results_path, "w") as f:
        json.dump({"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "tests": results}, f, indent=2)
    console.print(f"\n[dim]Results saved to {results_path}[/dim]")

    return results


if __name__ == "__main__":
    csv_path = str(Path(__file__).parent / "data" / "netflix_titles.csv")
    run_benchmark(csv_path)
