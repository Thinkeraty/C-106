# import csv
# import plotly.express as px
# import pandas as pd

# with open('Student Marks vs Days Present.csv', newline='') as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x='Student Marks vs Days Present.csv', y='Marks In Percentage')
#     fig.show()

import csv
import plotly.express as px
import numpy as np

def get_data(data_path):
    days_present = []
    marks = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        
        for row in df:
            days_present.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))

    return { 'x': days_present, 'y': marks }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])

def setup():
    data_path = 'Student Marks vs Days Present.csv'
    data_source = get_data(data_path)
    find_correlation(data_source)

setup()