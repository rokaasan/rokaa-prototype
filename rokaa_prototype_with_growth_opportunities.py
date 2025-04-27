import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="ROKAA Assessment", layout="wide")

st.title("Welcome to ROKAA")
st.subheader("Your data transformation journey starts here.")
st.write("Think of this like setting out on an exciting new adventure — with a trusted guide by your side.")

st.sidebar.header("Meet Joey 🤖 — Your ROKAA Guide")
bot_question = st.sidebar.text_input("Ask Joey anything:")
if bot_question:
    bot_knowledge = {
        "data governance": "Data governance is how your business manages data availability, usability, integrity, and security.",
        "data quality": "Data quality is about ensuring data is accurate, complete, timely, and reliable for decision-making.",
        "metadata management": "Metadata management helps you understand what data you have, where it lives, and how it’s used."
    }
    response = next((ans for key, ans in bot_knowledge.items() if key in bot_question.lower()), 
                    "That’s a great question! I’ll flag this for deeper support in the future.")
    st.sidebar.markdown(f"**Joey:** {response}")

# --- Progress Bar ---
if not st.session_state.get("ready_for_assessment"):
    st.progress(20)
elif not st.session_state.get("assessment_submitted"):
    st.progress(60)
else:
    st.progress(100)

st.divider()

# --- Capture Basic KYC with safer session storage ---
st.header("Tell us about your business")

if "segment" not in st.session_state:
    st.session_state["segment"] = ""
if "industry" not in st.session_state:
    st.session_state["industry"] = ""

st.session_state["segment"] = st.selectbox("Which best describes your organisation?", ["Startup", "SME", "Corporate"], key="segment_select")
company_name = st.text_input("What is your company name?", key="company_name")
st.session_state["industry"] = st.selectbox("Which industry best describes your business?", ["HealthTech", "FinTech", "B2B SaaS", "Climate-Tech", "EdTech", "Other"], key="industry_select")
years_operating = st.number_input("How many years has your company been operating?", min_value=0, max_value=100, value=0, key="years_operating")
funding_status = st.radio("What is your current funding status?", ["Self-funded / Bootstrapped", "Pre-seed / Seed", "Series A+", "Not sure"], key="funding_status")
markets = st.multiselect("Which markets do you serve?", ["Australia", "New Zealand", "Asia-Pacific", "North America", "Europe", "Latin America", "Other"], key="markets")
challenges = st.text_area("What are the biggest challenges you’re facing right now?", key="challenges")
goals = st.text_area("What do you hope to achieve in the next 12–24 months?", key="goals")

st.success(f"You are a **{st.session_state['segment']}** operating for **{years_operating}** years, currently **{funding_status}**.")
st.divider()

if st.button("Next: Begin Assessment"):
    st.session_state["ready_for_assessment"] = True
    st.rerun()
if st.session_state.get("ready_for_assessment"):
    st.header("Data Maturity Assessment")

    st.subheader("Section 1: Data Governance")
    dg1 = st.radio("Do you have a formal data governance policy?", ["Yes", "No", "In Progress"], key="dg1")
    dg2 = st.radio("Is there a data owner or steward responsible for governance?", ["Yes", "No", "Not Sure"], key="dg2")

    st.subheader("Section 2: Data Quality")
    dq1 = st.radio("Do you monitor the quality of your critical data sets?", ["Yes", "No", "Somewhat"], key="dq1")
    dq2 = st.radio("Are there automated checks in place for data accuracy/completeness?", ["Yes", "No", "In Progress"], key="dq2")

    st.subheader("Section 3: Metadata Management")
    mm1 = st.radio("Do you maintain a business glossary or data catalog?", ["Yes", "No", "Partially"], key="mm1")
    mm2 = st.radio("Is metadata captured and managed across systems?", ["Yes", "No", "Not Sure"], key="mm2")

    st.subheader("Your Aspirations")
    asp_gov = st.slider("Desired future state for Data Governance", 0, 100, 70)
    asp_qual = st.slider("Desired future state for Data Quality", 0, 100, 70)
    asp_meta = st.slider("Desired future state for Metadata Management", 0, 100, 70)

    if st.button("Submit Assessment"):
        st.session_state["assessment_submitted"] = True
        score_map = {"Yes": 1.5, "No": 0, "In Progress": 1, "Not Sure": 0, "Somewhat": 1, "Partially": 1}
        dg_score = (score_map[dg1] + score_map[dg2]) / 3.0 * 80
        dq_score = (score_map[dq1] + score_map[dq2]) / 3.0 * 80
        mm_score = (score_map[mm1] + score_map[mm2]) / 3.0 * 80

        if st.session_state["segment"] == "Startup":
            baseline = [40, 35, 30]
        elif st.session_state["segment"] == "SME":
            baseline = [60, 55, 50]
        else:
            baseline = [75, 70, 65]

        st.subheader("Your Data Maturity Overview (%)")
        categories = ["Data Governance", "Data Quality", "Metadata Management"]
        user_values = [dg_score, dq_score, mm_score]
        aspirational = [asp_gov, asp_qual, asp_meta]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=baseline + [baseline[0]], theta=categories + [categories[0]], fill='none', name='Peer Baseline'))
        fig.add_trace(go.Scatterpolar(r=user_values + [user_values[0]], theta=categories + [categories[0]], fill='toself', name='Your Current Maturity'))
        fig.add_trace(go.Scatterpolar(r=aspirational + [aspirational[0]], theta=categories + [categories[0]], fill='toself', name='Your Aspirational Maturity'))
        fig.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), showlegend=True)
        st.plotly_chart(fig)

        # --- Opportunities for Business Growth ---
        st.subheader("Opportunities for Business Growth")

        industry_cases = {
            "HealthTech": [
                {"title": "📈 Patient Flow Optimization", "desc": "Streamline onboarding with standardized data models and centralized data catalogs.", "value": "Potential Value: Reduce admin time by 20% across care sites."},
                {"title": "⚙️ AI-Ready Data Infrastructure", "desc": "Governed, high-quality data enables ML-driven triage and virtual health.", "value": "Potential Value: Speed to MVP by 3–6 months."},
                {"title": "📊 Clinical Compliance Acceleration", "desc": "Automate regulatory reporting (e.g., for GDPR, HIPAA) with structured metadata.", "value": "Potential Value: Save $50K+ in audit and admin overhead."}
            ],
            "FinTech": [
                {"title": "💡 Customer Segmentation & Personalization", "desc": "Use trusted data to enable personalized product offers and retention models.", "value": "Potential Value: 15–30% lift in customer conversion."},
                {"title": "🔒 Risk & Fraud Detection", "desc": "Improve fraud detection accuracy with consistent metadata and training data.", "value": "Potential Value: $100K+ in fraud mitigation annually."}
            ]
        }

        industry_selected = st.session_state["industry"]
        st.write(f"DEBUG: You selected industry = {industry_selected}")  # (Temporary debug helper)

        if industry_selected in industry_cases:
            for case in industry_cases[industry_selected][:3]:
                st.markdown(f"**{case['title']}**  \n{case['desc']}  \n*{case['value']}*  \n")
        else:
            st.info("We’ll tailor growth opportunities as we learn more about your industry.")
        # --- Key Risks Identified ---
        st.subheader("Key Risks Identified")

        risks = []

        if "Europe" in markets or "North America" in markets:
            if dg_score < 60:
                risks.append("⚠️ *Regulatory Exposure*: You're operating in international markets but lack strong data governance.\n**Why this matters:** Regulations like GDPR and CCPA carry significant penalties and reputational risks.")

        if dq_score < 50:
            risks.append("⚠️ *Poor Data Quality*: Inadequate checks on critical data.\n**Why this matters:** Poor data quality leads to bad decisions, customer dissatisfaction, and limits automation or AI effectiveness.")

        if mm_score < 50:
            risks.append("⚠️ *Metadata Gaps*: Weak or missing metadata practices.\n**Why this matters:** Without metadata, teams waste time finding, understanding, and revalidating data.")

        if "ai" in goals.lower() or "machine learning" in goals.lower():
            if dq_score < 60 or dg_score < 60:
                risks.append("⚠️ *AI Risk*: AI/ML ambitions with insufficient data maturity.\n**Why this matters:** Poor data foundations will lead to unreliable models, biased outcomes, and operational inefficiencies.")

        if st.session_state["segment"] == "Startup" and dg_score < 40:
            risks.append("⚠️ *Foundational Risk*: Low governance in early-stage company.\n**Why this matters:** Startups that neglect data structure early face scalability issues and trust breakdowns later.")

        if risks:
            for r in risks:
                st.warning(r)
        else:
            st.success("✅ No major data risks identified — great foundation to build on!")

        # --- PDF Report Summary ---
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "ROKAA Data Excellence Appraisal Prototype", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Segment: {st.session_state['segment']}", ln=True)
        pdf.cell(0, 10, f"Governance Score: {dg_score:.0f}%", ln=True)
        pdf.cell(0, 10, f"Quality Score: {dq_score:.0f}%", ln=True)
        pdf.cell(0, 10, f"Metadata Score: {mm_score:.0f}%", ln=True)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf.output(tmp.name)
        st.download_button("Download Report (PDF)", data=open(tmp.name, 'rb').read(), file_name="ROKAA_Report.pdf", mime="application/pdf")

