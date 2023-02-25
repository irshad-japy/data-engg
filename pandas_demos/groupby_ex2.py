import pandas as pd
import numpy as np

# create a sample dataframe
data = {'Gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
        'Age': [25, 32, 45, 19, 28, 36, 50, 42, 33, 27],
        'Income': [50000, 75000, 60000, 30000, 80000, 90000, 40000, 65000, 55000, 70000],
        'Location': ['City', 'City', 'Rural', 'Rural', 'City', 'Rural', 'City', 'City', 'Rural', 'Rural']}

df = pd.DataFrame(data)

# group the data by gender and location, and calculate the mean age and income for each group
grouped = df.groupby(['Gender', 'Location']).agg({'Age': np.mean, 'Income': np.mean})

print(grouped)
