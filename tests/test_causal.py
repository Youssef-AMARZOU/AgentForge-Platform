"""
Unit tests for causal inference module.
Run with: pytest tests/test_causal.py -v
"""

import pytest
from core.causal.inference import (
    CausalSpec,
    CausalResult,
    Actor,
    Critic,
    CausalAgent,
)


class TestCausalSpec:
    def test_spec_creation(self):
        spec = CausalSpec(
            treatment="type",
            outcome="release_year",
            estimand="ATE",
            covariates=["rating"],
            method="difference_in_means",
        )
        assert spec.treatment == "type"
        assert spec.outcome == "release_year"
        assert spec.covariates == ["rating"]


class TestCausalResult:
    def test_result_creation(self):
        spec = CausalSpec(treatment="type", outcome="release_year")
        result = CausalResult(
            spec=spec,
            estimate=5.2,
            std_error=1.1,
            ci_lower=3.0,
            ci_upper=7.4,
            n_treated=100,
            n_control=100,
        )
        assert result.estimate == 5.2
        assert result.ci_lower == 3.0
        assert result.ci_upper == 7.4


class TestActor:
    def test_actor_creation(self):
        actor = Actor()
        assert actor is not None

    def test_draft_spec_type_year(self):
        actor = Actor()
        spec = actor.draft_spec("Does movie type affect release year?")
        assert spec.treatment == "type"
        assert spec.outcome == "release_year"

    def test_draft_spec_rating_duration(self):
        actor = Actor()
        spec = actor.draft_spec("How does rating affect duration?")
        assert spec.treatment == "rating"
        assert spec.outcome == "duration_minutes"

    def test_draft_spec_movie_year(self):
        actor = Actor()
        spec = actor.draft_spec("Movie vs TV show year trends")
        assert spec.treatment == "type"
        assert spec.outcome == "release_year"

    def test_revise_spec_add_covariates(self):
        actor = Actor()
        spec = CausalSpec(treatment="type", outcome="release_year")
        revised = actor.revise_spec(spec, "add covariates")
        assert "release_year" in revised.covariates
        assert "rating" in revised.covariates

    def test_revise_spec_matching(self):
        actor = Actor()
        spec = CausalSpec(treatment="type", outcome="release_year")
        revised = actor.revise_spec(spec, "try matching")
        assert revised.method == "propensity_score_matching"


class TestCritic:
    def test_critic_creation(self):
        critic = Critic()
        assert critic is not None

    def test_review_satisfactory(self):
        critic = Critic()
        spec = CausalSpec(treatment="type", outcome="release_year")
        result = CausalResult(
            spec=spec,
            estimate=5.0,
            std_error=1.0,
            ci_lower=3.0,
            ci_upper=7.0,
            n_treated=100,
            n_control=100,
        )
        review = critic.review(result)
        assert review["verdict"] == "fully_satisfactory"
        assert len(review["issues"]) == 0

    def test_review_near_zero(self):
        critic = Critic()
        spec = CausalSpec(treatment="type", outcome="release_year")
        result = CausalResult(
            spec=spec,
            estimate=0.005,
            std_error=1.0,
            ci_lower=-1.0,
            ci_upper=1.0,
            n_treated=100,
            n_control=100,
        )
        review = critic.review(result)
        assert review["verdict"] in ("satisfactory_with_caveats", "not_satisfactory")
        assert any("near zero" in i.lower() for i in review["issues"])

    def test_review_small_sample(self):
        critic = Critic()
        spec = CausalSpec(treatment="type", outcome="release_year")
        result = CausalResult(
            spec=spec,
            estimate=5.0,
            std_error=1.0,
            ci_lower=3.0,
            ci_upper=7.0,
            n_treated=10,
            n_control=10,
        )
        review = critic.review(result)
        assert any("small sample" in i.lower() for i in review["issues"])

    def test_review_large_effect(self):
        critic = Critic()
        spec = CausalSpec(treatment="type", outcome="release_year")
        result = CausalResult(
            spec=spec,
            estimate=200.0,
            std_error=10.0,
            ci_lower=180.0,
            ci_upper=220.0,
            n_treated=100,
            n_control=100,
        )
        review = critic.review(result)
        assert any("unusually large" in i.lower() for i in review["issues"])


class TestCausalAgent:
    def test_agent_creation(self):
        agent = CausalAgent()
        assert agent.actor is not None
        assert agent.critic is not None
        assert agent.history == []

    def test_agent_run(self):
        agent = CausalAgent()

        def mock_data_fn(spec: CausalSpec) -> CausalResult:
            return CausalResult(
                spec=spec,
                estimate=2.5,
                std_error=0.5,
                ci_lower=1.5,
                ci_upper=3.5,
                n_treated=500,
                n_control=500,
            )

        result = agent.run("Does movie type affect release year?", mock_data_fn)

        assert "question" in result
        assert "spec" in result
        assert "estimate" in result
        assert "verdict" in result
        assert result["verdict"] == "fully_satisfactory"
        assert len(agent.history) == 1

    def test_agent_run_with_revision(self):
        agent = CausalAgent()
        call_count = 0

        def mock_data_fn(spec: CausalSpec) -> CausalResult:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # First call - small sample to trigger revision
                return CausalResult(
                    spec=spec,
                    estimate=2.5,
                    std_error=0.5,
                    ci_lower=1.5,
                    ci_upper=3.5,
                    n_treated=10,
                    n_control=10,
                )
            # Second call - larger sample
            return CausalResult(
                spec=spec,
                estimate=2.5,
                std_error=0.5,
                ci_lower=1.5,
                ci_upper=3.5,
                n_treated=500,
                n_control=500,
            )

        result = agent.run("Test question", mock_data_fn)

        # Should have run twice (initial + revision)
        assert call_count == 2
        assert len(agent.history) == 1  # Only final result in history


if __name__ == "__main__":
    pytest.main([__file__, "-v"])