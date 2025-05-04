import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="ROKAA Data Excellence Appraisal", layout="wide")
# Initialize session state for assessment submission
if "assessment_submitted" not in st.session_state:
    st.session_state["assessment_submitted"] = False

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

# Progress bar
if not st.session_state.get("ready_for_assessment"):
    st.progress(20)
elif not st.session_state.get("assessment_submitted"):
    st.progress(60)
else:
    st.progress(100)

st.divider()

# ---------------- KYC ---------------- #
st.header("Tell us about your business")

if "segment" not in st.session_state:
    st.session_state["segment"] = ""
if "industry" not in st.session_state:
    st.session_state["industry"] = ""

st.session_state["segment"] = st.selectbox(
    "Which best describes your organisation?",
    ["Startup", "SME", "Corporate"],
    key="segment_select"
)

company_name = st.text_input("What is your company name?", key="company_name")

st.session_state["industry"] = st.selectbox(
    "Which industry best describes your business?",
    ["HealthTech", "FinTech", "B2B SaaS", "ClimateTech", "EdTech", "Other"],
    key="industry_select"
)

years_operating = st.number_input(
    "How many years has your company been operating?",
    min_value=0, max_value=100,
    value=0,
    key="years_operating"
)

funding_status = st.radio(
    "What is your current funding status?",
    ["Self-funded / Bootstrapped", "Pre-seed / Seed", "Series A+", "Not sure"],
    key="funding_status"
)

markets = st.multiselect(
    "Which markets do you serve?",
    ["Australia", "New Zealand", "Asia-Pacific", "North America", "Europe", "Latin America", "Other"],
    key="markets"
)

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

    score_map = {"Yes": 2, "No": 0, "In Progress": 1, "Not Sure": 0, "Somewhat": 1, "Partially": 1}

    if st.button("Submit Assessment"):
        st.session_state["assessment_submitted"] = True
        st.session_state["dg_score"] = (score_map[dg1] + score_map[dg2]) / 4.0 * 100
        st.session_state["dq_score"] = (score_map[dq1] + score_map[dq2]) / 4.0 * 100
        st.session_state["mm_score"] = (score_map[mm1] + score_map[mm2]) / 4.0 * 100
        st.session_state["asp_gov"] = asp_gov
        st.session_state["asp_qual"] = asp_qual
        st.session_state["asp_meta"] = asp_meta
        st.rerun()

# --- Final Output and Insights ---
if st.session_state.get("assessment_submitted") and st.session_state.get("scores_calculated"):

    # Radar Chart
    fig = create_radar_chart(
        st.session_state.get("dg_score"),
        st.session_state.get("dq_score"),
        st.session_state.get("mm_score"),
        st.session_state.get("aspirational_scores"),
        st.session_state.get("peer_scores")
    )
    st.plotly_chart(fig, use_container_width=True)

    # Opportunities and Risks
    st.markdown("⬇️ Below are opportunities and risks based on your data maturity profile:")

    # --- Business Growth Opportunities ---
    st.subheader("Opportunities for Business Growth")
    for opp in st.session_state.get("growth_opportunities", []):
        st.markdown(f"### {opp['icon']} {opp['title']}")
        st.markdown(opp['description'])
        st.markdown(f"*Potential Value: {opp['value']}*")

    # --- Risks to Consider ---
    st.subheader("Risks to Consider")
    for risk in st.session_state.get("risks", []):
        st.markdown(f"### {risk['icon']} {risk['title']}")
        st.markdown(risk['description'])
        st.markdown(f"*Risk Level: {risk['level']}*")

    st.download_button(
        label="📄 Download Appraisal Report (PDF)",
        data=open(tmp.name, 'rb').read(),
        file_name="ROKAA_Data_Excellence_Appraisal.pdf",
        mime="application/pdf"
    )
       
