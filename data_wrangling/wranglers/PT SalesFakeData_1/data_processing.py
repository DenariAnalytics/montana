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
        narc.set_dates(i)

    s = sales.copy()
    c = costs.copy()

    s = narc.fill_dates(s)
    c = narc.fill_dates(c)

    c = narc.split_dates(c,format='period')
    s = narc.split_dates(s,format='period')

    processed_data = {'sales': s,
                      'costs': c,
                      }
    
    return processed_data