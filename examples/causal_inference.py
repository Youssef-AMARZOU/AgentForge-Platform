#!/usr/bin/env python
"""
Example: Causal Inference (Actor-Critic Pattern)
Run with: python examples/causal_inference.py
"""

from core.causal.inference import Actor, Critic, CausalAgent, CausalSpec, CausalResult
from core.netflix.analysis import NetflixCatalog


def main():
    print("=" * 60)
    print("CAUSAL INFERENCE EXAMPLES (Actor-Critic Pattern)")
    print("=" * 60)

    # 1. Actor - Draft specs from questions
    print("\n1. ACTOR: DRAFT SPECS FROM QUESTIONS")
    print("-" * 40)
    actor = Actor()

    questions = [
        "Does movie type affect release year?",
        "How does mature rating affect duration?",
        "What's the trend for movies vs TV shows over time?",
    ]

    for q in questions:
        spec = actor.draft_spec(q)
        print(f"Q: {q}")
        print(f"  -> Treatment: {spec.treatment}")
        print(f"  -> Outcome:   {spec.outcome}")
        print(f"  -> Method:    {spec.method}")

    # 2. Critic - Review results
    print("\n2. CRITIC: REVIEW RESULTS")
    print("-" * 40)
    critic = Critic()

    spec = CausalSpec(treatment="type", outcome="release_year")
    result = CausalResult(
        spec=spec,
        estimate=5.2,
        std_error=1.1,
        ci_lower=3.0,
        ci_upper=7.4,
        n_treated=500,
        n_control=500,
    )
    review = critic.review(result)
    print(f"Estimate: {result.estimate}")
    print(f"Verdict:  {review['verdict']}")
    print(f"Issues:   {review['issues']}")
    print(f"Suggestion: {review['suggestion']}")

    # Near-zero estimate
    result2 = CausalResult(
        spec=spec,
        estimate=0.001,
        std_error=0.5,
        ci_lower=-1.0,
        ci_upper=1.0,
        n_treated=100,
        n_control=100,
    )
    review2 = critic.review(result2)
    print(f"\nNear-zero estimate:")
    print(f"  Verdict: {review2['verdict']}")
    print(f"  Issues:  {review2['issues']}")

    # 3. Full Actor-Critic Agent with Netflix data
    print("\n3. FULL ACTOR-CRITIC AGENT WITH NETFLIX DATA")
    print("-" * 40)

    catalog = NetflixCatalog()

    def run_analysis(spec: CausalSpec) -> CausalResult:
        df = catalog.df.copy()

        if spec.treatment == "type":
            df["treatment"] = (df["type"] == "Movie").astype(int)
        elif spec.treatment == "rating":
            df["treatment"] = df["rating"].isin(["TV-MA", "R"]).astype(int)
        else:
            df["treatment"] = 0

        if spec.outcome == "release_year":
            df["outcome"] = df["release_year"]
        elif spec.outcome == "duration_minutes":
            df["outcome"] = df["duration"].str.extract(r"(\d+)").astype(float).fillna(0)
        else:
            df["outcome"] = 0

        treated = df[df["treatment"] == 1]["outcome"]
        control = df[df["treatment"] == 0]["outcome"]

        ate = float(treated.mean() - control.mean()) if len(treated) > 0 and len(control) > 0 else 0

        return CausalResult(
            spec=spec,
            estimate=round(ate, 4),
            std_error=0.1,
            ci_lower=round(ate - 1.96 * 0.1, 4),
            ci_upper=round(ate + 1.96 * 0.1, 4),
            n_treated=len(treated),
            n_control=len(control),
        )

    agent = CausalAgent()

    questions = [
        "Does movie type affect release year?",
        "Does mature rating affect duration?",
    ]

    for q in questions:
        result = agent.run(q, run_analysis)
        print(f"\nQuestion: {q}")
        print(f"  Spec:     {result['spec']['treatment']} -> {result['spec']['outcome']}")
        print(f"  Estimate: {result['estimate']}")
        print(f"  95% CI:   {result['ci']}")
        print(f"  Verdict:  {result['verdict']}")

    # 4. Show history
    print("\n4. AGENT HISTORY")
    print("-" * 40)
    for entry in agent.history:
        print(f"  Q: {entry['question']}")
        print(f"    -> {entry['spec']['treatment']} -> {entry['spec']['outcome']} = {entry['estimate']}")


if __name__ == "__main__":
    main()