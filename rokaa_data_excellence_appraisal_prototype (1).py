import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
import tempfile

# --- ROKAA Data Excellence Appraisal Prototype ---
st.set_page_config(page_title="ROKAA Assessment", layout="wide")

# --- Branding and Intro ---
st.title("Welcome to ROKAA")
st.subheader("Your data transformation journey starts here.")
st.write("Think of this like setting out on an exciting new adventure — with a trusted guide by your side.")

# --- Conversational Bot Sidebar ---
st.sidebar.header("Your ROKAA Guide 🤖")
bot_message = st.sidebar.text_input("Ask me anything:")
if bot_message:
    # Placeholder bot response logic
    st.sidebar.markdown(f"**Guide:** That’s a great question! I’m here to help you through each step.")

# --- Progress Indicator (Overall) ---
if not st.session_state.get("ready_for_assessment"):
    st.progress(20)
elif not st.session_state.get("assessment_submitted"):
    st.progress(60)
else:
    st.progress(100)

st.divider()

# --- Section B: KYC (Know Your Client) ---
st.header("Tell us about your business")
segment = st.selectbox(
    "Which best describes your organisation?",
    ["Startup", "SME", "Corporate"], key="segment"
)

company_name = st.text_input("What is your company name?", key="company_name")
industry = st.selectbox(
    "Which industry best describes your business?",
    ["HealthTech", "FinTech", "B2B SaaS", "Climate-Tech", "EdTech", "Other"], key="industry"
)
years_operating = st.number_input(
    "How many years has your company been operating?",
    min_value=0, max_value=100, value=0,
    help="Enter 0 if you’re pre-launch or just formed.", key="years_operating"
)

funding_status = st.radio(
    "What is your current funding status?",
    ["Self-funded / Bootstrapped", "Pre-seed / Seed", "Series A+", "Not sure"], key="funding_status"
)

markets = st.multiselect(
    "Which markets do you serve?",
    ["Australia","New Zealand","Asia-Pacific","North America","Europe","Latin America","Other"], key="markets"
)
challenges = st.text_area("What are the biggest challenges you’re facing right now?", key="challenges")
goals = st.text_area("What do you hope to achieve in the next 12–24 months?", key="goals")

st.success(f"You are a **{segment}** operating for **{years_operating}** years, currently **{funding_status}**.")
st.divider()

# --- Proceed to Assessment ---
if st.button("Next: Begin Assessment"):
    st.session_state["ready_for_assessment"] = True
    st.rerund()

# --- Section C: Data Maturity Assessment Questions ---
if st.session_state.get("ready_for_assessment"):
    st.header("Data Maturity Assessment")
    # Data Governance Section
    st.subheader("Section 1: Data Governance")
    dg1 = st.radio("Do you have a formal data governance policy?", ["Yes","No","In Progress"], key="dg1")
    dg2 = st.radio("Is there a data owner or steward responsible for governance?", ["Yes","No","Not Sure"], key="dg2")
    # Data Quality Section
    st.subheader("Section 2: Data Quality")
    dq1 = st.radio("Do you monitor the quality of your critical data sets?", ["Yes","No","Somewhat"], key="dq1")
    dq2 = st.radio("Are there automated checks in place for data accuracy/completeness?", ["Yes","No","In Progress"], key="dq2")
    # Metadata Management Section
    st.subheader("Section 3: Metadata Management")
    mm1 = st.radio("Do you maintain a business glossary or data catalog?", ["Yes","No","Partially"], key="mm1")
    mm2 = st.radio("Is metadata captured and managed across systems?", ["Yes","No","Not Sure"], key="mm2")

    # Submission and Scoring
    if st.button("Submit Assessment"):
        st.session_state["assessment_submitted"] = True
        score_map = {"Yes":2, "No":0, "In Progress":1, "Not Sure":0, "Somewhat":1, "Partially":1}
        dg_score = (score_map[st.session_state['dg1']] + score_map[st.session_state['dg2']]) / 4 * 100
        dq_score = (score_map[st.session_state['dq1']] + score_map[st.session_state['dq2']]) / 4 * 100
        mm_score = (score_map[st.session_state['mm1']] + score_map[st.session_state['mm2']]) / 4 * 100
        st.success("✅ Assessment submitted. Generating your personalized dashboard and report...")
        # Display Scores
        st.subheader("Your Data Maturity Scores (%)")
        st.write(f"**Data Governance:** {dg_score:.0f}%")
        st.write(f"**Data Quality:** {dq_score:.0f}%")
        st.write(f"**Metadata Management:** {mm_score:.0f}%")
        # Radar Chart
        categories = ["Data Governance","Data Quality","Metadata Management"]
        values = [dg_score, dq_score, mm_score]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=values + [values[0]], theta=categories + [categories[0]], fill='toself', name='Your Score'))
        fig.update_layout(polar=dict(radialaxis=dict(range=[0,100])), showlegend=False)
        st.plotly_chart(fig)
        # PDF Report Generation
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial","B",16)
        pdf.cell(0,10,"ROKAA Data Excellence Appraisal Prototype",ln=True)
        pdf.set_font("Arial","",12)
        pdf.cell(0,10,f"Segment: {segment}",ln=True)
        pdf.cell(0,10,f"Governance: {dg_score:.0f}%",ln=True)
        pdf.cell(0,10,f"Quality: {dq_score:.0f}%",ln=True)
        pdf.cell(0,10,f"Metadata: {mm_score:.0f}%",ln=True)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf.output(tmp.name)
        st.download_button("Download Report (PDF)", data=open(tmp.name, 'rb').read(), file_name="ROKAA_Report.pdf", mime="application/pdf")
