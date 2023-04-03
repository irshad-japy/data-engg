import pandas as pd

# create two dataframes
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'C', 'D', 'D'], 'value': [1, 2, 3, 4, 5, 6]})
df2 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [7, 8, 9, 10]})

# merge with many_to_one validation
result = df1.merge(df2, on='key', validate='many_to_one')

print(result)
