import os
import sys

def get_data(company):
    path = os.path.dirname(os.path.abspath(__file__))

    company_log = {
        'PT Fake 1': path + '/wranglers/PT SalesFakeData_1',
        'shroom': path + '/wranglers/shroom',
    }

    data_path = os.path.join(path, company_log[company])
    sys.path.append(data_path)

    from data_processing import process

    data = process()

    return data
