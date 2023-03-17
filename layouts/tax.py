from dash import html, dcc

profit_layout = html.Div([
    html.H1('Tax Analysis', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Optimize and Analyse', style={'textAlign': 'center', 'color': '#503D36'}),
    html.P('"The tax man is a bully" - Robert Kiyosaki"', style={'textAlign': 'center', 'color': '#503D36'}),
    html.Div([
        html.Div(dcc.Graph(id='rev-exp-prof'), style={'width': '50%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='rev-exp-prof-tot'), style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'width': '100%'})
])
