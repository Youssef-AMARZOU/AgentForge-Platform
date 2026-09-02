"""
Unit tests for Netflix analysis engine.
Run with: pytest tests/test_netflix.py -v
"""

import pytest
import pandas as pd
from core.netflix.analysis import (
    NetflixCatalog,
    NetflixAnalystAgent,
    RecommendationAgent,
    CausalInferenceAgent,
    AnalysisResult,
)


class TestNetflixCatalog:
    @pytest.fixture
    def catalog(self):
        return NetflixCatalog()

    def test_catalog_loads(self, catalog):
        assert catalog.df is not None
        assert len(catalog.df) > 0

    def test_get_stats(self, catalog):
        stats = catalog.get_stats()
        assert "total_titles" in stats
        assert "movies" in stats
        assert "tv_shows" in stats
        assert stats["total_titles"] == stats["movies"] + stats["tv_shows"]
        assert stats["total_titles"] > 8000  # Netflix dataset size

    def test_search(self, catalog):
        results = catalog.search("Breaking", limit=5)
        assert isinstance(results, list)
        assert len(results) <= 5
        for r in results:
            assert "title" in r

    def test_filter_by_genre(self, catalog):
        results = catalog.filter_by(genre="Drama")
        assert isinstance(results, list)
        for r in results[:5]:
            assert "Drama" in r.get("listed_in", "")

    def test_filter_by_type(self, catalog):
        movies = catalog.filter_by(content_type="Movie")
        for m in movies[:5]:
            assert m["type"] == "Movie"
        tv = catalog.filter_by(content_type="TV Show")
        for t in tv[:5]:
            assert t["type"] == "TV Show"

    def test_filter_by_country(self, catalog):
        results = catalog.filter_by(country="United States")
        for r in results[:5]:
            assert "United States" in r.get("country", "")

    def test_filter_by_year(self, catalog):
        results = catalog.filter_by(year=2020)
        for r in results[:5]:
            assert r["release_year"] == 2020

    def test_temporal_trends(self, catalog):
        trends = catalog.get_temporal_trends()
        assert "years" in trends
        assert "movies" in trends
        assert "tv_shows" in trends
        assert len(trends["years"]) == len(trends["movies"])

    def test_geographic_distribution(self, catalog):
        geo = catalog.get_geographic_distribution()
        assert "countries" in geo
        assert "counts" in geo
        assert len(geo["countries"]) == len(geo["counts"])
        assert geo["countries"][0] == "United States"

    def test_genre_analysis(self, catalog):
        genres = catalog.get_genre_analysis()
        assert "genres" in genres
        assert "counts" in genres

    def test_rating_distribution(self, catalog):
        ratings = catalog.get_rating_distribution()
        assert "ratings" in ratings
        assert "counts" in ratings


class TestNetflixAnalystAgent:
    def test_agent_creation(self):
        agent = NetflixAnalystAgent()
        assert agent.catalog is not None

    def test_run_full_analysis(self):
        agent = NetflixAnalystAgent()
        result = agent.run_full_analysis()

        assert "stats" in result
        assert "temporal_trends" in result
        assert "geographic_distribution" in result
        assert "genre_analysis" in result
        assert "rating_distribution" in result
        assert "insights" in result
        assert len(result["insights"]) >= 3

    def test_insights_content(self):
        agent = NetflixAnalystAgent()
        result = agent.run_full_analysis()
        insights = result["insights"]

        assert any("outnumber" in i for i in insights)
        assert any("Peak content year" in i for i in insights)
        assert any("Top producing country" in i for i in insights)


class TestRecommendationAgent:
    def test_agent_creation(self):
        agent = RecommendationAgent()
        assert agent.catalog is not None

    def test_recommend_by_genre(self):
        agent = RecommendationAgent()
        results = agent.recommend(genre="Drama", n=3)
        assert isinstance(results, list)
        assert len(results) <= 3

    def test_recommend_random(self):
        agent = RecommendationAgent()
        results = agent.recommend(n=3)
        assert isinstance(results, list)
        assert len(results) <= 3


class TestCausalInferenceAgent:
    def test_agent_creation(self):
        agent = CausalInferenceAgent()
        assert agent.catalog is not None

    def test_estimate_effect_type_year(self):
        agent = CausalInferenceAgent()
        result = agent.estimate_effect(treatment="type", outcome="release_year")

        assert "treatment" in result
        assert "outcome" in result
        assert "ate" in result
        assert "treated_mean" in result
        assert "control_mean" in result
        assert "method" in result

    def test_estimate_effect_rating_duration(self):
        agent = CausalInferenceAgent()
        result = agent.estimate_effect(treatment="rating", outcome="duration_minutes")

        assert "ate" in result
        assert result["method"] == "Difference-in-means (simplified ATE estimation)"


class TestAnalysisResult:
    def test_result_creation(self):
        result = AnalysisResult(
            title="Test Analysis",
            data={"key": "value"},
            insights=["insight 1", "insight 2"],
        )
        assert result.title == "Test Analysis"
        assert result.data == {"key": "value"}
        assert len(result.insights) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])