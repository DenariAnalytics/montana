from dash import html, dcc

demo_layout = html.Div(
    id='revenue-container',
    children=[html.H1('Demographics', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
              html.P('Understanding your Customers', style={'textAlign': 'center', 'color': '#503D36'}),
              html.Center(
    html.Div([
    dcc.Dropdown(id='dem-dropdown', value='shop', options=[{'label': 'gender', 'value': 'gender'},
                                                           {'label': 'age range', 'value': 'age range'},
                                                           ],
                                                           style={'display': 'inline-block', 'width': '150px'}),
                                                           ], style={'width': '100%'}),
),
              html.Div([html.Div(dcc.Graph(id='demographics'), style={'flex': '1'}),],
                        style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'width': '100%'}
                        ),
            ],
            style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'}
            )
