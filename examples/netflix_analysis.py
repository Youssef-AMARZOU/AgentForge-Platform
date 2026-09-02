#!/usr/bin/env python
"""
Example: Netflix Analysis Usage
Run with: python examples/netflix_analysis.py
"""

from core.netflix.analysis import (
    NetflixCatalog,
    NetflixAnalystAgent,
    RecommendationAgent,
    CausalInferenceAgent,
)


def main():
    print("=" * 60)
    print("NETFLIX ANALYSIS EXAMPLES")
    print("=" * 60)

    # 1. Direct catalog access
    print("\n1. DIRECT CATALOG ACCESS")
    print("-" * 40)
    catalog = NetflixCatalog()

    stats = catalog.get_stats()
    print(f"Total titles:  {stats['total_titles']:,}")
    print(f"Movies:        {stats['movies']:,}")
    print(f"TV Shows:      {stats['tv_shows']:,}")
    print(f"Countries:     {stats['countries']}")
    print(f"Year range:    {stats['year_range']['min']} - {stats['year_range']['max']}")

    # Search
    results = catalog.search("Breaking Bad", limit=3)
    print(f"\nSearch 'Breaking Bad': {len(results)} results")
    for r in results:
        print(f"  - {r['title']} ({r['type']})")

    # Filter
    dramas = catalog.filter_by(genre="Drama", content_type="Movie")
    print(f"\nDrama Movies (top 5):")
    for d in dramas[:5]:
        print(f"  - {d['title']} ({d['release_year']})")

    # 2. Analyst Agent - Full Analysis
    print("\n2. NETFLIX ANALYST AGENT (Full Analysis)")
    print("-" * 40)
    analyst = NetflixAnalystAgent()
    result = analyst.run_full_analysis()

    print(f"Total titles: {result['stats']['total_titles']:,}")
    print(f"\nInsights:")
    for insight in result['insights']:
        print(f"  - {insight}")

    print(f"\nTop genres:")
    for genre, count in list(result['genre_analysis'].items())[:5]:
        print(f"  - {genre}: {count}")

    print(f"\nTop countries:")
    for country, count in list(result['geographic_distribution'].items())[:5]:
        print(f"  - {country}: {count}")

    # 3. Temporal trends
    print("\n3. TEMPORAL TRENDS")
    print("-" * 40)
    trends = catalog.get_temporal_trends()
    for year, movies, tv in zip(
        trends['years'][-5:],
        trends['movies'][-5:],
        trends['tv_shows'][-5:],
    ):
        print(f"  {year}: Movies={movies}, TV Shows={tv}")

    # 4. Recommendations
    print("\n4. RECOMMENDATION AGENT")
    print("-" * 40)
    recommender = RecommendationAgent()

    # By genre
    drama_recs = recommender.recommend(genre="Thriller", n=3)
    print("Thriller recommendations:")
    for r in drama_recs:
        print(f"  - {r['title']} ({r['type']}, {r['release_year']})")

    # Random
    random_recs = recommender.recommend(n=3)
    print("\nRandom picks:")
    for r in random_recs:
        print(f"  - {r['title']} ({r['type']}, {r['release_year']})")

    # 5. Causal Inference
    print("\n5. CAUSAL INFERENCE AGENT")
    print("-" * 40)
    causal = CausalInferenceAgent()

    # Does movie type affect release year?
    result = causal.estimate_effect(treatment="type", outcome="release_year")
    print(f"Treatment: type (Movie vs TV Show)")
    print(f"Outcome:   release_year")
    print(f"ATE:       {result['ate']:.2f} years")
    print(f"Movie mean:    {result['treated_mean']:.1f}")
    print(f"TV Show mean:  {result['control_mean']:.1f}")
    print(f"95% CI:    [{result['ci_lower']:.1f}, {result['ci_upper']:.1f}]")

    # Does rating affect duration?
    result = causal.estimate_effect(treatment="rating", outcome="duration_minutes")
    print(f"\nTreatment: rating (Mature vs General)")
    print(f"Outcome:   duration_minutes")
    print(f"ATE:       {result['ate']:.1f} minutes")
    print(f"Method:    {result['method']}")


if __name__ == "__main__":
    main()