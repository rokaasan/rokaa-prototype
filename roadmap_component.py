
import streamlit as st
import pandas as pd
import plotly.express as px

def display_roadmap():
    st.subheader("🗺️ 12–18 Month Roadmap")
    st.markdown("Here's a tailored plan based on your assessment and goals:")

    # Written Summary
    st.markdown("### 📋 Summary")
    st.markdown("""
This roadmap includes quick wins and longer-term initiatives to uplift your data capability.  
It’s designed to match your current maturity while helping close key gaps.
    """)

    # Roadmap Table
    roadmap_data = {
        "Phase": ["0–3 Months", "0–3 Months", "4–9 Months", "4–9 Months", "10–18 Months", "10–18 Months"],
        "Focus Area": ["Assign Data Stewards", "Run Training on Data Roles",
                       "Implement Data Quality Monitoring", "Create Central Data Hub",
                       "Enable Self-Service BI", "Launch AI Use Cases"]
    }

    df = pd.DataFrame(roadmap_data)

    st.markdown("### 📅 Timeline View")
    fig = px.timeline(df, x_start="Phase", x_end="Phase", y="Focus Area", color="Phase", title="Action Roadmap")
    fig.update_yaxes(autorange="reversed")  # Optional: shows first item at top
    st.plotly_chart(fig, use_container_width=True)
