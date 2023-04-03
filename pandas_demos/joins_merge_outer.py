import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'B', 'C', 'C', 'C'],
    'value': [10, 20, 30, 40, 50, 60]
})

df3 = df1.merge(df2, on='key', how='outer')

print(df3)
