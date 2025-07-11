import streamlit as st
from utils.db import get_all_reports
from utils.charts import plot_pie_chart, plot_score_trend
import pandas as pd

st.set_page_config(page_title="Applicant Redirector Dashboard", layout="wide", page_icon="📊")

# ========== Custom CSS ==========
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: white;
        }
        .stMetric {
            color: white !important;
        }
        .element-container:has(.stMetric) {
            background: #1a1a1a;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)

# ========== Title ==========
st.markdown("""
    <h1 style="color:#ffffff; text-align:center; margin-bottom:10px;">📊 Applicant Redirector Dashboard</h1>
    <hr style="border:1px solid #444;">
""", unsafe_allow_html=True)

reports = get_all_reports()
total = len(reports)

# ========== Top Stats ==========
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📄 Total Submissions", value=total)
    with col2:
        if total > 0:
            last_score = reports[-1][4]
            st.metric(label="🔍 Last Submission Score", value=last_score)
        else:
            st.metric(label="🔍 Last Submission Score", value="N/A")

st.markdown("---")

# ========== Chart Section ==========
if reports:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Grade Distribution")
        st.pyplot(plot_pie_chart(reports), use_container_width=True)

    with col2:
        st.markdown("### 📈 Resume Scores Over Time")
        st.pyplot(plot_score_trend(reports), use_container_width=True)

    st.markdown("---")
    
    with st.expander("🗃️ Show Raw Data Table"):
        df = pd.DataFrame(reports, columns=["ID", "Name", "Email", "Preset", "Score", "LLM Report", "PDF Path"])
        st.dataframe(df.drop(columns=["LLM Report", "PDF Path"]))
else:
    st.info("🕵️‍♂️ No results yet. Submit a resume first to populate your dashboard.")
