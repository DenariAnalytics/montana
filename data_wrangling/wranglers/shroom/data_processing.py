import os
import pandas as pd
from denari import NarcoAnalytics as narc

def process():
    path = os.getcwd()
    data_folder = os.path.join(path, "data/shrooms")
    costs = pd.read_csv(data_folder + "/1_costs.csv", infer_datetime_format=True)
    yields = pd.read_csv(data_folder + "/2_myl.csv", infer_datetime_format=True)
    prices = pd.read_csv(data_folder + "/3_price.csv", infer_datetime_format=True)
    sales = pd.read_csv(data_folder + "/4_sales.csv", infer_datetime_format=True)
    #clients = pd.read_csv(data_folder + "/clients.csv", infer_datetime_format=True)
    
    x = [costs,yields,prices,sales]
    for i in x:
        narc.dates_set_column(i)

    s = sales.copy()
    c = costs.copy()

    s = narc.dates_fill_gaps(s)
    c = narc.dates_fill_gaps(c)

    c = narc.dates_split(c,format='period')
    s = narc.dates_split(s,format='period')

    processed_data = {'sales': s,
                      'costs': c,
                      }
    
    return processed_data