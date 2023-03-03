from dash import html, dcc

cumulation_layout =html.Div([ html.H1('Cash Cumulation',style={'textAlign':'center','color':'#503D36','font-size': 40}),
html.P('The Best Bit', style={'text-align':'center', 'color':'#503D36'}),
html.Div([
    html.Div(dcc.Graph(id='cash-cumulation')),], style={'width': '100'}),])