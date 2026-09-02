"""
MCP Server using FastMCP
Exposes compression tools via Model Context Protocol.
"""

from fastmcp import FastMCP
import json
from .engines import compress, compress_headroom, compress_claw, compress_super, count_tokens

mcp = FastMCP(
    name="AgentForge Compression Server",
    description="Token compression tools for AI agents -- Headroom, Claw Compactor, SuperCompress",
)


@mcp.tool()
def compress_text(text: str, engine: str = "auto", query: str = "", content_type: str = "auto") -> dict:
    """Compress text using the unified compression layer.

    Args:
        text: The text to compress
        engine: One of 'auto', 'headroom', 'claw', 'super'
        query: Optional query for query-aware compression (SuperCompress style)
        content_type: One of 'auto', 'json', 'log', 'code', 'text'
    """
    result = compress(text, engine=engine, query=query, content_type=content_type)
    return {
        "engine": result.engine,
        "original_tokens": result.original_tokens,
        "compressed_tokens": result.compressed_tokens,
        "savings_pct": result.savings_pct,
        "compressed_text": result.compressed_text,
        "metadata": result.metadata,
    }


@mcp.tool()
def compress_json_payload(json_text: str, engine: str = "auto") -> dict:
    """Compress a JSON payload (API responses, database outputs, etc.).

    Args:
        json_text: JSON string to compress
        engine: Compression engine to use
    """
    return compress(json_text, engine=engine, content_type="json").__dict__


@mcp.tool()
def compress_server_logs(log_text: str, engine: str = "auto") -> dict:
    """Compress server logs by deduplicating and collapsing repeated patterns.

    Args:
        log_text: Log text to compress
        engine: Compression engine to use
    """
    return compress(log_text, engine=engine, content_type="log").__dict__


@mcp.tool()
def compress_query_aware(text: str, query: str, engine: str = "super") -> dict:
    """Compress context relative to a specific query -- keeps answer-critical lines.

    Args:
        text: The context to compress
        query: The query to compress against
        engine: Compression engine (default: super for query-aware)
    """
    return compress(text, engine=engine, query=query).__dict__


@mcp.tool()
def compare_engines(text: str, query: str = "") -> dict:
    """Run all compression engines and compare results side by side.

    Args:
        text: Text to compress with all engines
        query: Optional query for query-aware comparison
    """
    results = {}
    hr = compress_headroom(text)
    if hr:
        results["headroom"] = {
            "tokens": hr.compressed_tokens,
            "savings_pct": hr.savings_pct,
        }
    claw = compress_claw(text)
    results["claw_compactor"] = {
        "tokens": claw.compressed_tokens,
        "savings_pct": claw.savings_pct,
    }
    if query:
        sc = compress_super(text, query)
        results["supercompress"] = {
            "tokens": sc.compressed_tokens,
            "savings_pct": sc.savings_pct,
        }
    results["original_tokens"] = count_tokens(text)
    return results


@mcp.resource("compression://stats")
def get_stats() -> str:
    """Get information about available compression engines."""
    return json.dumps({
        "engines": {
            "headroom": "Netflix's Headroom -- SmartCrusher, ML model, reversible CCR",
            "claw_compactor": "14-stage pipeline -- JSON tabularization, log crunching, AST collapse",
            "supercompress": "Query-aware extractive -- keeps answer-critical lines",
        },
        "supported_content": ["json", "log", "code", "text", "diff", "search_results"],
    }, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
