
import streamlit as st

def display_risks_component(session_data):
    st.subheader("⚠️ Risks")
    st.markdown("Below are key risks identified based on your data maturity and business profile:")

    risks = []

    segment = session_data.get("business_type", "Other")
    governance = session_data.get("scores", {}).get("Governance", 0)
    management = session_data.get("scores", {}).get("Management", 0)
    quality = session_data.get("scores", {}).get("Quality", 0)

    if governance < 2.5:
        risks.append({
            "title": "Weak Data Governance",
            "impact": "Increased compliance risks and lack of clarity on data ownership.",
            "roi": "Improving governance can reduce regulatory exposure and improve decision-making confidence."
        })

    if management < 2.5:
        risks.append({
            "title": "Limited Data Management Processes",
            "impact": "Poor data discoverability and inefficient operations.",
            "roi": "Better management enables scalability and faster access to insights."
        })

    if quality < 2.5:
        risks.append({
            "title": "Inconsistent Data Quality",
            "impact": "Lack of trust in reporting and analytics.",
            "roi": "Enhancing quality improves operational performance and stakeholder confidence."
        })

    if segment == "StartUp" and governance < 3:
        risks.append({
            "title": "Insufficient Foundations for Growth",
            "impact": "You may struggle to scale or meet partner/investor expectations.",
            "roi": "Addressing early gaps ensures smoother growth and faster onboarding of new systems."
        })

    if not risks:
        st.success("No major risks identified based on your current responses.")
    else:
        for risk in risks:
            st.markdown(f"### 🔸 {risk['title']}")
            st.markdown(f"- **Business Impact**: {risk['impact']}")
            st.markdown(f"- **Why it matters**: {risk['roi']}")
            st.markdown("---")
