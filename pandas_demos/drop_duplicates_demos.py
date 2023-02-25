'''
The drop_duplicates() method in Pandas is used to remove duplicates from a DataFrame. It can be used to drop duplicates
based on one or more columns. The subset parameter is used to specify the columns to use for identifying duplicates,
and the keep parameter is used to specify which duplicate to keep.

Here is an example of how to use drop_duplicates() with the subset and keep parameters:

'''

import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
        'score': [80, 90, 70, 85, 95, 75],
        'age': [25, 30, 35, 25, 30, 35]}
df = pd.DataFrame(data)

# Drop duplicates based on the name column, keeping the last duplicate
df_unique = df.drop_duplicates(subset='name', keep='last')

print(df_unique)

'''
In this example, we used drop_duplicates() to remove duplicates based on the name column. We specified keep='last' to 
keep the last duplicate of each group of duplicates. In other words, for each group of rows that have the same value 
in the name column, we kept only the last row in the group.

The resulting DataFrame df_unique contains only the last row for each unique name. We can see that Alice, Bob, and 
Charlie are still in the DataFrame, but the duplicate rows have been removed.

Note that if you don't specify the subset parameter, drop_duplicates() will remove duplicates based on all columns 
in the DataFrame. If you don't specify the keep parameter, drop_duplicates() will keep the first occurrence of each 
group of duplicates.
'''
