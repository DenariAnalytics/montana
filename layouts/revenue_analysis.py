from dash import html, dcc

revenue_layout = html.Div(
    id='revenue-container',
    children=[html.H1('Revenue Analysis', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
              html.P('Analysis of Package Sales', style={'textAlign': 'center', 'color': '#503D36'}),
              html.Div([html.Div([html.H4('Package Sales', style={'text-align': 'center'}),
                                  dcc.Graph(id='pack-sales'),],style={'flex': '1'}),
                        html.Div([html.H4('Total Package Sales for this Period', style={'text-align': 'center'}),
                                  dcc.Graph(id='pack-tot'),],style={'flex': '1'}),],
                                  style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'width': '100%'}),
                        html.Div([html.Div([html.H4('Cash vs Bank Transfer', style={'text-align': 'center'}),
                                            dcc.Graph(id='cash-card'),], style={'flex': '1'}),
                        html.Div([html.H4('Total Cash and Bank Transfers for this Period', style={'text-align': 'center'}),
                                  dcc.Graph(id='pay-tot'),], style={'flex': '1'}),], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'width': '100%'}),],
                      style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'}
                      )

