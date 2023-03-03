from dash import html, dcc

cost_layout = html.Div([
    html.H1('Cost Analysis', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Analysis of Expenses', style={'text-align': 'center', 'color': '#503D36'}),
    html.Center(
        html.Div([
            dcc.Dropdown(id='cat-dropdown', value='shop', options=[{'label': 'shop', 'value': 'shop'},
                                                                    {'label': 'type', 'value': 'type'},
                                                                   ],
                         style={'display': 'inline-block', 'width': '150px'}),
        ], style={'width': '100%'}),
    ),
    html.Div([
        html.Div(dcc.Graph(id='costs'), style={'width': '50%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='cost-totals'), style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'width': '100%'}),
])
