# ==========================================================
# AI Resume Screening System
# Visualization Module
# ==========================================================

import plotly.graph_objects as go
import plotly.express as px


def _apply_dashboard_style(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#393530"},
        title_font={"color": "#4D3526"},
        margin={"t": 55, "r": 20, "b": 45, "l": 45},
    )
    fig.update_xaxes(
        color="#62584E",
        gridcolor="#E6DCCB",
        zerolinecolor="#E6DCCB",
    )
    fig.update_yaxes(
        color="#62584E",
        gridcolor="#E6DCCB",
        zerolinecolor="#E6DCCB",
    )
    return fig


# ==========================================================
# ATS Score Gauge Chart
# ==========================================================

def ats_gauge_chart(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "ATS Score",
                "font": {"color": "#4D3526"},
            },
            number={"font": {"color": "#B86E4B"}},
            gauge={
                "axis": {
                    "range": [
                        0,
                        100
                    ],
                    "tickcolor": "#62584E",
                },
                "bar": {"color": "#B86E4B", "thickness": 0.25},
                "bgcolor": "#F0E5D2",
                "bordercolor": "#DED0B8",
                "steps": [
                    {
                        "range": [
                            0,
                            50
                        ],
                        "color": "#f4d7d2"
                    },
                    {
                        "range": [
                            50,
                            75
                        ],
                        "color": "#f4ebce"
                    },
                    {
                        "range": [
                            75,
                            100
                        ],
                        "color": "#EADBBE"
                    }
                ]
            }
        )
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#393530"},
        margin={"t": 40, "r": 25, "b": 20, "l": 25},
    )

    return fig


# ==========================================================
# Skill Match Pie Chart
# ==========================================================

def skill_match_chart(
        matched,
        missing
):
    labels = [
        "Matched Skills",
        "Missing Skills"
    ]

    values = [
        len(matched),
        len(missing)
    ]

    fig = px.pie(
        names=labels,
        values=values,
        title="Skill Match Analysis",
        color_discrete_sequence=["#C49A58", "#B86E4B"],
    )

    fig.update_traces(
        hole=0.48,
        marker={"line": {"color": "#f7f0df", "width": 3}},
    )

    return _apply_dashboard_style(fig)


# ==========================================================
# Skill Category Bar Chart
# ==========================================================

def skill_category_chart(categories):
    category_names = list(
        categories.keys()
    )

    counts = [
        len(value)
        for value in categories.values()
    ]

    fig = px.bar(
        x=category_names,
        y=counts,
        labels={
            "x": "Skill Category",
            "y": "Number of Skills"
        },
        title="Skills Distribution",
        color_discrete_sequence=["#C49A58"],
    )

    return _apply_dashboard_style(fig)


# ==========================================================
# ATS Component Score Chart
# ==========================================================

def ats_component_chart(scores):
    components = [
        key
        for key in scores.keys()
        if key != "ATS Score"
    ]

    values = [
        scores[key]
        for key in components
    ]

    fig = px.bar(
        x=components,
        y=values,
        title="ATS Score Breakdown",
        labels={
            "x": "Evaluation Factor",
            "y": "Score"
        },
        color_discrete_sequence=["#B86E4B"],
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    return _apply_dashboard_style(fig)
