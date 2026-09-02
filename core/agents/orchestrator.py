"""
Agent Orchestration Layer
Inspired by mcp-agent patterns: router, orchestrator-workers, parallel map-reduce.
"""

import json
import time
from dataclasses import dataclass, field
from typing import Any, Callable
from ..compression.engines import compress, count_tokens


@dataclass
class AgentTask:
    id: str
    description: str
    status: str = "pending"
    result: Any = None
    error: str | None = None
    tokens_before: int = 0
    tokens_after: int = 0
    duration_ms: float = 0


@dataclass
class AgentSpec:
    name: str
    role: str
    tools: list[str] = field(default_factory=list)
    compress_output: bool = True


class BaseAgent:
    def __init__(self, spec: AgentSpec):
        self.spec = spec
        self.history: list[AgentTask] = []

    def execute(self, task: AgentTask) -> AgentTask:
        raise NotImplementedError


class DataAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentSpec(
            name="DataAnalyst",
            role="Analyzes datasets, computes statistics, finds patterns",
            tools=["search", "filter", "stats", "aggregate"],
        ))

    def execute(self, task: AgentTask) -> AgentTask:
        task.status = "running"
        start = time.time()
        try:
            result = self._analyze(task.description)
            task.result = result
            task.status = "completed"
        except Exception as e:
            task.error = str(e)
            task.status = "failed"
        task.duration_ms = (time.time() - start) * 1000
        self.history.append(task)
        return task

    def _analyze(self, description: str) -> dict:
        return {
            "agent": self.spec.name,
            "analysis": f"Analyzed: {description}",
            "insights": ["Pattern detected", "Anomaly found", "Trend identified"],
        }


class CompressionExpertAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentSpec(
            name="CompressionExpert",
            role="Selects and applies the best compression engine for each data type",
            tools=["compress", "compare", "route"],
        ))

    def execute(self, task: AgentTask) -> AgentTask:
        task.status = "running"
        start = time.time()
        try:
            text = task.description
            result = compress(text, engine="auto")
            task.result = {
                "engine": result.engine,
                "original_tokens": result.original_tokens,
                "compressed_tokens": result.compressed_tokens,
                "savings_pct": result.savings_pct,
            }
            task.tokens_before = result.original_tokens
            task.tokens_after = result.compressed_tokens
            task.status = "completed"
        except Exception as e:
            task.error = str(e)
            task.status = "failed"
        task.duration_ms = (time.time() - start) * 1000
        self.history.append(task)
        return task


class InsightSynthesizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentSpec(
            name="InsightSynthesizer",
            role="Combines outputs from other agents into coherent summaries",
            tools=["synthesize", "summarize", "report"],
        ))

    def execute(self, task: AgentTask) -> AgentTask:
        task.status = "running"
        start = time.time()
        try:
            task.result = self._synthesize(task.description)
            task.status = "completed"
        except Exception as e:
            task.error = str(e)
            task.status = "failed"
        task.duration_ms = (time.time() - start) * 1000
        self.history.append(task)
        return task

    def _synthesize(self, description: str) -> dict:
        return {
            "agent": self.spec.name,
            "summary": f"Synthesized insights from: {description}",
            "recommendations": ["Optimize X", "Monitor Y", "Scale Z"],
        }


# --- Orchestrator Patterns ---

class Router:
    """Routes tasks to the best agent based on content analysis."""

    def __init__(self, agents: list[BaseAgent]):
        self.agents = {a.spec.name: a for a in agents}

    def route(self, task: AgentTask) -> BaseAgent:
        desc = task.description.lower()
        if any(w in desc for w in ["compress", "token", "reduce", "optimize"]):
            return self.agents.get("CompressionExpert", list(self.agents.values())[0])
        if any(w in desc for w in ["analyze", "stat", "pattern", "trend", "data"]):
            return self.agents.get("DataAnalyst", list(self.agents.values())[0])
        if any(w in desc for w in ["summary", "combine", "synthesize", "report"]):
            return self.agents.get("InsightSynthesizer", list(self.agents.values())[0])
        return list(self.agents.values())[0]


class Orchestrator:
    """Orchestrator-workers pattern: plan -> dispatch -> collect -> synthesize."""

    def __init__(self, agents: list[BaseAgent]):
        self.router = Router(agents)
        self.agents = agents

    def run(self, query: str) -> dict:
        start = time.time()
        task = AgentTask(id="orch-001", description=query)
        agent = self.router.route(task)
        result = agent.execute(task)

        synthesize_agent = self.agents[-1] if self.agents else None
        if synthesize_agent and synthesize_agent.spec.name == "InsightSynthesizer":
            synth_task = AgentTask(
                id="orch-002",
                description=f"Query: {query} | Agent: {result.status} | Result: {json.dumps(result.result) if result.result else result.error}",
            )
            synthesize_agent.execute(synth_task)

        return {
            "query": query,
            "routed_to": agent.spec.name,
            "status": result.status,
            "result": result.result,
            "error": result.error,
            "tokens_before": result.tokens_before,
            "tokens_after": result.tokens_after,
            "duration_ms": (time.time() - start) * 1000,
        }


class ParallelExecutor:
    """Map-reduce pattern: fan out to multiple agents, aggregate results."""

    def __init__(self, agents: list[BaseAgent]):
        self.agents = agents

    def run(self, queries: list[str]) -> list[dict]:
        results = []
        for query in queries:
            agent = self.agents[0] if self.agents else None
            if agent:
                task = AgentTask(id=f"par-{len(results):03d}", description=query)
                result = agent.execute(task)
                results.append({
                    "query": query,
                    "agent": agent.spec.name,
                    "status": result.status,
                    "result": result.result,
                })
        return results
