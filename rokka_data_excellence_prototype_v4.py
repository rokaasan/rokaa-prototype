
import streamlit as st

st.set_page_config(page_title="ROKAA Data Excellence Appraisal", layout="wide")

st.title("ROKAA Data Excellence Appraisal")
st.markdown("This interactive appraisal helps you understand your current data maturity and explore tailored recommendations to uplift your data, analytics, and AI capabilities.")

# ------------------ Part A: Understanding Your Business ------------------
st.header("🔍 Part A – Understanding Your Business")

st.markdown("This helps us learn more about you and what you need.")

business_name = st.text_input("Business Name")
business_type = st.selectbox("How would you describe your business?", ["StartUp", "SME", "Corporate", "Other"])
markets_served = st.multiselect("Which markets do you serve?", ["Australia", "New Zealand", "Latin America", "North America", "Europe"])
funding_stage = st.selectbox("How are you funded?", ["Bootstrapped", "Pre-seed", "Seed", "Series A", "Series B+", "Grant-funded", "Revenue-funded"])
years_operating = st.selectbox("How long have you been operating?", ["< 1 year", "1–2 years", "2–5 years", "5+ years"])
sector = st.selectbox("Which sector best describes your business?", ["Healthtech", "Fintech", "Edtech", "Retail", "Other"])
business_challenges = st.text_area("What are the biggest challenges facing your business at the moment?")
goals_2yr = st.text_area("What are your 3 biggest goals over the next 2 years?")
aspirational_focus = st.multiselect("What areas do you want to improve in the next 12–24 months?", [
    "Build a modern data stack",
    "Improve data quality",
    "Get leadership insights faster",
    "Make analytics accessible to teams",
    "Automate compliance reporting",
    "Embed AI in daily decisions"
])

# ------------------ Part B: Data Maturity Assessment ------------------
st.header("📊 Part B – Data Maturity Assessment")

st.markdown("Please assess your current maturity across each area:")

def assess(label, key):
    return st.radio(label, [
        "1 - Not in place", "2 - Ad hoc", "3 - Emerging", "4 - Established", "5 - Optimised"
    ], index=2, key=key, horizontal=True)

gov1 = assess("We have defined roles and responsibilities for data governance.", "gov1")
gov2 = assess("We have policies or guidelines to manage data quality, access, or lifecycle.", "gov2")
mgmt1 = assess("Our data is stored in a structured, accessible format.", "mgmt1")
mgmt2 = assess("We manage metadata, master data, or data lineage formally.", "mgmt2")
dq1 = assess("We identify and correct data errors or inconsistencies regularly.", "dq1")
dq2 = assess("We measure and monitor data quality for key business data.", "dq2")

# ------------------ Part C: Your Curated Journey ------------------
st.header("🎯 Part C – Your Curated Journey")

st.markdown("Based on your assessment and aspirations, here’s your tailored roadmap.")

# Placeholder for Opportunities, Risks, Recommendations, Roadmap, and Literacy
st.subheader("🔎 Opportunities")
st.info("Opportunities will be curated based on scores and goals.")

st.subheader("⚠️ Risks")
st.warning("Key risks will reflect gaps in maturity and regulatory pressure.")

st.subheader("💡 Strategic Recommendations")
st.success("Recommendations will include tools, practices, and advisory services like myCDO.")

st.subheader("📚 Training & Literacy Uplift")
st.markdown("To close the key gaps and uplift literacy, ROKAA recommends the following themes:")

st.markdown("**Governance & Compliance (Executive)**")
st.write("- ROKAA Microcourse: 'Foundations of Data Governance'")
st.write("- Suggested: 'Data Management Fundamentals' (DAMA Certification)")

st.markdown("**Operational Data Quality (Team)**")
st.write("- ROKAA Microcourse: 'Data Quality 101'")
st.write("- External: 'Practical Data Cleaning in Python' (Coursera)")

st.markdown("**AI Awareness (Executive)**")
st.write("- ROKAA Workshop: 'AI Readiness for Leaders'")
st.write("- Optional: 'AI for Everyone' by Andrew Ng (Coursera)")

st.markdown("**Analytics Enablement (Team)**")
st.write("- ROKAA Quickstart: 'How to build dashboards in 5 days'")
st.write("- External: 'Power BI Basics' (LinkedIn Learning)")

st.subheader("🗺️ Roadmap")
st.markdown("A visual and written summary of next steps will appear here.")
