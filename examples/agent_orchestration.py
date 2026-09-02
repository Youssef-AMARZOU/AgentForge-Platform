#!/usr/bin/env python
"""
Example: Agent Orchestration Usage
Run with: python examples/agent_orchestration.py
"""

from core.agents.orchestrator import (
    AgentTask,
    DataAnalystAgent,
    CompressionExpertAgent,
    InsightSynthesizerAgent,
    Router,
    Orchestrator,
    ParallelExecutor,
)


def main():
    print("=" * 60)
    print("AGENT ORCHESTRATION EXAMPLES")
    print("=" * 60)

    # Create agents
    analyst = DataAnalystAgent()
    compressor = CompressionExpertAgent()
    synthesizer = InsightSynthesizerAgent()
    agents = [analyst, compressor, synthesizer]

    # 1. Router - routes to best agent
    print("\n1. ROUTER PATTERN")
    print("-" * 40)
    router = Router(agents)

    tasks = [
        AgentTask(id="r1", description="Compress this JSON payload"),
        AgentTask(id="r2", description="Analyze the sales dataset for trends"),
        AgentTask(id="r3", description="Summarize the findings into a report"),
    ]

    for task in tasks:
        agent = router.route(task)
        result = agent.execute(task)
        print(f"Task: '{task.description[:40]}...'")
        print(f"  -> Routed to: {agent.spec.name}")
        print(f"  -> Status: {result.status}")

    # 2. Orchestrator-Workers pattern
    print("\n2. ORCHESTRATOR-WORKERS PATTERN")
    print("-" * 40)
    orchestrator = Orchestrator(agents)

    queries = [
        "Analyze Netflix catalog and compress the results",
        "Compress server logs and provide insights",
    ]

    for query in queries:
        result = orchestrator.run(query)
        print(f"Query: {query}")
        print(f"  -> Routed to: {result['routed_to']}")
        print(f"  -> Status: {result['status']}")
        if result['result']:
            print(f"  -> Result keys: {list(result['result'].keys())}")

    # 3. Parallel Map-Reduce
    print("\n3. PARALLEL MAP-REDUCE PATTERN")
    print("-" * 40)
    parallel = ParallelExecutor([analyst])
    queries = [
        "Analyze Q1 revenue trends",
        "Analyze user retention metrics",
        "Analyze feature adoption rates",
    ]
    results = parallel.run(queries)

    for r in results:
        print(f"Query: {r['query']}")
        print(f"  -> Agent: {r['agent']}")
        print(f"  -> Status: {r['status']}")

    # 4. Compression expert with token tracking
    print("\n4. COMPRESSION WITH TOKEN TRACKING")
    print("-" * 40)
    import json
    large_json = json.dumps([{"id": i, "data": "x" * 200} for i in range(200)])

    task = AgentTask(id="comp-001", description=large_json)
    result = compressor.execute(task)

    print(f"Engine used:     {result.result['engine']}")
    print(f"Original tokens: {result.result['original_tokens']:,}")
    print(f"Compressed:      {result.result['compressed_tokens']:,}")
    print(f"Savings:         {result.result['savings_pct']}%")
    print(f"Duration:        {result.duration_ms:.1f}ms")


if __name__ == "__main__":
    main()