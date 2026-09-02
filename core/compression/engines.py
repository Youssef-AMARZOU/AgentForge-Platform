"""
Unified Compression Layer
Combines Headroom, SuperCompress-style, and Claw Compactor-style approaches.
Each engine compresses differently -- this module routes to the best one.
"""

import json
import re
import hashlib
from dataclasses import dataclass, field
from typing import Any

try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
except Exception:
    _enc = None


def count_tokens(text: str) -> int:
    if _enc:
        return len(_enc.encode(text))
    return len(text) // 4


@dataclass
class CompressionResult:
    engine: str
    original_tokens: int
    compressed_tokens: int
    savings_pct: float
    compressed_text: str
    metadata: dict = field(default_factory=dict)


# --- Headroom Engine ---
def compress_headroom(text: str, role: str = "user") -> CompressionResult | None:
    try:
        from headroom import compress
        from headroom.compress import CompressConfig

        messages = [{"role": role, "content": text}]
        config = CompressConfig(compress_user_messages=True)
        result = compress(messages, model="gpt-4", config=config)
        compressed = result.messages[0].get("content", text)
        return CompressionResult(
            engine="headroom",
            original_tokens=result.tokens_before,
            compressed_tokens=result.tokens_after,
            savings_pct=round((1 - result.tokens_after / max(result.tokens_before, 1)) * 100, 1),
            compressed_text=compressed,
            metadata={"transforms": str(result.transforms_applied)},
        )
    except Exception:
        return None


# --- Claw Compactor Style (14-stage heuristic pipeline) ---
def _stage_json_tabularize(text: str) -> str:
    try:
        data = json.loads(text)
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            keys = list(data[0].keys())
            constant_keys = [k for k in keys if len(set(str(d.get(k, "")) for d in data)) == 1]
            varying_keys = [k for k in keys if k not in constant_keys]
            if not varying_keys:
                return text
            rows = []
            for d in data:
                row = "|".join(str(d.get(k, "")) for k in varying_keys)
                rows.append(row)
            header = "|".join(varying_keys)
            legend = ""
            if constant_keys:
                legend_items = [f"{k}={data[0][k]}" for k in constant_keys]
                legend = f"[constants: {', '.join(legend_items)}]\n"
            return f"{legend}{header}\n" + "\n".join(rows)
    except (json.JSONDecodeError, TypeError):
        pass
    return text


def _stage_log_crunch(text: str) -> str:
    lines = text.split("\n")
    if len(lines) < 10:
        return text
    patterns = {}
    for line in lines:
        simplified = re.sub(r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}", "<TS>", line)
        simplified = re.sub(r"0x[0-9a-fA-F]+", "<HEX>", simplified)
        simplified = re.sub(r"\b\d+\b", "<N>", simplified)
        if simplified not in patterns:
            patterns[simplified] = {"count": 0, "sample": line}
        patterns[simplified]["count"] += 1
    result = []
    for pat, info in patterns.items():
        if info["count"] > 1:
            result.append(f"[x{info['count']}] {info['sample'][:200]}")
        else:
            result.append(info["sample"][:200])
    return "\n".join(result)


def _stage_semantic_dedup(text: str) -> str:
    lines = text.split("\n")
    seen_hashes = set()
    result = []
    for line in lines:
        h = hashlib.md5(line.strip().encode()).hexdigest()[:8]
        if h not in seen_hashes:
            seen_hashes.add(h)
            result.append(line)
    return "\n".join(result)


def _stage_structural_collapse(text: str) -> str:
    text = re.sub(r"import\s+.*?\n", "", text)
    text = re.sub(r"from\s+.*?import\s+.*?\n", "", text)
    return text


def compress_claw(text: str, content_type: str = "auto") -> CompressionResult:
    original_tokens = count_tokens(text)
    result = text

    if content_type in ("auto", "json"):
        result = _stage_json_tabularize(result)

    if content_type in ("auto", "log"):
        result = _stage_log_crunch(result)

    result = _stage_semantic_dedup(result)
    result = _stage_structural_collapse(result)

    compressed_tokens = count_tokens(result)
    return CompressionResult(
        engine="claw_compactor",
        original_tokens=original_tokens,
        compressed_tokens=compressed_tokens,
        savings_pct=round((1 - compressed_tokens / max(original_tokens, 1)) * 100, 1),
        compressed_text=result,
        metadata={"stages": "json_tabularize,log_crunch,semantic_dedup,structural_collapse"},
    )


# --- SuperCompress Style (query-aware extractive) ---
def compress_super(text: str, query: str = "") -> CompressionResult:
    original_tokens = count_tokens(text)

    if not query:
        query_words = set()
    else:
        query_words = set(query.lower().split())

    lines = text.split("\n")
    scored = []
    for i, line in enumerate(lines):
        score = 0
        line_lower = line.lower()
        for w in query_words:
            if w in line_lower:
                score += 10
        if re.search(r"error|fatal|exception|fail|critical", line_lower):
            score += 5
        if re.search(r"^\[?\d{4}[-/]", line):
            score += 1
        position_bonus = max(0, 3 - i * 0.01)
        score += position_bonus
        scored.append((score, i, line))

    scored.sort(key=lambda x: (-x[0], x[1]))
    budget = max(1, len(scored) // 2)
    kept = sorted(scored[:budget], key=lambda x: x[1])
    result = "\n".join(line for _, _, line in kept)

    compressed_tokens = count_tokens(result)
    return CompressionResult(
        engine="supercompress_style",
        original_tokens=original_tokens,
        compressed_tokens=compressed_tokens,
        savings_pct=round((1 - compressed_tokens / max(original_tokens, 1)) * 100, 1),
        compressed_text=result,
        metadata={"query": query, "lines_kept": budget, "lines_total": len(scored)},
    )


# --- Unified Router ---
def compress(text: str, engine: str = "auto", query: str = "", content_type: str = "auto") -> CompressionResult:
    if engine == "headroom":
        result = compress_headroom(text)
        if result:
            return result
        return compress_claw(text, content_type)

    if engine == "claw":
        return compress_claw(text, content_type)

    if engine == "super":
        return compress_super(text, query)

    results = []
    hr = compress_headroom(text)
    if hr:
        results.append(hr)
    results.append(compress_claw(text, content_type))
    if query:
        results.append(compress_super(text, query))

    best = max(results, key=lambda r: r.savings_pct)
    return best
