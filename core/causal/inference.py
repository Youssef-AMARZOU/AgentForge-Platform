"""
Causal Inference Module
Based on Netflix OCI Agent pattern: actor-critic approach for causal analysis.
"""

from dataclasses import dataclass, field
from typing import Any
import json


@dataclass
class CausalSpec:
    treatment: str
    outcome: str
    estimand: str = "ATE"
    covariates: list[str] = field(default_factory=list)
    method: str = "difference_in_means"


@dataclass
class CausalResult:
    spec: CausalSpec
    estimate: float
    std_error: float
    ci_lower: float
    ci_upper: float
    n_treated: int
    n_control: int
    verdict: str = ""
    critique: str = ""


class Actor:
    """Translates causal questions into analysis specs."""

    def draft_spec(self, question: str) -> CausalSpec:
        q = question.lower()
        treatment = "type"
        outcome = "release_year"
        if "movie" in q or "film" in q:
            treatment = "type"
        if "rating" in q or "mature" in q:
            treatment = "rating"
        if "year" in q or "trend" in q:
            outcome = "release_year"
        if "duration" in q or "length" in q:
            outcome = "duration_minutes"

        return CausalSpec(
            treatment=treatment,
            outcome=outcome,
            covariates=[],
            method="difference_in_means",
        )

    def revise_spec(self, spec: CausalSpec, critique: str) -> CausalSpec:
        if "add covariates" in critique.lower():
            spec.covariates = ["release_year", "rating"]
        if "try matching" in critique.lower():
            spec.method = "propensity_score_matching"
        return spec


class Critic:
    """Reviews causal analysis results and provides feedback."""

    def review(self, result: CausalResult) -> dict:
        issues = []
        if abs(result.estimate) < 0.01:
            issues.append("Estimate near zero -- may be underpowered")
        if result.n_treated < 30 or result.n_control < 30:
            issues.append("Small sample size in one or both groups")
        if abs(result.estimate) > 100:
            issues.append("Effect size unusually large -- check data")

        if not issues:
            verdict = "fully_satisfactory"
        elif len(issues) == 1:
            verdict = "satisfactory_with_caveats"
        else:
            verdict = "not_satisfactory"

        return {
            "verdict": verdict,
            "issues": issues,
            "suggestion": "Add covariates for more precise estimates" if issues else "Results look good",
        }


class CausalAgent:
    """Full actor-critic causal inference agent."""

    def __init__(self):
        self.actor = Actor()
        self.critic = Critic()
        self.history: list[dict] = []

    def run(self, question: str, data_fn) -> dict:
        spec = self.actor.draft_spec(question)
        result = data_fn(spec)
        review = self.critic.review(result)

        if review["verdict"] != "fully_satisfactory":
            spec = self.actor.revise_spec(spec, review["suggestion"])
            result = data_fn(spec)
            review = self.critic.review(result)

        entry = {
            "question": question,
            "spec": {"treatment": spec.treatment, "outcome": spec.outcome, "method": spec.method},
            "estimate": result.estimate,
            "ci": [result.ci_lower, result.ci_upper],
            "verdict": review["verdict"],
            "issues": review["issues"],
        }
        self.history.append(entry)
        return entry
