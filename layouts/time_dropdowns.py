from dash import html, dcc
import dash_bootstrap_components as dbc

style_drop = {
    'display': 'inline-block', 
    'width': '300px', 
    'margin': 'auto', 
    'vertical-align': 'left'
    }

style_label = {
    'text-align': 'center',
    'vertical-align': 'middle',
    'line-height': '34px'
}

dropdowns = dbc.Row(
    [
        dbc.Col(
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Analysis Period Size:", style=style_label),
                    dbc.Select(
                        id="dropdown-1",
                        value="year",
                        options=[
                            {"label": "All Time", "value": "alltime"},
                            {"label": "Tax Year", "value": "tax year"},
                            {"label": "Year", "value": "year"},
                            {"label": "Quarter", "value": "quarter"},
                            {"label": "Month", "value": "month"},
                            {"label": "Week", "value": "week"},
                        ],
                    ),
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Select Analysis Period:", style=style_label),
                    dbc.Select(
                        id="sub-dropdown-1", value="2022", options=[], 
                    ),
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Group By:", style=style_label),
                    dbc.Select(
                        id="sub-dropdown-2", value="month", options=[], 
                    ),
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Bar Mode:", style=style_label),
                    dbc.Select(
                        id="bar-type",
                        value="group",
                        options=[
                            {"label": "Group", "value": "group"},
                            {"label": "Stack", "value": "stack"},
                        ],
                    ),
                ]
            ),
            md=3,
        ),
    ],
    justify="center",
    className="no-gutters row-centered",
    style={'margin-top': '50px'},
)
