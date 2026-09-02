"""
Unit tests for the agent orchestration layer.
Run with: pytest tests/test_agents.py -v
"""

import pytest
from core.agents.orchestrator import (
    AgentTask,
    AgentSpec,
    BaseAgent,
    DataAnalystAgent,
    CompressionExpertAgent,
    InsightSynthesizerAgent,
    Router,
    Orchestrator,
    ParallelExecutor,
)


class TestAgentTask:
    def test_task_creation(self):
        task = AgentTask(id="test-001", description="Test task")
        assert task.id == "test-001"
        assert task.description == "Test task"
        assert task.status == "pending"
        assert task.result is None

    def test_task_with_fields(self):
        task = AgentTask(
            id="test-002",
            description="Test with fields",
            status="completed",
            result={"key": "value"},
            tokens_before=100,
            tokens_after=50,
        )
        assert task.status == "completed"
        assert task.result == {"key": "value"}
        assert task.tokens_before == 100


class TestAgentSpec:
    def test_spec_creation(self):
        spec = AgentSpec(name="TestAgent", role="Test role", tools=["tool1", "tool2"])
        assert spec.name == "TestAgent"
        assert spec.tools == ["tool1", "tool2"]
        assert spec.compress_output is True


class TestDataAnalystAgent:
    def test_agent_creation(self):
        agent = DataAnalystAgent()
        assert agent.spec.name == "DataAnalyst"
        assert "search" in agent.spec.tools

    def test_agent_execution(self):
        agent = DataAnalystAgent()
        task = AgentTask(id="da-001", description="Analyze sales data")
        result = agent.execute(task)

        assert result.status == "completed"
        assert result.result is not None
        assert "analysis" in result.result
        assert "insights" in result.result
        assert len(agent.history) == 1

    def test_agent_execution_error_handling(self):
        agent = DataAnalystAgent()
        # Force an error by making _analyze raise
        original_analyze = agent._analyze

        def failing_analyze(desc):
            raise ValueError("Test error")

        agent._analyze = failing_analyze
        task = AgentTask(id="da-002", description="Will fail")
        result = agent.execute(task)

        assert result.status == "failed"
        assert result.error == "Test error"
        agent._analyze = original_analyze


class TestCompressionExpertAgent:
    def test_agent_creation(self):
        agent = CompressionExpertAgent()
        assert agent.spec.name == "CompressionExpert"
        assert "compress" in agent.spec.tools

    def test_agent_execution(self):
        agent = CompressionExpertAgent()
        task = AgentTask(id="ce-001", description="Compress this JSON payload")
        result = agent.execute(task)

        assert result.status == "completed"
        assert result.result is not None
        assert "engine" in result.result
        assert "savings_pct" in result.result
        assert result.tokens_before > 0


class TestInsightSynthesizerAgent:
    def test_agent_creation(self):
        agent = InsightSynthesizerAgent()
        assert agent.spec.name == "InsightSynthesizer"
        assert "synthesize" in agent.spec.tools

    def test_agent_execution(self):
        agent = InsightSynthesizerAgent()
        task = AgentTask(id="is-001", description="Synthesize results")
        result = agent.execute(task)

        assert result.status == "completed"
        assert result.result is not None
        assert "summary" in result.result
        assert "recommendations" in result.result


class TestRouter:
    def test_router_creation(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        router = Router(agents)
        assert len(router.agents) == 3

    def test_router_routes_compression(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        router = Router(agents)
        task = AgentTask(id="r-001", description="Compress this JSON data")
        agent = router.route(task)
        assert agent.spec.name == "CompressionExpert"

    def test_router_routes_analysis(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        router = Router(agents)
        task = AgentTask(id="r-002", description="Analyze the dataset for patterns")
        agent = router.route(task)
        assert agent.spec.name == "DataAnalyst"

    def test_router_routes_synthesis(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        router = Router(agents)
        task = AgentTask(id="r-003", description="Summarize the findings")
        agent = router.route(task)
        assert agent.spec.name == "InsightSynthesizer"

    def test_router_default_fallback(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        router = Router(agents)
        task = AgentTask(id="r-004", description="Unknown task type")
        agent = router.route(task)
        assert agent is not None


class TestOrchestrator:
    def test_orchestrator_creation(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        orch = Orchestrator(agents)
        assert len(orch.agents) == 3

    def test_orchestrator_run(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent(), InsightSynthesizerAgent()]
        orch = Orchestrator(agents)
        result = orch.run("Analyze this data and compress it")

        assert "query" in result
        assert "routed_to" in result
        assert "status" in result
        assert result["status"] in ("completed", "failed")
        assert "duration_ms" in result


class TestParallelExecutor:
    def test_parallel_executor_creation(self):
        agents = [DataAnalystAgent(), CompressionExpertAgent()]
        executor = ParallelExecutor(agents)
        assert len(executor.agents) == 2

    def test_parallel_executor_run(self):
        agents = [DataAnalystAgent()]
        executor = ParallelExecutor(agents)
        queries = ["Query 1", "Query 2", "Query 3"]
        results = executor.run(queries)

        assert len(results) == 3
        for r in results:
            assert "query" in r
            assert "agent" in r
            assert "status" in r


if __name__ == "__main__":
    pytest.main([__file__, "-v"])