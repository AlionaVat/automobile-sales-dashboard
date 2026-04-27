#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv"
)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"

# Dropdown options
dropdown_options = [
    {"label": "Yearly Statistics", "value": "Yearly Statistics"},
    {"label": "Recession Period Statistics", "value": "Recession Period Statistics"}
]

# Year list
year_list = [i for i in range(1980, 2024)]

# App layout
app.layout = html.Div([
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={
            "textAlign": "center",
            "color": "#503D36",
            "font-size": 24
        }
    ),

    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id="dropdown-statistics",
            options=dropdown_options,
            value="Yearly Statistics",
            placeholder="Select Statistics"
        )
    ]),

    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id="select-year",
            options=[{"label": i, "value": i} for i in year_list],
            value=1980,
            placeholder="Select Year"
        )
    ]),

    html.Div(
        id="output-container",
        className="chart-grid",
        style={"display": "flex", "flexDirection": "column"}
    )
])


# Enable/disable year dropdown
@app.callback(
    Output("select-year", "disabled"),
    Input("dropdown-statistics", "value")
)
def update_input_container(selected_statistics):
    if selected_statistics == "Yearly Statistics":
        return False
    else:
        return True


# Update charts
@app.callback(
    Output("output-container", "children"),
    [
        Input("dropdown-statistics", "value"),
        Input("select-year", "value")
    ]
)
def update_output_container(selected_statistics, input_year):

    if selected_statistics == "Recession Period Statistics":
        recession_data = data[data["Recession"] == 1]

        # Plot 1
        yearly_rec = recession_data.groupby("Year")["Automobile_Sales"].mean().reset_index()

        R_chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x="Year",
                y="Automobile_Sales",
                title="Average Automobile Sales fluctuation over Recession Period"
            )
        )

        # Plot 2
        average_sales = recession_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()

        R_chart2 = dcc.Graph(
            figure=px.bar(
                average_sales,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title="Average Number of Vehicles Sold by Vehicle Type"
            )
        )

        # Plot 3
        exp_rec = recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()

        R_chart3 = dcc.Graph(
            figure=px.pie(
                exp_rec,
                values="Advertising_Expenditure",
                names="Vehicle_Type",
                title="Total Advertising Expenditure Share by Vehicle Type During Recessions"
            )
        )

        # Plot 4
        unemp_data = recession_data.groupby(
            ["unemployment_rate", "Vehicle_Type"]
        )["Automobile_Sales"].mean().reset_index()

        R_chart4 = dcc.Graph(
            figure=px.bar(
                unemp_data,
                x="unemployment_rate",
                y="Automobile_Sales",
                color="Vehicle_Type",
                labels={
                    "unemployment_rate": "Unemployment Rate",
                    "Automobile_Sales": "Average Automobile Sales"
                },
                title="Effect of Unemployment Rate on Vehicle Type and Sales"
            )
        )

        return [
            html.Div(
                className="chart-item",
                children=[html.Div(R_chart1), html.Div(R_chart2)],
                style={"display": "flex"}
            ),
            html.Div(
                className="chart-item",
                children=[html.Div(R_chart3), html.Div(R_chart4)],
                style={"display": "flex"}
            )
        ]

    elif selected_statistics == "Yearly Statistics" and input_year:
        yearly_data = data[data["Year"] == input_year]

        # Plot 1
        yas = data.groupby("Year")["Automobile_Sales"].mean().reset_index()

        Y_chart1 = dcc.Graph(
            figure=px.line(
                yas,
                x="Year",
                y="Automobile_Sales",
                title="Yearly Automobile Sales"
            )
        )

        # Plot 2
        mas = yearly_data.groupby("Month")["Automobile_Sales"].sum().reset_index()

        Y_chart2 = dcc.Graph(
            figure=px.line(
                mas,
                x="Month",
                y="Automobile_Sales",
                title="Total Monthly Automobile Sales"
            )
        )

        # Plot 3
        avr_vdata = yearly_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()

        Y_chart3 = dcc.Graph(
            figure=px.bar(
                avr_vdata,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title=f"Average Vehicles Sold by Vehicle Type in the year {input_year}"
            )
        )

        # Plot 4
        exp_data = yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()

        Y_chart4 = dcc.Graph(
            figure=px.pie(
                exp_data,
                values="Advertising_Expenditure",
                names="Vehicle_Type",
                title="Total Advertisement Expenditure for Each Vehicle"
            )
        )

        return [
            html.Div(
                className="chart-item",
                children=[html.Div(Y_chart1), html.Div(Y_chart2)],
                style={"display": "flex"}
            ),
            html.Div(
                className="chart-item",
                children=[html.Div(Y_chart3), html.Div(Y_chart4)],
                style={"display": "flex"}
            )
        ]

    return None


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
