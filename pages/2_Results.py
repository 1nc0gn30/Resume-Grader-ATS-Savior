import streamlit as st
from utils.db import get_all_reports

def get_grade_color(score):
    try:
        score = int(score)
    except (ValueError, TypeError):
        return "gray"

    if score >= 80:
        return "green"
    elif score >= 60:
        return "yellow"
    else:
        return "red"

def get_color_hex(color_name):
    return {
        "green": "#22c55e",
        "yellow": "#eab308",
        "red": "#ef4444",
        "gray": "#6b7280"
    }.get(color_name, "#6b7280")

st.set_page_config(page_title="Results", layout="wide")
st.title("📁 View All Graded Applications")

results = get_all_reports()

if not results:
    st.info("No submissions yet.")
else:
    for r in results[::-1]:  # newest first
        record_id, name, email, preset, score, report, pdf_path = r
        color_name = get_grade_color(score)
        hex_color = get_color_hex(color_name)

        with st.container():
            st.markdown(f"### 👤 {name} ({email})")
            st.markdown(f"**Review Type:** {preset}")

            badge_html = f"""
                <div style='
                    background-color: {hex_color};
                    display: inline-block;
                    padding: 5px 12px;
                    border-radius: 10px;
                    color: white;
                    font-weight: bold;
                    margin-top: 6px;
                '>
                    Score: {score if score is not None else 'N/A'} ({color_name.upper()})
                </div>
            """
            st.markdown(badge_html, unsafe_allow_html=True)

            st.markdown("#### 🤖 LLM Report")
            st.text_area("Full Feedback", report or "No feedback found.", height=300)

            if pdf_path and st.button(f"📥 Download PDF for #{record_id}", key=f"download-{record_id}"):
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="Download Resume PDF",
                        data=f,
                        file_name=f"resume_{name}_{record_id}.pdf",
                        mime="application/pdf"
                    )

        st.divider()
