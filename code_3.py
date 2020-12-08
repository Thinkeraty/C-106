import csv
import plotly.express as px
import numpy as np

def get_data(data_path):
    icecream_sales = []
    temperature = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        
        for row in df:
            icecream_sales.append(float(row['Ice-cream Sales']))
            temperature.append(float(row['Temperature']))

    return { 'x': icecream_sales, 'y': temperature }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])

def setup():
    data_path = 'Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    data_source = get_data(data_path)
    find_correlation(data_source)

setup()