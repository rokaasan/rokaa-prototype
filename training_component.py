
import streamlit as st

def display_training_recommendations(scores, business_type):
    st.subheader("📚 Training & Literacy Uplift")
    st.markdown("To close key gaps and uplift literacy, ROKAA recommends:")

    # Executive recommendations
    if scores["Governance"] < 3:
        st.markdown("**Governance & Compliance (Executive)**")
        st.write("- ROKAA Microcourse: 'Foundations of Data Governance'")
        st.write("- External: 'Data Management Fundamentals' (DAMA Certification)")

    if scores["Management"] < 3:
        st.markdown("**Data Management Strategy (Executive)**")
        st.write("- ROKAA Briefing: 'Aligning Data Management with Business Value'")
        st.write("- Suggested: 'CDMP Prep Series – Strategy & Planning Module'")

    if scores["Quality"] < 3:
        st.markdown("**Data Quality Literacy (Executive)**")
        st.write("- ROKAA MiniCourse: 'Executive’s Guide to Data Quality ROI'")
        st.write("- Optional: 'Data Quality Concepts' (LinkedIn Learning)")

    # Team/Operational recommendations
    if scores["Governance"] < 3:
        st.markdown("**Governance Practices (Team)**")
        st.write("- ROKAA Microcourse: 'Role-based Data Ownership'")
        st.write("- Optional: 'Creating Data Stewardship Playbooks'")

    if scores["Quality"] < 3:
        st.markdown("**Operational Data Quality (Team)**")
        st.write("- ROKAA Microcourse: 'Data Quality 101'")
        st.write("- External: 'Practical Data Cleaning in Python' (Coursera)")

    if "ai" in business_type.lower() or "StartUp" in business_type:
        st.markdown("**AI Readiness & Literacy (Mixed)**")
        st.write("- ROKAA Workshop: 'AI Readiness for Leaders'")
        st.write("- External: 'AI for Everyone' by Andrew Ng (Coursera)")

    if all(v >= 3 for v in scores.values()):
        st.success("Strong baseline literacy detected! You may explore advanced leadership series or tailored domain training.")
