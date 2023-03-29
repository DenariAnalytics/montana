from dash import html, dcc
import dash_bootstrap_components as dbc

options = {"shop": "shop",
            "type": "type"}
           
category_dropdown = dbc.Select(
    id="cat-dropdown",
    options=options,
    value="shop",
)
text_input_group = dbc.InputGroup(
    [
        dbc.InputGroupText("Categorize By:"),
        category_dropdown,
    ]
)
cost_layout = html.Div([
    html.H1('Cost Analysis', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Analysis of Expenses', style={'text-align': 'center', 'color': '#503D36'}),
    html.Center(
        html.Div(dbc.Row(
    [
        dbc.Col(text_input_group, width=4),
    ],
    justify="center",
    
    ),
    style={'width': '100%'}),
    ),
    html.Div([
        html.Div(dcc.Graph(id='costs'), style={'width': '50%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='cost-totals'), style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'width': '100%'}),
])
