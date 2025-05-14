
# ROKAA Data Excellence Prototype v5 - Full with Joey + Sector Logic
import streamlit as st
from radar_chart_component import display_radar_chart
from opportunities_component import display_opportunities
from risks_component import display_risks
from recommendations_component import display_recommendations
from training_component import display_training
from roadmap_component import display_roadmap

# Title and Joey Bot Sidebar
st.set_page_config(layout="wide")
st.title("Rokaa Data Excellence Appraisal")
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=60)
    st.markdown("### 🤖 Meet Joey the Bot")
    st.markdown("I'm here to guide you! As you answer questions, I’ll offer tips. At the end, I’ll help interpret your results.")

# Progress tracking
if "stage" not in st.session_state:
    st.session_state.stage = "kyc"

# Part A: KYC
if st.session_state.stage == "kyc":
    st.subheader("🧭 Part A: Understanding Your Business")
    business_name = st.text_input("Business Name")
    segment = st.selectbox("How would you describe your business?", ["StartUp", "SME", "Corporate"])
    sector = st.selectbox("Which sector best describes you?", ["Healthtech", "Fintech", "Other"])
    funding = st.radio("How are you funded?", ["Bootstrapped", "Seed/Angel", "VC", "Revenue-funded", "Government/Grant"])
    goals = st.text_area("What are your 3 biggest goals over the next 2 years?")
    improvement_areas = st.multiselect(
        "Which of the following ways to improve and leverage data would interest you in the next 12–24 months?",
        ["Improve data quality", "Get more value from data", "Support AI adoption", "Strengthen governance", "Drive innovation"]
    )
    if st.button("Next: Data Maturity Assessment"):
        st.session_state.kyc = {
            "business_name": business_name,
            "segment": segment,
            "sector": sector,
            "funding": funding,
            "goals": goals,
            "improvement_areas": improvement_areas
        }
        st.session_state.stage = "assessment"
        st.rerun()

# Part B: Maturity Assessment
elif st.session_state.stage == "assessment":
    st.subheader("📊 Part B: Data Maturity Assessment")
    st.markdown("Rate your organization's current practices:")

    gov = st.slider("Governance", 0, 5, 2)
    mgmt = st.slider("Management", 0, 5, 2)
    qual = st.slider("Quality", 0, 5, 2)

    if st.button("Submit Assessment"):
        st.session_state.scores = {
            "Governance": gov,
            "Management": mgmt,
            "Quality": qual
        }
        st.session_state.stage = "results"
        st.rerun()

# Part C: Results
elif st.session_state.stage == "results":
    st.subheader("🌟 Part C: Your Curated Journey")

    display_radar_chart(st.session_state.scores)

    st.markdown("---")
    display_opportunities(
        segment=st.session_state.kyc["segment"],
        sector=st.session_state.kyc["sector"],
        goals=st.session_state.kyc["goals"]
    )

    st.markdown("---")
    display_risks(
        segment=st.session_state.kyc["segment"],
        sector=st.session_state.kyc["sector"],
        scores=st.session_state.scores
    )

    st.markdown("---")
    display_recommendations(
        segment=st.session_state.kyc["segment"],
        sector=st.session_state.kyc["sector"],
        goals=st.session_state.kyc["goals"]
    )

    st.markdown("---")
    display_training(
        segment=st.session_state.kyc["segment"],
        sector=st.session_state.kyc["sector"],
        scores=st.session_state.scores
    )

    st.markdown("---")
    display_roadmap(
        segment=st.session_state.kyc["segment"],
        goals=st.session_state.kyc["goals"]
    )

    st.markdown("🔁 Want to do another appraisal?")
    if st.button("Start Again"):
        st.session_state.clear()
        st.rerun()
