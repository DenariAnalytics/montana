import os
import pandas as pd
from denari import NarcoAnalytics as narc

def process():

    path = os.getcwd()
    data_folder = os.path.join(path, "data/PT SalesFakeData_1")
    costs = pd.read_csv(data_folder + "/spending.csv", infer_datetime_format=True)
    pack = pd.read_csv(data_folder + "/packages.csv", infer_datetime_format=True)
    clients = pd.read_csv(data_folder + "/clients.csv", infer_datetime_format=True)
    sales = pd.read_csv(data_folder + "/calex.csv", infer_datetime_format=True)
    x = [costs,pack,sales]
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