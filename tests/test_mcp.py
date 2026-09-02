"""
Unit tests for MCP server tools.
Run with: pytest tests/test_mcp.py -v
"""

import pytest
import json
from core.mcp.server import (
    compress_text,
    compress_json_payload,
    compress_server_logs,
    compress_query_aware,
    compare_engines,
    get_stats,
)


class TestMCPTools:
    def test_compress_text_auto(self):
        text = "This is a test message " * 100
        result = compress_text(text, engine="auto")
        assert "engine" in result
        assert "original_tokens" in result
        assert "compressed_tokens" in result
        assert "savings_pct" in result
        assert "compressed_text" in result

    def test_compress_text_explicit_engines(self):
        text = "test content"
        for engine in ["headroom", "claw", "super"]:
            result = compress_text(text, engine=engine)
            assert "engine" in result

    def test_compress_json_payload(self):
        data = [{"id": i, "value": "x" * 50} for i in range(20)]
        json_text = json.dumps(data)
        result = compress_json_payload(json_text, engine="auto")
        assert "engine" in result
        assert result["original_tokens"] > 0

    def test_compress_server_logs(self):
        logs = "\n".join([f"2024-01-01 10:00:{i:02d} ERROR Connection failed" for i in range(30)])
        result = compress_server_logs(logs, engine="auto")
        assert "engine" in result
        assert result["savings_pct"] > 0

    def test_compress_query_aware(self):
        text = "\n".join([
            "Error: database connection failed",
            "Info: retrying in 5 seconds",
            "Debug: pool size is 10",
            "Error: timeout after 30s",
        ])
        result = compress_query_aware(text, query="error")
        assert "engine" in result
        assert "error" in result["compressed_text"].lower()

    def test_compare_engines(self):
        text = json.dumps([{"id": i, "data": "x" * 100} for i in range(30)])
        result = compare_engines(text, query="error")
        assert "original_tokens" in result
        assert "headroom" in result or "claw_compactor" in result

    def test_get_stats(self):
        result = get_stats()
        data = json.loads(result)
        assert "engines" in data
        assert "supported_content" in data
        assert "headroom" in data["engines"]
        assert "claw_compactor" in data["engines"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])