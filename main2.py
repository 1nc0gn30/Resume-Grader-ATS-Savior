import streamlit as st

st.set_page_config(page_title="Applicant Redirector", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
        body {
            background-color: #111;
            color: white;
        }
        .stApp {
            background-color: #111;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 👋 Welcome to Applicant Redirector

This tool allows you to:
- ✅ Upload resumes and applications for AI-driven grading
- 📈 Track submission scores over time
- 🎯 View grade distribution across Green, Yellow, and Red categories
- 🧾 Store and review detailed LLM analysis for every submission

### 🔍 Use the sidebar to:
- **Submit** a new resume
- **View Results** from past applicants
- **Explore Dashboard** with charts and metrics

---

Built with ❤️ using Python, Streamlit, and Ollama.
""")
