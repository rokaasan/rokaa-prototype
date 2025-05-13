
import streamlit as st

def display_recommendations(scores, business_type, aspirations):
    st.subheader("💡 Strategic Recommendations")
    st.markdown("These targeted actions are based on your maturity assessment and aspirations:")

    recs = []

    if scores["Governance"] < 3:
        recs.append({
            "area": "Data Governance",
            "action": "Establish a governance framework and assign data stewards.",
            "why": "This improves accountability and enables trusted data use."
        })

    if scores["Management"] < 3:
        recs.append({
            "area": "Data Management",
            "action": "Implement centralised data storage and metadata management.",
            "why": "Boosts efficiency and enables AI-readiness."
        })

    if scores["Quality"] < 3:
        recs.append({
            "area": "Data Quality",
            "action": "Deploy automated quality checks and issue resolution workflows.",
            "why": "Reduces decision risk and increases confidence."
        })

    if "ai" in aspirations.lower():
        recs.append({
            "area": "AI Foundations",
            "action": "Prioritise structured data and clear lineage to enable AI projects.",
            "why": "Poor data foundations block meaningful AI adoption."
        })

    if business_type == "SME" and ("compliance" in aspirations.lower() or "scale" in aspirations.lower()):
        recs.append({
            "area": "Fractional Leadership",
            "action": "Engage a fractional Chief Data Officer (myCDO).",
            "why": "Helps guide strategic uplift without full-time overhead."
        })

    if not recs:
        st.success("You're performing strongly. We recommend exploring innovation tracks:")
        recs = [
            {
                "area": "Innovation",
                "action": "Adopt data product thinking and advanced analytics practices.",
                "why": "To extend value capture and differentiate competitively."
            }
        ]

    for rec in recs:
        st.markdown(f"### 🧭 {rec['area']}")
        st.markdown(f"- **What to do**: {rec['action']}")
        st.markdown(f"- **Why it matters**: {rec['why']}")
        st.markdown("---")
