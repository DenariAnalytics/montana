from dash import html, dcc

style_drop = {
    'display': 'inline-block', 
    'width': '300px', 
    'margin': 'auto', 
    'vertical-align': 'left'
    }

style_label = {
        'display': 'inline-block',
        'width': '150px',
        'text-align': 'center',
        'vertical-align': 'middle',
        'line-height': '34px'
    }

dropdowns = html.Div([
    html.Label('Analysis Period Size:', style=style_label),
    dcc.Dropdown(id='dropdown-1', 
                 value='year',
                 options=[
                     {'label': 'All Time', 'value': 'alltime'},
                     {'label': 'Tax Year', 'value': 'tax year'},
                     #{'label': 'Multi-Year', 'value': 'year'},
                     {'label': 'Year', 'value': 'year'},
                     {'label': 'Quarter', 'value': 'quarter'},
                     {'label': 'Month', 'value': 'month'},
                     {'label': 'Week', 'value': 'week'}
                 ],
                 style=style_drop
    ),
    html.Label('Select Analysis Period:', style=style_label),
    dcc.Dropdown(id='sub-dropdown-1', 
                 value='2022', 
                 options=[], 
                 style=style_drop
    ),
    html.Label('Group By:', style=style_label),
    dcc.Dropdown(id='sub-dropdown-2', 
                 value='month', 
                 options=[], 
                 style=style_drop
    ),
    html.Label('Bar Mode:', style=style_label),
    dcc.Dropdown(id='bar-type', 
                 value='group', 
                 options=[
                     {'label': 'Group', 'value': 'group'},
                     {'label': 'Stack', 'value': 'stack'}
                 ],
                 style=style_drop
    )
],
style={
    'text-align': 'center',
    'display': 'flex',
    'flex-direction': 'row',
    'align-items': 'center',
    'justify-content': 'center'
})
