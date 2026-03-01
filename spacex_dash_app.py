import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

spacex_df = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv"
)
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

app = Dash(__name__)

options = [{"label": "All Sites", "value": "ALL"}]
for site in spacex_df["Launch Site"].unique():
    options.append({"label": site, "value": site})

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="site-dropdown",
                    options=options,
                    value="ALL",
                    placeholder="Select a Launch Site here",
                    searchable=True,
                )
            ]
        ),
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        html.Div(
            [
                dcc.RangeSlider(
                    id="payload-slider",
                    min=0,
                    max=10000,
                    step=1000,
                    marks={
                        0: "0",
                        2500: "2500",
                        5000: "5000",
                        7500: "7500",
                        10000: "10000",
                    },
                    value=[min_payload, max_payload],
                )
            ]
        ),
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def get_pie_chart(entered_site):
    if entered_site == "ALL":
        fig = px.pie(
            spacex_df,
            values="class",
            names="Launch Site",
            title="Total Success Launches by Site",
        )
        return fig
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
        site_counts = filtered_df["class"].value_counts().reset_index()
        site_counts.columns = ["class", "count"]
        site_counts["outcome"] = site_counts["class"].map({1: "Success", 0: "Failure"})
        fig = px.pie(
            site_counts,
            values="count",
            names="outcome",
            title=f"Total Success Launches for site {entered_site}",
        )
        return fig


@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def get_scatter_chart(entered_site, payload_range):
    if payload_range is None:
        low, high = min_payload, max_payload
    else:
        low, high = payload_range

    mask = (spacex_df["Payload Mass (kg)"] >= low) & (
        spacex_df["Payload Mass (kg)"] <= high
    )
    filtered_df = spacex_df[mask]

    if entered_site == "ALL":
        return px.scatter(
            filtered_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version",
            title="Correlation between Payload and Success for all Sites",
        )
    else:
        site_df = filtered_df[filtered_df["Launch Site"] == entered_site]
        return px.scatter(
            site_df,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version",
            title=f"Correlation between Payload and Success for {entered_site}",
        )


if __name__ == "__main__":
    app.run(port=8050)
