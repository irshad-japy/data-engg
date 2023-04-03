import pandas as pd

# create two dataframes
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [5, 6, 7, 8]})

# merge with one_to_one validation
result = df1.merge(df2, on='key', validate='one_to_one')

print(result)
