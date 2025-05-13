
import plotly.graph_objects as go
import streamlit as st

def render_radar_chart(scores, peer_scores, asp_scores):
    categories = list(scores.keys())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=categories,
        fill='toself',
        name='Your Scores'
    ))

    fig.add_trace(go.Scatterpolar(
        r=list(peer_scores.values()),
        theta=categories,
        fill='toself',
        name='Peer Standard'
    ))

    fig.add_trace(go.Scatterpolar(
        r=list(asp_scores.values()),
        theta=categories,
        fill='toself',
        name='Aspirational Goal'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5])
        ),
        showlegend=True,
        title="Data Maturity Comparison"
    )

    st.plotly_chart(fig)
