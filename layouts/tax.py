from dash import html, dcc
import dash_bootstrap_components as dbc

# Create the options list for tax_years
tax_years = ["2020/2021", "2021/2022", "2022/2023", "2023/2024"]
options = [{"label": i, "value": i} for i in tax_years]

tax_year_dropdown = dbc.Select(
    id="tax_year_dropdown",
    options=options,
    placeholder="Select a tax year",
)

# Text string input with InputGroup
text_input_group = dbc.InputGroup(
    [
        dbc.InputGroupText("Tax Code"),
        dbc.Input(id="text_input", type="text", placeholder="Enter text", value= '1257A'),
    ]
)

# Salary integer input with InputGroup
salary_input_group = dbc.InputGroup(
    [
        dbc.InputGroupText("Salary"),
        dbc.Input(id="salary_input", type="number", placeholder="Enter salary", value=12500),
    ]
)

# Tax year dropdown input with InputGroup
tax_year_input_group = dbc.InputGroup(
    [
        dbc.InputGroupText("Tax Year"),
        tax_year_dropdown,
    ]
)

tax_layout = html.Div([
    html.H1('Tax Analysis', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Optimize and Analyse', style={'textAlign': 'center', 'color': '#503D36'}),
    html.P('"The tax man is a bully" - Robert Kiyosaki', style={'textAlign': 'center', 'color': '#503D36'}),
    # Combine the components in a row
    dbc.Row(
    [
        dbc.Col(text_input_group, width=4),
        dbc.Col(salary_input_group, width=4),
        dbc.Col(tax_year_input_group, width=4),
    ],
    justify="center",
    ),
    #Calculate Button
    dbc.Button("Calculate", id="submit_button", color="primary"),
    #Output
    html.Div(id="result_output"),
    #Optimize Button
    dbc.Button("Optimize", id="optimize_button", color="primary"),
    dcc.Graph(id='iteration_graph', style={'width': '50%', 'display': 'inline-block'})
    ])