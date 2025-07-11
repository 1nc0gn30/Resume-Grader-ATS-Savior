import streamlit as st
from utils.grader import process_submission
import io

st.set_page_config(page_title="Submit Resume", layout="centered")
st.title("📤 Submit Resume for Grading")

with st.form("resume_form", clear_on_submit=False):
    name = st.text_input("🧑 Full Name")
    email = st.text_input("✉️ Email Address")
    preset = st.selectbox("🧠 Select Review Type", [
        "general_review", 
        "developer_focus", 
        "soft_skills", 
        "cybersecurity_analyst"
    ])
    uploaded = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])
    
    submitted = st.form_submit_button("🚀 Submit for Grading")

if submitted:
    if uploaded and name and email:
        # Log section
        with st.expander("📋 Process Log", expanded=True):
            st.write("✅ Form submitted.")
            st.write(f"📁 Uploaded file: `{uploaded.name}`")
            st.write(f"📌 Review preset selected: `{preset}`")
            st.write("📄 Reading and processing PDF...")
        
        # Read bytes
        bytes_data = uploaded.read()
        
        # Run grading
        with st.spinner("🤖 Grading with Ollama..."):
            result = process_submission(name, email, preset, bytes_data)
        
        st.success("✅ Grading complete!")
        st.markdown("### 📝 Evaluation Report")
        st.text_area("LLM Feedback", result, height=350)
    else:
        st.warning("⚠️ Please complete all fields and upload a resume.")
