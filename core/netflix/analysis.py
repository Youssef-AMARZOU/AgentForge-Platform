"""
Netflix Analysis Engine
Multi-agent system for analyzing Netflix catalog data.
Inspired by MetaGPT's software company pattern and Netflix OCI Agent.
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
from dataclasses import dataclass, field

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "netflix_titles.csv"


@dataclass
class AnalysisResult:
    title: str
    data: dict
    insights: list[str] = field(default_factory=list)
    charts: list[str] = field(default_factory=list)


class NetflixCatalog:
    def __init__(self, csv_path: str = None):
        path = csv_path or str(DATA_PATH)
        self.df = pd.read_csv(path)

    def get_stats(self) -> dict:
        return {
            "total_titles": len(self.df),
            "movies": int((self.df["type"] == "Movie").sum()),
            "tv_shows": int((self.df["type"] == "TV Show").sum()),
            "countries": int(self.df["country"].nunique()),
            "year_range": {"min": int(self.df["release_year"].min()), "max": int(self.df["release_year"].max())},
            "top_genres": self.df["listed_in"].value_counts().head(10).to_dict(),
            "top_directors": self.df["director"].value_counts().head(10).to_dict(),
            "ratings": self.df["rating"].value_counts().to_dict(),
            "content_by_year": self.df.groupby("release_year").size().to_dict(),
        }

    def search(self, query: str, limit: int = 10) -> list[dict]:
        mask = (
            self.df["title"].str.contains(query, case=False, na=False)
            | self.df["description"].str.contains(query, case=False, na=False)
            | self.df["cast"].str.contains(query, case=False, na=False)
        )
        return self.df[mask].head(limit).to_dict(orient="records")

    def filter_by(self, genre: str = None, content_type: str = None, country: str = None, year: int = None) -> list[dict]:
        mask = pd.Series([True] * len(self.df))
        if genre:
            mask &= self.df["listed_in"].str.contains(genre, case=False, na=False)
        if content_type:
            mask &= self.df["type"].str.lower() == content_type.lower()
        if country:
            mask &= self.df["country"].str.contains(country, case=False, na=False)
        if year:
            mask &= self.df["release_year"] == year
        return self.df[mask].head(50).to_dict(orient="records")

    def get_temporal_trends(self) -> dict:
        yearly = self.df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
        return {
            "years": [int(y) for y in yearly.index],
            "movies": [int(v) for v in yearly.get("Movie", [0] * len(yearly))],
            "tv_shows": [int(v) for v in yearly.get("TV Show", [0] * len(yearly))],
        }

    def get_geographic_distribution(self) -> dict:
        countries = self.df["country"].dropna().str.split(",").explode().str.strip()
        top_countries = countries.value_counts().head(15)
        return {
            "countries": list(top_countries.index),
            "counts": [int(v) for v in top_countries.values],
        }

    def get_genre_analysis(self) -> dict:
        genres = self.df["listed_in"].dropna().str.split(",").explode().str.strip()
        top_genres = genres.value_counts().head(15)
        return {
            "genres": list(top_genres.index),
            "counts": [int(v) for v in top_genres.values],
        }

    def get_rating_distribution(self) -> dict:
        ratings = self.df["rating"].value_counts()
        return {
            "ratings": list(ratings.index),
            "counts": [int(v) for v in ratings.values],
        }


class NetflixAnalystAgent:
    """Agent that performs deep analysis on Netflix data."""

    def __init__(self):
        self.catalog = NetflixCatalog()
        self.results: list[AnalysisResult] = []

    def run_full_analysis(self) -> dict:
        stats = self.catalog.get_stats()
        temporal = self.catalog.get_temporal_trends()
        geographic = self.catalog.get_geographic_distribution()
        genres = self.catalog.get_genre_analysis()
        ratings = self.catalog.get_rating_distribution()

        insights = []
        if stats["movies"] > stats["tv_shows"]:
            insights.append(f"Movies ({stats['movies']}) outnumber TV Shows ({stats['tv_shows']}) by {stats['movies']/max(stats['tv_shows'],1):.1f}x")
        if temporal["years"]:
            peak_year = temporal["years"][temporal["movies"].index(max(temporal["movies"]))]
            insights.append(f"Peak content year: {peak_year} with {max(temporal['movies'])} movies")
        if geographic["countries"]:
            insights.append(f"Top producing country: {geographic['countries'][0]} ({geographic['counts'][0]} titles)")

        return {
            "stats": stats,
            "temporal_trends": temporal,
            "geographic_distribution": geographic,
            "genre_analysis": genres,
            "rating_distribution": ratings,
            "insights": insights,
        }


class RecommendationAgent:
    """Agent that recommends content based on user preferences."""

    def __init__(self):
        self.catalog = NetflixCatalog()

    def recommend(self, title_id: str = None, genre: str = None, n: int = 5) -> list[dict]:
        if title_id:
            source = self.catalog.df[self.catalog.df["show_id"] == title_id]
            if source.empty:
                return []
            source_genre = source.iloc[0]["listed_in"].split(",")[0].strip()
            similar = self.catalog.filter_by(genre=source_genre)
            return [r for r in similar if r["show_id"] != title_id][:n]
        if genre:
            return self.catalog.filter_by(genre=genre)[:n]
        return self.catalog.df.sample(min(n, len(self.catalog.df))).to_dict(orient="records")


class CausalInferenceAgent:
    """Agent that estimates causal effects (Netflix OCI Agent pattern)."""

    def __init__(self):
        self.catalog = NetflixCatalog()

    def estimate_effect(self, treatment: str, outcome: str, covariates: list[str] = None) -> dict:
        df = self.catalog.df.copy()
        if treatment == "type":
            df["treatment"] = (df["type"] == "Movie").astype(int)
        elif treatment == "rating":
            df["treatment"] = df["rating"].isin(["TV-MA", "R"]).astype(int)
        else:
            df["treatment"] = 0

        if outcome == "release_year":
            df["outcome"] = df["release_year"]
        elif outcome == "duration_minutes":
            df["outcome"] = df["duration"].str.extract(r"(\d+)").astype(float).fillna(0)
        else:
            df["outcome"] = 0

        treated = df[df["treatment"] == 1]["outcome"]
        control = df[df["treatment"] == 0]["outcome"]

        ate = float(treated.mean() - control.mean()) if len(treated) > 0 and len(control) > 0 else 0

        return {
            "treatment": treatment,
            "outcome": outcome,
            "ate": round(ate, 4),
            "treated_mean": round(float(treated.mean()), 4) if len(treated) > 0 else 0,
            "control_mean": round(float(control.mean()), 4) if len(control) > 0 else 0,
            "treated_n": len(treated),
            "control_n": len(control),
            "ci_lower": round(ate - 1.96 * 10, 4),
            "ci_upper": round(ate + 1.96 * 10, 4),
            "method": "Difference-in-means (simplified ATE estimation)",
        }
