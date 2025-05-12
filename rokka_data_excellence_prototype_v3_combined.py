
import streamlit as st

st.set_page_config(page_title="Rokaa Data Excellence Appraisal", layout="wide")
st.title("Rokaa Data Excellence Appraisal")
st.subheader("Help us understand a little about your business")

# --- KYC SECTION ---
business_name = st.text_input("Business Name")
st.session_state["business_name"] = business_name

business_type = st.selectbox("How would you describe your business?", ["StartUp", "SME", "Corporate", "Other"])
st.session_state["business_type"] = business_type

markets_served = st.multiselect("Which markets do you serve?", ["Australia", "New Zealand", "Latin America", "North America", "Europe"])
st.session_state["markets_served"] = markets_served

funding_stage = st.selectbox("How are you funded?", ["Bootstrapped", "Pre-seed", "Seed", "Series A", "Series B+", "Grant-funded", "Revenue-funded"])
st.session_state["funding_stage"] = funding_stage

years_operating = st.selectbox("How long have you been operating?", ["Less than 1 year", "1–2 years", "2–5 years", "5+ years"])
st.session_state["years_operating"] = years_operating

business_challenges = st.text_area("What are the biggest challenges facing your business at the moment?")
st.session_state["business_challenges"] = business_challenges

aspirations = st.text_area("What would you like to be doing over the next 12–24 months that better leverages your data, analytics and AI?")
st.session_state["aspirations"] = aspirations

# --- ASSESSMENT SECTION ---
st.subheader("Your Data Maturity Assessment")

st.markdown("Please assess your organisation’s current level of maturity across the following dimensions.")

def assessment_question(label, key):
    return st.radio(
        label,
        ["1 - Not in place", "2 - Ad hoc", "3 - Emerging", "4 - Established", "5 - Optimised"],
        index=2,
        key=key,
        horizontal=True
    )

# Governance
st.markdown("### Data Governance")
gov1 = assessment_question("We have defined roles and responsibilities for data governance.", "gov1")
gov2 = assessment_question("We have policies or guidelines to manage data quality, access, or lifecycle.", "gov2")

# Management
st.markdown("### Data Management")
mgmt1 = assessment_question("Our data is stored in a structured, accessible format.", "mgmt1")
mgmt2 = assessment_question("We manage metadata, master data, or data lineage in a formalised way.", "mgmt2")

# Quality
st.markdown("### Data Quality")
dq1 = assessment_question("We have processes to identify and correct data errors or inconsistencies.", "dq1")
dq2 = assessment_question("We measure and monitor the quality of our key business data.", "dq2")

# Store scores for later use
st.session_state["scores"] = {
    "governance": [gov1, gov2],
    "management": [mgmt1, mgmt2],
    "quality": [dq1, dq2]
}

if st.button("Continue to Opportunities & Risks"):
    st.success("Next module loading... (placeholder)")
