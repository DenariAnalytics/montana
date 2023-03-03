import os
import pandas as pd
from denari import NarcoAnalytics as narc, Montana as mn, TaxTools as tax
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

slash = '/'
path = os.getcwd()
data_folder = path + slash + "data" + slash
costs = pd.read_csv(data_folder + "spending.csv", infer_datetime_format=True)
pack = pd.read_csv(data_folder + "packages.csv", infer_datetime_format=True)
clients = pd.read_csv(data_folder + "clients.csv", infer_datetime_format=True)
sales = pd.read_csv(data_folder + "calex.csv", infer_datetime_format=True)
x = [costs,pack,sales]
for i in x:
    narc.set_dates(i)

s = sales.copy()
c = costs.copy()

s = narc.fill_dates(s)
c = narc.fill_dates(c)

c = narc.split_dates(c,format='period')
s = narc.split_dates(s,format='period')

from title import title_layout
from time_dropdowns import dropdowns
from revenue_analysis import revenue_layout
from profit import profit_layout
from cost import cost_layout
from cash_cumulate import cumulation_layout
from demographics import demo_layout

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])


app.layout = html.Div(children=[html.Div(title_layout),
                                html.Div(dropdowns, {'position': 'fixed', 'top': '0'}),
                                dcc.Tabs(id='tabs', value='tab-1', children=[
                                    dcc.Tab(label='Revenue', value='tab-1', children=[
                                        html.Div(revenue_layout)
                                    ]),
                                    dcc.Tab(label='Costs', value='tab-2', children=[
                                        html.Div(cost_layout)
                                    ]),
                                    dcc.Tab(label='Profit', value='tab-3', children=[
                                        html.Div(profit_layout)
                                    ]),
                                    dcc.Tab(label='Cash Cumulation', value='tab-4', children=[
                                        html.Div(cumulation_layout)
                                    ]),
                                    dcc.Tab(label='Year Comparison', value='tab-5', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Tax Analysis', value='tab-6', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Customer Analysis', value='tab-7', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                    dcc.Tab(label='Demographics', value='tab-8', children=[
                                        html.Div(html.H1('COMING SOON', style={'text-align': 'center', 'margin-top': '30vh', 'font-size': '5em'}))
                                    ]),
                                ]),
                               ])
                               

@app.callback(Output('sub-dropdown-1', 'options'), [Input('dropdown-1', 'value')])
def sub_dropdown_1(main_dropdown_value):
    options = mn.input_dropdown_column_set(s,main_dropdown_value)
    return options

@app.callback(Output('sub-dropdown-2', 'options'), [Input('dropdown-1', 'value')])
def sub_dropdown_2(main_dropdown_value):
    options = mn.input_dropdown_micro(main_dropdown_value)
    return options

@app.callback([Output(component_id='pack-sales', component_property='figure'),
               Output(component_id='cash-card', component_property='figure'),
               Output(component_id='pack-tot', component_property='figure'),
               Output(component_id='pay-tot', component_property='figure')],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-2', component_property='value'),
               Input(component_id='bar-type', component_property='value')
              ])

def revenue(main_dropdown_value,sub_dropdown_1,sub_dropdown_2,bar_mode):
    color = 'one'
    dff = s.copy()
    dff = dff.fillna(0)
    
    cat = 'package'
    order_ls = narc.column_set(dff,cat,'payment')
    order_lspt = narc.column_set(dff,'payment type','payment')

    if main_dropdown_value != 'alltime':
        dff = dff[dff[main_dropdown_value] == sub_dropdown_1]
    else:
        dff = dff

    pack_sales = narc.aggregate_category(dff,sub_dropdown_2,cat,'payment',order_ls)
    pack_sales = pack_sales.drop(0, axis=1)
    cash_card = narc.aggregate_category(dff,sub_dropdown_2,'payment type','payment',order_lspt)
    cash_card = cash_card.drop(0, axis=1)

    mc = narc.metric_columns(pack_sales,'sum')
    ccmc = narc.metric_columns(cash_card,'sum')

    a = narc.graph_index_columns(pack_sales,colors=color,barmode=bar_mode)
    b = narc.graph_index_columns(cash_card,colors=color,barmode=bar_mode)
    c = narc.graph_metrics(mc)
    d = narc.graph_metrics(ccmc)
    
    return [a,b,c,d]

@app.callback([Output(component_id='costs', component_property='figure'),
               Output(component_id='cost-totals', component_property='figure')],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-2', component_property='value'),
               Input(component_id='bar-type', component_property='value'),
               Input(component_id='cat-dropdown', component_property='value')]
             )

def costs(main_dropdown_value, sub_dropdown_1, sub_dropdown_2, bar_mode, cat):
    color = 'one'
    dff = c.copy()
    dff = dff.fillna(0)

    order_ls = narc.column_set(dff,cat,'cost')

    if main_dropdown_value != 'alltime':
        dff = dff[dff[main_dropdown_value] == sub_dropdown_1]
    else:
        dff = dff

    agg_costs = narc.aggregate_category(dff,sub_dropdown_2,cat,'cost',order_ls)
    agg_costs = agg_costs.drop(0, axis=1)
    mc = narc.metric_columns(agg_costs,'sum')

    a = narc.graph_index_columns(agg_costs,colors=color,barmode=bar_mode)
    b = narc.graph_metrics(mc)
    
    return [a,b]


@app.callback([Output(component_id='rev-exp-prof', component_property='figure'),
               Output(component_id='rev-exp-prof-tot', component_property='figure')],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-2', component_property='value'),
               Input(component_id='bar-type', component_property='value')
              ]
             )

def rev_exp_prof(main_dropdown_value,sub_dropdown_1,sub_dropdown_2,bar_mode):
    color = 'one'
    
    sales = s.copy()
    costs = c.copy()
    

    if main_dropdown_value != 'alltime':
        sales = sales[sales[main_dropdown_value] == sub_dropdown_1]
        costs = costs[costs[main_dropdown_value] == sub_dropdown_1]
    else:
        sales = sales
        costs = costs
    
    sales = sales.groupby(s['date'])['payment'].sum().reset_index()
    sales = sales.rename(columns={'payment': 'revenue'})
    costs = costs.groupby(c['date'])['cost'].sum().reset_index()
    costs = costs.rename(columns={'cost': 'expenditure'})
    sc = pd.merge(sales, costs, on='date', how='outer')
    sc = sc.fillna(0)
    sc['gross profit'] = sc['revenue'] - sc['expenditure']
    profit = narc.create_date_range(sc.iloc[0]['date'],split_dates=False,last_date=sc.iloc[-1]['date'])
    profit = pd.merge(profit, sc, on='date', how='outer')
    profit = profit.fillna(0)
    profit = narc.split_dates(profit,format='period')
    
    prof = narc.gross_profit(profit,sub_dropdown_2)
    total = narc.metric_columns(prof,'sum')
    
    a = narc.graph_index_columns(prof,colors=color,barmode=bar_mode)
    b = narc.graph_metrics(total)
    
    return [a,b]
                                 
@app.callback([Output(component_id='cash-cumulation', component_property='figure'),],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-2', component_property='value'),
               Input(component_id='bar-type', component_property='value')])
                                 
def cash_cumulate(main_dropdown_value,sub_dropdown_1,sub_dropdown_2,bar_mode):
    color = 'one'
    
    sales = s.copy()
    costs = c.copy()
    
    if main_dropdown_value != 'alltime':
        sales = sales[sales[main_dropdown_value] == sub_dropdown_1]
        costs = costs[costs[main_dropdown_value] == sub_dropdown_1]
    else:
        sales = sales
        costs = costs
    
    sales = sales.groupby(s['date'])['payment'].sum().reset_index()
    sales = sales.rename(columns={'payment': 'revenue'})
    costs = costs.groupby(c['date'])['cost'].sum().reset_index()
    costs = costs.rename(columns={'cost': 'expenditure'})
    sc = pd.merge(sales, costs, on='date', how='outer')
    sc = sc.fillna(0)
    sc['gross profit'] = sc['revenue'] - sc['expenditure']
    profit = narc.create_date_range(sc.iloc[0]['date'],split_dates=False,last_date=sc.iloc[-1]['date'])
    profit = pd.merge(profit, sc, on='date', how='outer')
    profit = profit.fillna(0)
    profit = narc.split_dates(profit,format='period')
    
    prof = narc.gross_profit(profit,sub_dropdown_2)
                                 
    cumulate = prof.copy()
    cumulate = narc.cash_cumulate(cumulate)
    cumulate = cumulate[[col for col in cumulate.columns if 'cumulative' in col]]
    
    a = narc.graph_index_columns(cumulate,colors=color,barmode=bar_mode)
    
    return [a]

@app.callback([Output(component_id='demographics', component_property='figure'),],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='bar-type', component_property='value'),
               Input(component_id='dem-dropdown', component_property='value')])
                                 
def demographics(main_dropdown_value,sub_dropdown_1,bar_mode,demographic):
    color = 'one'
    dem = sales.copy()
    
    if main_dropdown_value != 'alltime':
        dem = dem[dem[main_dropdown_value] == sub_dropdown_1]
    else:
        dem = dem

    dem = dem.merge(clients, on=['surname', 'name'], how='left')
    bins = [20, 25, 30, 35, 40, 45, 50, 55]
    labels = ['20-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55']
    dem['age range'] = pd.cut(dem['age'], bins=bins, labels=labels)
    pack_order = ['single','five','eight','ten','twelve','twenty']
    cat_package = pd.Categorical(pack['package'], categories=pack_order, ordered=True)
    cat = 'gender'
    ls = narc.column_set(dem,cat,'payment')
    raw = narc.aggregate_category(dem,demographic,cat,'payment',ls,metric='sum')
    a = narc.graph_index_columns(raw,colors=color,barmode=bar_mode)
    return [a]

if __name__ == '__main__':
    app.run_server()