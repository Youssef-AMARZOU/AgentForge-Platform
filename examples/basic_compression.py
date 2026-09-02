#!/usr/bin/env python
"""
Example: Basic Compression Usage
Run with: python examples/basic_compression.py
"""

import json
from core.compression.engines import compress, compress_headroom, compress_claw, compress_super, count_tokens


def main():
    # Sample JSON data (simulating API response)
    json_data = {
        "users": [
            {"id": i, "name": f"User {i}", "email": f"user{i}@example.com", "status": "active"}
            for i in range(100)
        ],
        "meta": {"total": 100, "page": 1, "page_size": 100}
    }
    json_text = json.dumps(json_data)

    print("=" * 60)
    print("BASIC COMPRESSION EXAMPLE")
    print("=" * 60)

    # 1. Auto engine selection
    print("\n1. AUTO ENGINE SELECTION")
    print("-" * 40)
    result = compress(json_text, engine="auto")
    print(f"Engine:     {result.engine}")
    print(f"Original:   {result.original_tokens:,} tokens")
    print(f"Compressed: {result.compressed_tokens:,} tokens")
    print(f"Savings:    {result.savings_pct}%")
    print(f"Preview:    {result.compressed_text[:200]}...")

    # 2. Explicit Headroom (best for JSON)
    print("\n2. HEADROOM ENGINE (JSON specialist)")
    print("-" * 40)
    result = compress_headroom(json_text)
    if result:
        print(f"Original:   {result.original_tokens:,} tokens")
        print(f"Compressed: {result.compressed_tokens:,} tokens")
        print(f"Savings:    {result.savings_pct}%")

    # 3. Claw Compactor (best for logs/tabular)
    print("\n3. CLAW COMPACTOR (Log/JSON specialist)")
    print("-" * 40)
    result = compress_claw(json_text, content_type="json")
    print(f"Engine:     {result.engine}")
    print(f"Original:   {result.original_tokens:,} tokens")
    print(f"Compressed: {result.compressed_tokens:,} tokens")
    print(f"Savings:    {result.savings_pct}%")

    # 4. Server logs example
    print("\n4. SERVER LOGS COMPRESSION")
    print("-" * 40)
    logs = "\n".join([
        f"2024-01-15 10:{i//60:02d}:{i%60:02d} ERROR Database connection failed"
        for i in range(500)
    ])
    result = compress(logs, engine="auto", content_type="log")
    print(f"Engine:     {result.engine}")
    print(f"Original:   {result.original_tokens:,} tokens")
    print(f"Compressed: {result.compressed_tokens:,} tokens")
    print(f"Savings:    {result.savings_pct}%")

    # 5. Query-aware compression
    print("\n5. QUERY-AWARE COMPRESSION (SuperCompress)")
    print("-" * 40)
    context = "\n".join([
        "Error: Connection timeout at 10:00:00",
        "Info: Retrying connection...",
        "Debug: Buffer size 1024",
        "Error: Authentication failed",
        "Warning: High latency detected",
        "Info: Request completed successfully",
    ])
    result = compress_super(context, query="error")
    print(f"Query:      'error'")
    print(f"Original:   {result.original_tokens:,} tokens")
    print(f"Compressed: {result.compressed_tokens:,} tokens")
    print(f"Savings:    {result.savings_pct}%")
    print(f"Kept lines: {result.metadata['lines_kept']}/{result.metadata['lines_total']}")
    print(f"Result:\n{result.compressed_text}")


if __name__ == "__main__":
    main()