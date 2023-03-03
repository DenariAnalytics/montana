from dash import html, dcc

from revenue_analysis import revenue_layout
from profit import profit_layout
from cost import cost_layout
from cash_cumulate import cumulation_layout

tab_layout = dcc.Tabs(id='tabs', value='tab-1', children=[
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
                                    dcc.Tab(label='Demographics', value='tab-5', children=[
                                        html.Div('COMING SOON')
                                    ]),
                                ])