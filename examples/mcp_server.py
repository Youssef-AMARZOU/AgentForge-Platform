#!/usr/bin/env python
"""
Example: MCP Server Usage
Run with: python examples/mcp_server.py
"""

import json
from core.mcp.server import (
    compress_text,
    compress_json_payload,
    compress_server_logs,
    compress_query_aware,
    compare_engines,
    get_stats,
)


def main():
    print("=" * 60)
    print("MCP SERVER TOOLS EXAMPLE")
    print("=" * 60)

    # 1. Get server stats
    print("\n1. SERVER STATS (Resource)")
    print("-" * 40)
    stats = get_stats()
    print(stats)

    # 2. Compress text
    print("\n2. COMPRESS_TEXT (Tool)")
    print("-" * 40)
    text = "This is a sample text that will be compressed. " * 50
    result = compress_text(text, engine="auto")
    print(f"Engine:     {result['engine']}")
    print(f"Original:   {result['original_tokens']:,} tokens")
    print(f"Compressed: {result['compressed_tokens']:,} tokens")
    print(f"Savings:    {result['savings_pct']}%")

    # 3. Compress JSON payload
    print("\n3. COMPRESS_JSON_PAYLOAD (Tool)")
    print("-" * 40)
    api_response = {
        "data": [
            {"id": i, "name": f"Item {i}", "description": "x" * 100, "tags": ["tag1", "tag2"]}
            for i in range(100)
        ],
        "pagination": {"page": 1, "size": 100, "total": 10000}
    }
    json_text = json.dumps(api_response)
    result = compress_json_payload(json_text, engine="auto")
    print(f"Engine:     {result['engine']}")
    print(f"Original:   {result['original_tokens']:,} tokens")
    print(f"Compressed: {result['compressed_tokens']:,} tokens")
    print(f"Savings:    {result['savings_pct']}%")

    # 4. Compress server logs
    print("\n4. COMPRESS_SERVER_LOGS (Tool)")
    print("-" * 40)
    logs = "\n".join([
        f"2024-01-15 10:{i//60:02d}:{i%60:02d} ERROR [connection-pool] Failed to acquire connection"
        for i in range(200)
    ])
    result = compress_server_logs(logs, engine="auto")
    print(f"Engine:     {result['engine']}")
    print(f"Original:   {result['original_tokens']:,} tokens")
    print(f"Compressed: {result['compressed_tokens']:,} tokens")
    print(f"Savings:    {result['savings_pct']}%")
    print(f"Preview:    {result['compressed_text'][:200]}...")

    # 5. Query-aware compression
    print("\n5. COMPRESS_QUERY_AWARE (Tool)")
    print("-" * 40)
    context = "\n".join([
        "ERROR: Database connection timeout after 30s",
        "INFO: Attempting reconnect...",
        "DEBUG: Pool size: 10, Active: 8",
        "ERROR: Authentication failed for user admin",
        "WARN: High memory usage detected: 85%",
        "INFO: Request processed in 245ms",
    ])
    result = compress_query_aware(context, query="error", engine="super")
    print(f"Query:      'error'")
    print(f"Engine:     {result['engine']}")
    print(f"Original:   {result['original_tokens']:,} tokens")
    print(f"Compressed: {result['compressed_tokens']:,} tokens")
    print(f"Savings:    {result['savings_pct']}%")
    print(f"Result:\n{result['compressed_text']}")

    # 6. Compare all engines
    print("\n6. COMPARE_ENGINES (Tool)")
    print("-" * 40)
    text = json.dumps([{"id": i, "value": "x" * 200} for i in range(50)])
    results = compare_engines(text, query="error")
    print(f"Original: {results['original_tokens']:,} tokens")
    for engine, data in results.items():
        if engine != "original_tokens":
            print(f"  {engine}: {data['tokens']:,} tokens ({data['savings_pct']}% savings)")


if __name__ == "__main__":
    main()