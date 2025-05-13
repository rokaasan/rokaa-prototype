
import streamlit as st

def display_opportunities(scores, business_type, aspirations):
    st.subheader("🌟 Opportunities Ahead")
    st.markdown("Based on your assessment and goals, here are key opportunities to consider:")

    opportunities = []

    if scores["Governance"] < 3:
        opportunities.append("🔍 **Establish foundational data governance practices** to ensure data is trusted and properly managed.")
    if scores["Management"] < 3:
        opportunities.append("⚙️ **Improve data management workflows** to boost efficiency and consistency.")
    if scores["Quality"] < 3:
        opportunities.append("🧹 **Invest in data quality tools and literacy** to reduce errors and increase confidence in decision-making.")
    if business_type == "SME" and "growth" in aspirations.lower():
        opportunities.append("🚀 **Use analytics to scale operational insights** as your business expands.")
    if "ai" in aspirations.lower():
        opportunities.append("🤖 **Prepare for AI-readiness** by enhancing data structure and metadata practices.")

    if not opportunities:
        st.success("You're in great shape! But here are advanced opportunities:")
        opportunities.append("📈 Leverage predictive analytics to drive proactive decision-making.")
        opportunities.append("🔐 Explore privacy-by-design and ethical AI initiatives.")

    for opp in opportunities:
        st.markdown(opp)
