import pandas as pd
from denari import NarcoAnalytics as narc, TaxTools as tax
from montana import montana as mn
from dash.dependencies import Input, Output, State
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash

import index
from data_wrangling import wrangled
from app import app

color = 'one'

data = wrangled.get_data('PT Fake 1')
s = data['sales']
c = data['costs']

app.layout = index.tab_layout
                               
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
    sales = s.copy()
    sales = sales.fillna(0)
    category = 'product'

    sales = mn.filter_time_period(sales,main_dropdown_value,sub_dropdown_1)

    #Create grouped package graph
    package_order = narc.column_set(sales,category,'payment')
    package_sales = narc.aggregate_category(sales.copy(),sub_dropdown_2,category,'payment',package_order)
    package_sales = package_sales.drop(0, axis=1)
    package_graph = narc.graph_index_columns(package_sales,colors=color,barmode=bar_mode)

    #Create grouped payment type graph
    payment_type_list = narc.column_set(sales,'payment type','payment')
    cash_card = narc.aggregate_category(sales,sub_dropdown_2,'payment type','payment',payment_type_list)
    cash_card = cash_card.drop(0, axis=1)
    cash_card_graph = narc.graph_index_columns(cash_card,colors=color,barmode=bar_mode)

    #Graph total package sales this period
    package_totals = narc.metric_columns(package_sales,'sum')
    package_totals_graph = narc.graph_metrics(package_totals)

    #Grpah total payment type this period
    cash_card_totals = narc.metric_columns(cash_card,'sum')
    cash_card_totals_graph = narc.graph_metrics(cash_card_totals)
    
    return [package_graph,cash_card_graph,package_totals_graph,cash_card_totals_graph]

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

    dff = mn.filter_time_period(dff,main_dropdown_value,sub_dropdown_1)

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
    
    sales = mn.filter_time_period(sales,main_dropdown_value,sub_dropdown_1)
    costs = mn.filter_time_period(costs,main_dropdown_value,sub_dropdown_1)
    
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

    sales = mn.filter_time_period(sales,main_dropdown_value,sub_dropdown_1)
    costs = mn.filter_time_period(costs,main_dropdown_value,sub_dropdown_1)
    
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

@app.callback(
    [Output("result_output", "children"),
     Output("iteration_graph", "figure")],
    [Input("submit_button", "n_clicks"),
     Input("optimize_button", "n_clicks")],
    [State("text_input", "value"),
     State("salary_input", "value"),
     State("tax_year_dropdown", "value"),
     State("result_output", "children"),
     State("iteration_graph", "figure")],
    prevent_initial_call=True,
)
def calculate_tax_and_graph(submit_n_clicks, optimize_n_clicks, tc, sal, ty, stored_result_output, stored_iteration_graph):
    t = 40000
    e = 3000
    
    ctx = dash.callback_context

    if not ctx.triggered:
        return "", {}
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "submit_button" and tc and sal and ty:
        result = tax.ltd_full_take(t, sal, e, ty, tc)
        column_names = result.columns.to_list()
        result_dict = result.to_dict(orient='records')
        header = [html.Th(col_name) for col_name in column_names]
        rows = [
            html.Tr([
                html.Td(round(row[col_name], 2) if isinstance(row[col_name], (int, float)) else row[col_name])
                for col_name in column_names
            ])
            for row in result_dict
        ]
        table_body = [html.Thead(header), html.Tbody(rows)]
        test_table = dbc.Table(table_body, bordered=True, striped=True, hover=True, responsive=True)
        return test_table, {}
    
    if button_id == "optimize_button" and tc and sal and ty:
        print("opt")
        tax_iterations = tax.iterate_lite_full_take(t, e, ty, tc, optimal=False)
        columns_to_plot = ['Gross Take', 'Total Takehome']
        colors = narc.color_list(columns_to_plot,'one')
        yaxis2_columns = ['Percentage Take']
        fig = go.Figure()
        for i, column in enumerate(columns_to_plot):
            fig.add_trace(go.Scatter(x=tax_iterations['Salary'], y=tax_iterations[column], mode='lines', name=column, line=dict(color=colors[i]), yaxis='y1'))
        for column in yaxis2_columns:
            fig.add_trace(go.Scatter(x=tax_iterations['Salary'], y=tax_iterations[column], mode='lines', name=column, yaxis='y2'))
        fig.update_layout(title='Tax Optimization',
                          xaxis_title='Salary',
                          yaxis_title='Values',
                          yaxis=dict(title='£'),
                          yaxis2=dict(title='%', overlaying='y', side='right')
                          )
        return {}, fig

    return "", {}



@app.callback([Output(component_id='demographics', component_property='figure'),],
              [Input(component_id='dropdown-1', component_property='value'),
               Input(component_id='sub-dropdown-1', component_property='value'),
               Input(component_id='bar-type', component_property='value'),
               Input(component_id='dem-dropdown', component_property='value')])
                                 
def demographics(main_dropdown_value,sub_dropdown_1,bar_mode,demographic):
    color = 'one'
    sales = s.copy()

    dem = mn.filter_time_period(sales,main_dropdown_value,sub_dropdown_1)

    dem = dem.merge(clients, on=['surname', 'name'], how='left')
    bins = [20, 25, 30, 35, 40, 45, 50, 55]
    labels = ['20-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55']
    dem['age range'] = pd.cut(dem['age'], bins=bins, labels=labels)
    pack_order = ['single','five','eight','ten','twelve','twenty']
    cat_product = pd.Categorical(pack['product'], categories=pack_order, ordered=True)
    cat = 'gender'
    ls = narc.column_set(dem,cat,'payment')
    raw = narc.aggregate_category(dem,demographic,cat,'payment',ls,metric='sum')
    a = narc.graph_index_columns(raw,colors=color,barmode=bar_mode)
    return [a]

if __name__ == '__main__':
    app.run_server()
