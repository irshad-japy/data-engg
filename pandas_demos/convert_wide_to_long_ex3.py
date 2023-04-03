import pandas as pd

'''
Suppose you have two dataframes df1 and df2:
You can merge them based on the common column ID using merge function:
You can then use the melt function to unpivot the columns A, B, C, and D into rows of a new column called Variable:

The resulting dataframe has a row for each combination of ID and Variable with the corresponding value in the value 
column.

df1:
   ID   A   B
0   1  10  40
1   2  20  50
2   3  30  60

df2:
   ID   C    D
0   1  70  100
1   2  80  110
2   3  90  120

merged_df:
   ID   A   B   C    D
0   1  10  40  70  100
1   2  20  50  80  110
2   3  30  60  90  120

'''
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'A': [10, 20, 30],
                    'B': [40, 50, 60]})

df2 = pd.DataFrame({'ID': [1, 2, 3],
                    'C': [70, 80, 90],
                    'D': [100, 110, 120]})
merged_df = df1.merge(df2, on='ID')
unpivoted_df = merged_df.melt(id_vars=['ID'], var_name='Variable')

print(unpivoted_df)
