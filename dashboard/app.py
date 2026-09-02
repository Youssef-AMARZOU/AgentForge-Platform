"""
Streamlit Dashboard for AgentForge Platform
Interactive visualization of compression results and Netflix analysis.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from core.netflix.analysis import NetflixCatalog, NetflixAnalystAgent, RecommendationAgent, CausalInferenceAgent
from core.compression.engines import compress, count_tokens

st.set_page_config(page_title="AgentForge Platform", page_icon="forging", layout="wide")

st.title("AgentForge Platform")
st.markdown("*Compression + Multi-Agent + Netflix Analysis -- all in one*")

tab1, tab2, tab3, tab4 = st.tabs(["Compression", "Netflix Analysis", "Recommendations", "Causal Inference"])

with tab1:
    st.header("Token Compression Engine")
    st.markdown("Compare Headroom, Claw Compactor, and SuperCompress on your data")

    text_input = st.text_area("Enter text to compress (JSON, logs, or any text):", height=200)
    col1, col2 = st.columns(2)
    with col1:
        engine = st.selectbox("Engine", ["auto", "headroom", "claw", "super"])
    with col2:
        query = st.query if hasattr(st, "query") else st.text_input("Query (for SuperCompress):")

    if st.button("Compress") and text_input:
        result = compress(text_input, engine=engine, query=query)
        col1, col2, col3 = st.columns(3)
        col1.metric("Original", f"{result.original_tokens:,} tokens")
        col2.metric("Compressed", f"{result.compressed_tokens:,} tokens")
        col3.metric("Savings", f"{result.savings_pct}%")

        with st.expander("Compressed Output"):
            st.code(result.compressed_text)

with tab2:
    st.header("Netflix Catalog Analysis")
    try:
        agent = NetflixAnalystAgent()
        analysis = agent.run_full_analysis()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Titles", f"{analysis['stats']['total_titles']:,}")
        col2.metric("Movies", f"{analysis['stats']['movies']:,}")
        col3.metric("TV Shows", f"{analysis['stats']['tv_shows']:,}")

        fig = px.bar(
            x=analysis["genre_analysis"]["genres"][:10],
            y=analysis["genre_analysis"]["counts"][:10],
            title="Top 10 Genres",
        )
        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            fig = px.pie(
                names=["Movies", "TV Shows"],
                values=[analysis["stats"]["movies"], analysis["stats"]["tv_shows"]],
                title="Movies vs TV Shows",
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.bar(
                x=analysis["geographic_distribution"]["countries"][:10],
                y=analysis["geographic_distribution"]["counts"][:10],
                title="Top 10 Countries",
            )
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Insights")
        for insight in analysis["insights"]:
            st.info(insight)
    except Exception as e:
        st.error(f"Error loading Netflix data: {e}")

with tab3:
    st.header("Content Recommendations")
    try:
        rec_agent = RecommendationAgent()
        genre = st.text_input("Genre:", "Action")
        if st.button("Get Recommendations"):
            recs = rec_agent.recommend(genre=genre)
            if recs:
                df = pd.DataFrame(recs)
                st.dataframe(df[["title", "type", "rating", "listed_in"]].head(5))
            else:
                st.warning("No recommendations found")
    except Exception as e:
        st.error(f"Error: {e}")

with tab4:
    st.header("Causal Inference (Netflix OCI Agent)")
    try:
        causal_agent = CausalInferenceAgent()
        treatment = st.selectbox("Treatment:", ["type", "rating"])
        outcome = st.selectbox("Outcome:", ["release_year", "duration_minutes"])

        if st.button("Estimate Effect"):
            result = causal_agent.estimate_effect(treatment, outcome)
            col1, col2, col3 = st.columns(3)
            col1.metric("ATE", f"{result['ate']:.4f}")
            col2.metric("Treated Mean", f"{result['treated_mean']:.4f}")
            col3.metric("Control Mean", f"{result['control_mean']:.4f}")

            st.json(result)
    except Exception as e:
        st.error(f"Error: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("**AgentForge Platform**")
st.sidebar.markdown("Built on:")
st.sidebar.markdown("- [Headroom](https://github.com/headroomlabs-ai/headroom)")
st.sidebar.markdown("- [FastMCP](https://github.com/PrefectHQ/fastmcp)")
st.sidebar.markdown("- [mcp-agent](https://github.com/lastmile-ai/mcp-agent)")
st.sidebar.markdown("- [MetaGPT](https://github.com/geekan/MetaGPT)")
st.sidebar.markdown("- [Netflix OCI Agent](https://github.com/Netflix-Skunkworks/oci-agent)")
st.sidebar.markdown("- [Claw Compactor](https://github.com/open-compress/claw-compactor)")
st.sidebar.markdown("- [SuperCompress](https://github.com/Supercompress/Supercompress)")
