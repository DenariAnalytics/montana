from dash import html, dcc

from layouts.title import title_layout
from layouts.time_dropdowns import dropdowns
from layouts.revenue_analysis import revenue_layout
from layouts.profit import profit_layout
from layouts.cost import cost_layout
from layouts.cash_cumulate import cumulation_layout
from layouts.demographics import demo_layout

tab_layout = html.Div(children=[html.Div(title_layout),
                                html.Div(dropdowns, {'position': 'fixed', 'top': '0'}),
                                dcc.Tabs(id='tabs', value='tab-1', children=[
                                    dcc.Tab(label='Revenue', value='tab-1', children=[
                                        html.Div(revenue_layout)
                                    ]),
                                    dcc.Tab(label='Costs', value='tab-2', children=[
                                        html.Div(cost_layout)
                                    ]),
                                    dcc.Tab(label='Profit', value='tab-3', children=[
                                        html.Div(profit_layout)
                                    ]),
                                    dcc.Tab(label='Cash Cumulation', value='tab-4', children=[
                                        html.Div(cumulation_layout)
                                    ]),
                                    dcc.Tab(label='Year Comparison', value='tab-5', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Tax Analysis', value='tab-6', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Customer Analysis', value='tab-7', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Demographics', value='tab-8', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                ]),
                               ])