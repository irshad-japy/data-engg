"""
Reference:
https://www.datasciencemadesimple.com/join-merge-data-frames-pandas-python/
https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
https://www.w3resource.com/pandas/dataframe/dataframe-merge.php

"""

import pandas as pd
import numpy as np

# data frame 1
d1 = {'EmployeeId': pd.Series([1, 2, 3, 4, 5, 6]),
      'PID': pd.Series(['PID186', 'PID182', 'PID189', 'PID176', 'PID178', 'PID181']),
      'Skills': pd.Series(['Java', 'Python', 'JavaScript', 'Pyspark', 'AWS', 'SQL']),
      'Mobile': [8100, 8200, 8300, 8400, 9100, 9200]}
df1 = pd.DataFrame(d1)

# data frame 2
d2 = {'EmployeeId': pd.Series([2, 4, 6, 7, 8]),
      'ProjectId': pd.Series(['PID182', 'PID176', 'PID181', 'PID191', 'PID194']),
      'Salary': pd.Series([50000, 45000, 60000, 40000, 50000]),
      'Mobile': [8200, 8400, 9200, 9400, 9600]}
df2 = pd.DataFrame(d2)

# inner join in python pandas
inner_join_df1 = pd.merge(df1, df2, how='inner', on='EmployeeId')
inner_join_df2 = df1.merge(df2, how='inner', left_on=['EmployeeId', 'PID'], right_on=['EmployeeId', 'ProjectId'],
                           suffixes=('_left', '_right'), validate='1:1')

# # outer join in python pandas
# outer_join_df1 = pd.merge(df1, df2, how='outer', on='EmployeeId')
# outer_join_df2 = df1.merge(df2, how='outer', left_on='Skills', right_on='State',
#                            suffixes=('_left', '_right'))
#
# # left join in python
# left_join_df1 = pd.merge(df1, df2, how='left', on='EmployeeId')
# left_join_df2 = df1.merge(df2, how='left', left_on='Skills', right_on='State',
#                           suffixes=('_left', '_right'))
#
# # right join in python pandas
# right_join_df1 = pd.merge(df1, df2, how='right', on='EmployeeId')
# right_join_df2 = df1.merge(df2, how='right', left_on='Skills', right_on='State',
#                            suffixes=('_left', '_right'))
#
# # join based on index python pandas
# df_index1 = pd.merge(df1, df2, right_index=True, left_index=True)
# df_index2 = df1.merge(df2, right_index=True, left_index=True)
#
# # Concatenate and keep the old index python pandas
# df_row = pd.concat([df1, df2])
