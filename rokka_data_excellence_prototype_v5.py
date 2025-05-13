
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if st.button("🔄 Start Again"):
    st.session_state.clear()
    st.experimental_rerun()

st.title("ROKAA Data Excellence Appraisal")
st.markdown("An interactive journey to assess and uplift your data, analytics, and AI readiness.")

# ------------------ Part A ------------------
st.header("🔍 Part A – Understanding Your Business")

business_type = st.selectbox("How would you describe your business?", ["StartUp", "SME", "Corporate", "Other"])
sector = st.selectbox("Which sector best describes your business?", ["Healthtech", "Fintech", "Edtech", "Retail", "Other"])
markets_served = st.multiselect("Which markets do you serve?", ["Australia", "New Zealand", "Latin America", "North America", "Europe"])
funding_stage = st.selectbox("How are you funded?", ["Bootstrapped", "Pre-seed", "Seed", "Series A", "Series B+", "Grant-funded", "Revenue-funded"])
years_operating = st.selectbox("How long have you been operating?", ["< 1 year", "1–2 years", "2–5 years", "5+ years"])
challenges = st.text_area("What are the biggest challenges facing your business at the moment?")
goals = st.multiselect("What are your 3 biggest goals over the next 2 years?", [
    "Build trust in data", "Automate compliance", "Enable self-service analytics",
    "Use AI responsibly", "Accelerate reporting", "Scale operations", "Other"
])
aspirations = st.multiselect("Which of the following ways to improve and leverage data would interest you in the next 12–24 months?", [
    "Build a modern data stack", "Improve data quality", "Get leadership insights faster",
    "Make analytics accessible to teams", "Automate compliance reporting", "Embed AI in daily decisions"
])

# ------------------ Part B ------------------
st.header("📊 Part B – Data Maturity Assessment")

def assess(label, key):
    return st.radio(label, [
        "1 - Not in place", "2 - Ad hoc", "3 - Emerging", "4 - Established", "5 - Optimised"
    ], index=2, key=key, horizontal=True)

st.subheader("Data Governance")
gov1 = assess("We have defined roles and responsibilities for data governance.", "gov1")
gov2 = assess("We have policies or guidelines to manage data quality, access, or lifecycle.", "gov2")

st.subheader("Data Management")
mgmt1 = assess("Our data is stored in a structured, accessible format.", "mgmt1")
mgmt2 = assess("We manage metadata, master data, or data lineage formally.", "mgmt2")

st.subheader("Data Quality")
dq1 = assess("We identify and correct data errors or inconsistencies regularly.", "dq1")
dq2 = assess("We measure and monitor data quality for key business data.", "dq2")

# Convert answers to numeric scores
def to_score(val):
    return int(val[0]) if val else 0

scores = {
    "Governance": (to_score(gov1) + to_score(gov2)) / 2,
    "Management": (to_score(mgmt1) + to_score(mgmt2)) / 2,
    "Quality": (to_score(dq1) + to_score(dq2)) / 2
}

peer_scores = {"Governance": 4, "Management": 3.5, "Quality": 4}
asp_scores = {k: 4.5 for k in scores}

# Radar Chart
st.subheader("📈 Maturity Radar")
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=list(scores.values()), theta=list(scores.keys()), fill='toself', name='Your Score'))
fig.add_trace(go.Scatterpolar(r=list(peer_scores.values()), theta=list(peer_scores.keys()), fill='toself', name='Peer Benchmark'))
fig.add_trace(go.Scatterpolar(r=list(asp_scores.values()), theta=list(asp_scores.keys()), fill='toself', name='Aspirational Goal'))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,5])), showlegend=True)
st.plotly_chart(fig, use_container_width=True)

# Submit button
if not st.session_state.submitted:
    if st.button("📩 Submit Assessment"):
        st.session_state.submitted = True
        st.experimental_rerun()
    st.stop()

# ------------------ Part C ------------------
st.header("🎯 Part C – Your Curated Journey")

# Opportunities
st.subheader("🌟 Opportunities")
if scores["Governance"] < 3:
    st.markdown("🔍 **Establish foundational data governance** to manage risk and build trust.")
if scores["Management"] < 3:
    st.markdown("⚙️ **Modernize your data management** to improve efficiency.")
if scores["Quality"] < 3:
    st.markdown("🧹 **Invest in data quality tools** to improve decision confidence.")
if "ai" in " ".join(aspirations).lower():
    st.markdown("🤖 **Get AI-ready** by structuring your data assets.")

# Risks
st.subheader("⚠️ Risks")
if scores["Governance"] < 2.5:
    st.markdown("- **Weak governance** may expose you to compliance and audit risks.")
if scores["Management"] < 2.5:
    st.markdown("- **Poor metadata** will reduce data discoverability and trust.")
if scores["Quality"] < 2.5:
    st.markdown("- **Low quality data** creates decision-making blind spots.")

# Recommendations
st.subheader("💡 Strategic Recommendations")
if scores["Governance"] < 3:
    st.markdown("- Assign data owners and establish clear roles.")
if scores["Quality"] < 3:
    st.markdown("- Implement automated data quality checks.")
if business_type == "SME" and ("ai" in " ".join(aspirations).lower() or "scale" in " ".join(goals).lower()):
    st.markdown("- Consider engaging a **fractional Chief Data Officer (myCDO)** for scalable leadership.")

# Training
st.subheader("📚 Training & Literacy")
if scores["Governance"] < 3:
    st.markdown("- ROKAA Microcourse: *Foundations of Data Governance*")
if scores["Management"] < 3:
    st.markdown("- ROKAA Briefing: *Metadata Management Made Easy*")
if scores["Quality"] < 3:
    st.markdown("- ROKAA Microcourse: *Data Quality 101*")
st.markdown("- Executive Workshop: *AI Readiness for Leaders*")

# Roadmap
st.subheader("🗺️ Roadmap: Next 12–18 Months")
roadmap = {
    "0–3 Months": ["Assign data stewards", "Kickoff literacy program"],
    "4–9 Months": ["Centralize data platform", "Deploy data quality monitoring"],
    "10–18 Months": ["Enable self-service BI", "Launch AI pilot"]
}
for phase, items in roadmap.items():
    st.markdown(f"### {phase}")
    for item in items:
        st.markdown(f"- {item}")
