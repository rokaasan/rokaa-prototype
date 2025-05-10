
import streamlit as st

st.set_page_config(page_title="Rokaa Data Excellence Prototype v3", layout="wide")

st.title("Rokaa Data Excellence Appraisal")
st.subheader("Help us understand a little about your business")

# --- KYC SECTION: BUSINESS CONTEXT ---

# Business Name
business_name = st.text_input("Business Name")
st.session_state["business_name"] = business_name

# Business Segment
business_type = st.selectbox(
    "How would you describe your business?",
    options=["StartUp", "SME", "Corporate", "Other"]
)
st.session_state["business_type"] = business_type

# Markets Served (for compliance logic, e.g. GDPR if 'Europe' selected)
markets_served = st.multiselect(
    "Which markets do you serve?",
    options=["Australia", "New Zealand", "Latin America", "North America", "Europe"]
)
st.session_state["markets_served"] = markets_served

# Funding Stage (used to tailor recommendations, ambition level, etc.)
funding_stage = st.selectbox(
    "How are you funded?",
    options=["Bootstrapped", "Pre-seed", "Seed", "Series A", "Series B+", "Grant-funded", "Revenue-funded"]
)
st.session_state["funding_stage"] = funding_stage

# Operating Duration (used for maturity curve logic)
years_operating = st.selectbox(
    "How long have you been operating?",
    options=["Less than 1 year", "1–2 years", "2–5 years", "5+ years"]
)
st.session_state["years_operating"] = years_operating

# Business Challenges (used for opportunity/rec targeting)
business_challenges = st.text_area("What are the biggest challenges facing your business at the moment?")
st.session_state["business_challenges"] = business_challenges

# Aspirations for Data/AI Uplift
aspirations = st.text_area(
    "What would you like to be doing over the next 12–24 months that better leverages your data, analytics and AI?"
)
st.session_state["aspirations"] = aspirations

# Placeholder for moving to the next section (e.g., assessment)
if st.button("Continue to Assessment"):
    st.success("Proceeding to next section... (placeholder)")
