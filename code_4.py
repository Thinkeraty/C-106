import csv
import plotly.express as px
import numpy as np

def get_data(data_path):
    size_of_tv = []
    time_spent = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        
        for row in df:
            size_of_tv.append(float(row['Size of TV']))
            time_spent.append(float(row['\tAverage time spent watching TV in a week']))

    return { 'x': size_of_tv, 'y': time_spent }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])

def setup():
    data_path = 'Size of TV and Average time spent watching TV in a week.csv'
    data_source = get_data(data_path)
    find_correlation(data_source)

setup()