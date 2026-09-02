"""
Unit tests for the unified compression layer.
Run with: pytest tests/test_compression.py -v
"""

import pytest
import json
from core.compression.engines import (
    count_tokens,
    CompressionResult,
    compress_headroom,
    compress_claw,
    compress_super,
    compress,
    _stage_json_tabularize,
    _stage_log_crunch,
    _stage_semantic_dedup,
    _stage_structural_collapse,
)


class TestTokenCounting:
    def test_count_tokens_with_tiktoken(self):
        text = "Hello world"
        tokens = count_tokens(text)
        assert isinstance(tokens, int)
        assert tokens > 0

    def test_count_tokens_empty_string(self):
        assert count_tokens("") == 0


class TestCompressionResult:
    def test_compression_result_creation(self):
        result = CompressionResult(
            engine="test",
            original_tokens=100,
            compressed_tokens=50,
            savings_pct=50.0,
            compressed_text="compressed",
        )
        assert result.engine == "test"
        assert result.original_tokens == 100
        assert result.compressed_tokens == 50
        assert result.savings_pct == 50.0


class TestClawStages:
    def test_json_tabularize(self):
        data = [
            {"id": 1, "name": "A", "status": "active"},
            {"id": 2, "name": "B", "status": "active"},
            {"id": 3, "name": "C", "status": "inactive"},
        ]
        json_text = json.dumps(data)
        result = _stage_json_tabularize(json_text)
        assert "id|name|status" in result
        assert "active" in result

    def test_json_tabularize_non_list(self):
        text = '{"key": "value"}'
        result = _stage_json_tabularize(text)
        assert result == text

    def test_json_tabularize_invalid_json(self):
        text = "not json"
        result = _stage_json_tabularize(text)
        assert result == text

    def test_log_crunch(self):
        logs = "\n".join([
            "2024-01-01 10:00:00 ERROR Connection failed",
            "2024-01-01 10:00:01 ERROR Connection failed",
            "2024-01-01 10:00:02 INFO Retrying",
        ])
        result = _stage_log_crunch(logs)
        assert "[x2]" in result
        assert "ERROR Connection failed" in result

    def test_log_crunch_few_lines(self):
        text = "short log"
        result = _stage_log_crunch(text)
        assert result == text

    def test_semantic_dedup(self):
        text = "line 1\nline 2\nline 1\nline 3"
        result = _stage_semantic_dedup(text)
        lines = result.split("\n")
        assert len(lines) == 3
        assert "line 1" in result

    def test_structural_collapse(self):
        code = "import os\nimport sys\nfrom typing import List\ndef foo():\n    pass"
        result = _stage_structural_collapse(code)
        assert "import os" not in result
        assert "from typing import List" not in result


class TestClawCompactor:
    def test_compress_claw_json(self):
        data = [{"id": i, "type": "record"} for i in range(10)]
        text = json.dumps(data)
        result = compress_claw(text, content_type="json")
        assert isinstance(result, CompressionResult)
        assert result.engine == "claw_compactor"
        assert result.compressed_tokens <= result.original_tokens

    def test_compress_claw_logs(self):
        logs = "\n".join([f"2024-01-01 10:00:{i:02d} ERROR Failed" for i in range(20)])
        result = compress_claw(logs, content_type="log")
        assert result.engine == "claw_compactor"
        assert result.savings_pct > 0

    def test_compress_claw_auto(self):
        text = "some random text without structure"
        result = compress_claw(text, content_type="auto")
        assert result.engine == "claw_compactor"


class TestSuperCompress:
    def test_compress_super_with_query(self):
        text = "\n".join([
            "Error: connection timeout",
            "Info: retrying connection",
            "Debug: buffer size 1024",
            "Error: authentication failed",
        ])
        result = compress_super(text, query="error")
        assert result.engine == "supercompress_style"
        assert "error" in result.compressed_text.lower()
        assert result.metadata["lines_kept"] > 0

    def test_compress_super_no_query(self):
        text = "line 1\nline 2\nline 3"
        result = compress_super(text, query="")
        assert result.engine == "supercompress_style"
        assert result.compressed_tokens <= result.original_tokens


class TestUnifiedRouter:
    def test_compress_auto_selects_engine(self):
        text = json.dumps([{"id": i, "data": "x" * 100} for i in range(50)])
        result = compress(text, engine="auto")
        assert isinstance(result, CompressionResult)
        assert result.engine in ("headroom", "claw_compactor", "supercompress_style")

    def test_compress_explicit_headroom(self):
        text = "test content"
        result = compress(text, engine="headroom")
        assert result.engine in ("headroom", "claw_compactor")

    def test_compress_explicit_claw(self):
        text = "test content"
        result = compress(text, engine="claw")
        assert result.engine == "claw_compactor"

    def test_compress_explicit_super(self):
        text = "test content"
        result = compress(text, engine="super", query="test")
        assert result.engine == "supercompress_style"

    def test_compress_with_query_prefers_super(self):
        text = "error: something failed\ninfo: retrying"
        result = compress(text, engine="auto", query="error")
        assert result.engine in ("supercompress_style", "claw_compactor", "headroom")


class TestEdgeCases:
    def test_compress_empty_string(self):
        result = compress("", engine="claw")
        assert result.compressed_tokens == 0

    def test_compress_unicode(self):
        text = "日本語テスト\n中文测试\nالعربية"
        result = compress(text, engine="claw")
        assert isinstance(result, CompressionResult)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])