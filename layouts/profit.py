from dash import html, dcc

profit_layout = html.Div([
    html.H1('Profit/Loss', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Revenue, Expenditure, Gross Profit', style={'textAlign': 'center', 'color': '#503D36'}),
    html.Div([
        html.Div(dcc.Graph(id='rev-exp-prof'), style={'width': '50%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='rev-exp-prof-tot'), style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'width': '100%'})
])
