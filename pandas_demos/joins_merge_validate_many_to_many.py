'''
is validate='many_to_many' and how='outer' same?

Answer:
No, validate='many_to_many' and how='outer' are not the same.
validate='many_to_many' is a parameter in the merge() function in Pandas that checks if the merge keys contain
duplicates. If there are duplicates, it creates a Cartesian product of the rows that share the same key values. This is
useful for handling many-to-many relationships in which the same key values appear multiple times in both the left and
right DataFrames.

On the other hand, how='outer' is a parameter that specifies the type of merge to perform. An outer join returns all
rows from both left and right DataFrames, and fills the missing values with NaN. This is useful for retaining all the
data from both DataFrames, even if there are missing or non-matching values.

So while they may be used together in some cases, they are not interchangeable or the same thing.
'''
import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D', 'E'],
    'value': [1, 2, 3, 4, 5]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'C', 'D', 'D', 'D'],
    'value': [10, 20, 30, 40, 50, 60]
})
merged_df = pd.merge(df1, df2, on='key', how='outer', validate='many_to_many')

print(merged_df)