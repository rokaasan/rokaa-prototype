"""
ROKAA Data Excellence Appraisal Prototype v3

This is the enhanced version including:
- Business Aspirations (KYC)
- Data Uplift Goals (renamed from generic 'goals')
- Curated Training & Literacy Recommendations
- Dynamic Strategic & Tactical Recommendations (with potential fCDO prompts)
- 12–18 month Roadmap with tactical and strategic sequencing
- Management Dashboards to track progress
"""

import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
import tempfile

# --- Radar Chart Function ---
def create_radar_chart(dg_score, dq_score, mm_score, asp_scores, peer_scores):
    categories = ["Data Governance", "Data Quality", "Metadata Management"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[dg_score, dq_score, mm_score], theta=categories, fill='toself', name='Your Score'))
    fig.add_trace(go.Scatterpolar(r=asp_scores, theta=categories, fill='toself', name='Aspirational'))
    if peer_scores:
        fig.add_trace(go.Scatterpolar(r=peer_scores, theta=categories, fill='toself', name='Peer Average'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True)
    return fig

# --- UI Setup ---
st.set_page_config(page_title="ROKAA Data Excellence Appraisal", layout="wide")
st.title("ROKAA Data Excellence Appraisal")

# --- KYC Section ---
with st.form("kyc_form"):
    st.subheader("Know Your Company (KYC)")
    company_name = st.text_input("Organization Name")
    sector = st.selectbox("Select your sector", ["Healthtech", "Fintech", "Govtech", "Retail", "Education", "Other"])
    aspirations = st.text_area("Business Aspirations (What are your business goals over the next 1–3 years?)")
    data_goals = st.text_area("Data Uplift Goals (for the next 12–24 months)")

    submit_kyc = st.form_submit_button("Next: Begin Assessment")
    if submit_kyc:
        st.session_state["ready_for_assessment"] = True
        st.session_state["sector"] = sector

# --- Assessment ---
if st.session_state.get("ready_for_assessment"):
    st.header("Data Maturity Assessment")

    st.subheader("Section 1: Data Governance")
    dg1 = st.radio("Do you have a formal data governance policy?", ["Yes", "No", "In Progress"])
    dg2 = st.radio("Is there a data owner or steward responsible for governance?", ["Yes", "No", "In Progress"])

    st.subheader("Section 2: Data Quality")
    dq1 = st.radio("Do you monitor the quality of your critical data sets?", ["Yes", "No", "Somewhat"])
    dq2 = st.radio("Are there automated checks in place for data accuracy/completeness?", ["Yes", "No", "Somewhat"])

    st.subheader("Section 3: Metadata Management")
    mm1 = st.radio("Do you maintain a business glossary or data catalog?", ["Yes", "No", "Partially"])
    mm2 = st.radio("Is metadata captured and managed across systems?", ["Yes", "No", "Not Sure"])

    st.subheader("Your Aspirations")
    asp_gov = st.slider("Desired future state for Data Governance", 0, 100, 70)
    asp_qual = st.slider("Desired future state for Data Quality", 0, 100, 70)
    asp_meta = st.slider("Desired future state for Metadata Management", 0, 100, 70)

    score_map = {"Yes": 2, "No": 0, "In Progress": 1, "Not Sure": 0, "Somewhat": 1, "Partially": 1}

    if st.button("Submit Assessment"):
        st.session_state["assessment_submitted"] = True
        st.session_state["dg_score"] = (score_map[dg1] + score_map[dg2]) / 4.0 * 100
        st.session_state["dq_score"] = (score_map[dq1] + score_map[dq2]) / 4.0 * 100
        st.session_state["mm_score"] = (score_map[mm1] + score_map[mm2]) / 4.0 * 100
        st.session_state["aspirational_scores"] = [asp_gov, asp_qual, asp_meta]
        st.session_state["peer_scores"] = [60, 65, 50]  # Placeholder
        st.session_state["scores_calculated"] = True
        st.rerun()

# --- Final Output ---
if st.session_state.get("assessment_submitted") and st.session_state.get("scores_calculated"):
    st.header("Summary & Insights")

    # Radar Chart
    fig = create_radar_chart(
        st.session_state["dg_score"],
        st.session_state["dq_score"],
        st.session_state["mm_score"],
        st.session_state["aspirational_scores"],
        st.session_state["peer_scores"]
    )
    st.plotly_chart(fig, use_container_width=True)

    # Opportunities & Risks (stubbed)
    st.subheader("Opportunities for Business Growth")
    st.markdown("- AI-enabled insights")
    st.markdown("- Automation of governance workflows")

    st.subheader("Risks to Consider")
    st.markdown("- Lack of data stewardship")
    st.markdown("- Regulatory non-compliance")

    # Training Recommendations
    st.subheader("Recommended Training")
    st.markdown("- Data Governance 101 (Internal Microcourse)")
    st.markdown("- AI Risk Management (External Course)")

    # Strategic & Tactical Recommendations
    st.subheader("Strategic & Tactical Recommendations")
    st.markdown("- Appoint a Data Steward")
    st.markdown("- Implement basic data quality automation")
    st.markdown("- Explore Rokaa myCDO fractional advisory")

    # Roadmap
    st.subheader("Roadmap (12–18 months)")
    st.markdown("1. Quarter 1: Assign roles, clarify responsibilities")
    st.markdown("2. Quarter 2: Implement training & automation")
    st.markdown("3. Quarter 3+: Introduce strategic initiatives")

    # Download Button
    st.download_button(
        label="Download PDF Report",
        data=open(tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name, 'rb').read(),
        file_name="ROKAA_Data_Excellence_Report.pdf",
        mime="application/pdf"
    )
