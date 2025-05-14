
import streamlit as st
import plotly.graph_objects as go

def display_radar_chart(scores, peer_scores, asp_scores):
    categories = list(scores.keys())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=categories,
        fill='toself',
        name='Your Scores',
        line_color='blue'
    ))

    fig.add_trace(go.Scatterpolar(
        r=list(peer_scores.values()),
        theta=categories,
        fill='toself',
        name='Peer Benchmark',
        line_color='orange'
    ))

    fig.add_trace(go.Scatterpolar(
        r=list(asp_scores.values()),
        theta=categories,
        fill='toself',
        name='Your Aspiration',
        line_color='green'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )
        ),
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)
