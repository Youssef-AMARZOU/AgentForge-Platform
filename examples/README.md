# Examples

Run examples from the project root:

```bash
cd AgentForge-Platform
python examples/basic_compression.py
python examples/agent_orchestration.py
python examples/netflix_analysis.py
python examples/mcp_server.py
python examples/causal_inference.py
python examples/dashboard_demo.py
```

## Example Scripts

| Script | Description |
|--------|-------------|
| `basic_compression.py` | Compression engines: auto, headroom, claw, super |
| `agent_orchestration.py` | Router, Orchestrator-Workers, Parallel map-reduce |
| `netflix_analysis.py` | Catalog stats, search, recommendations, causal inference |
| `mcp_server.py` | All MCP tools: compress_text, compare_engines, etc. |
| `causal_inference.py` | Actor-Critic pattern with Netflix data |
| `dashboard_demo.py` | Launch Streamlit dashboard |

## Running Tests

```bash
# All tests
pytest

# Specific test files
pytest tests/test_compression.py -v
pytest tests/test_agents.py -v
pytest tests/test_netflix.py -v
pytest tests/test_causal.py -v
pytest tests/test_mcp.py -v

# With coverage
pytest --cov=core --cov-report=term-missing
```