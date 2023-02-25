# pd.testing.assert_frame_equal
'''
In each of the test cases, the assert_frame_equal method is used to compare two dataframes. If the dataframes are
identical, the test will pass. If they are different, an AssertionError will be raised, indicating that the test
has failed.
'''

import pandas as pd
import numpy as np

# Test case 1: Compare two identical dataframes
df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

pd.testing.assert_frame_equal(df1, df2)

# Test case 2: Compare two different dataframes
df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 5]})

try:
    pd.testing.assert_frame_equal(df1, df2)
except AssertionError as e:
    print("DataFrames are different:", e)

# Test case 3: Compare two dataframes with different column names
df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col3': [1, 2], 'col4': [3, 4]})

try:
    pd.testing.assert_frame_equal(df1, df2)
except AssertionError as e:
    print("DataFrames are different:", e)

# Test case 4: Compare two dataframes with different indices
df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}, index=[0, 1])
df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}, index=[1, 0])

try:
    pd.testing.assert_frame_equal(df1, df2)
except AssertionError as e:
    print("DataFrames are different:", e)
