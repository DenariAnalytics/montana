import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from layouts.title import title_layout
from layouts.time_dropdowns import dropdowns
from layouts.revenue_analysis import revenue_layout
from layouts.profit import profit_layout
from layouts.cost import cost_layout
from layouts.cash_cumulate import cumulation_layout
from layouts.demographics import demo_layout

from app import app

tab_layout = dbc.Container(
    [
        html.Div(dropdowns),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(title_layout),
                        dbc.Nav(
                            [
                                dbc.NavLink("Revenue", href="/revenue", id="tab-1"),
                                dbc.NavLink("Costs", href="/costs", id="tab-2"),
                                dbc.NavLink("Profit", href="/profit", id="tab-3"),
                                dbc.NavLink("Cash Cumulation", href="/cash-cumulation", id="tab-4"),
                                dbc.NavLink("Year Comparison", href="/year-comparison", id="tab-5"),
                                dbc.NavLink("Tax Analysis", href="/tax-analysis", id="tab-6"),
                                dbc.NavLink("Customer Analysis", href="/customer-analysis", id="tab-7"),
                                dbc.NavLink("Demographics", href="/demographics", id="tab-8"),
                            ],
                            vertical=True,
                            pills=True,
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    html.Div(id="content"),
                    width=10,
                ),
            ]
        ),
    ],
    fluid=True,
)

from dash import no_update

@app.callback(
    Output("content", "children"),
    [Input("tab-1", "n_clicks"),
     Input("tab-2", "n_clicks"),
     Input("tab-3", "n_clicks"),
     Input("tab-4", "n_clicks"),
     Input("tab-5", "n_clicks"),
     Input("tab-6", "n_clicks"),
     Input("tab-7", "n_clicks"),
     Input("tab-8", "n_clicks")],
)
def render_content(tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8):
    ctx = dash.callback_context

    if not ctx.triggered:
        return no_update
    else:
        tab_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if tab_id == "tab-1":
        return revenue_layout
    elif tab_id == "tab-2":
        return cost_layout
    elif tab_id == "tab-3":
        return profit_layout
    elif tab_id == "tab-4":
        return cumulation_layout
    elif tab_id == "tab-5":
        return html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'})
    elif tab_id == "tab-6":
        return html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'})
    elif tab_id == "tab-7":
        return html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'})
    elif tab_id == "tab-8":
        return html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'})
    

