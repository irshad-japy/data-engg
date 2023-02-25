import pandas as pd
import numpy as np

data = {'first_set': [1, 2, 3, 4, 5, np.nan, 6, 7, np.nan, np.nan],
        'second_set': ['a', 'b', np.nan, np.nan, 'c', 'd', 'e', np.nan, np.nan, 'f'],
        'third_set': ['aa', np.nan, 'bb', 'cc', np.nan, np.nan, 'dd', np.nan, np.nan, 'ee']
        }

df = pd.DataFrame(data, columns=['first_set', 'second_set', 'third_set'],
                  index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8', 'row_9'])

# find nan counts in a row
count_nan = df.loc[['row_7']].isna().sum().sum()

print('Count of NaN: ' + str(count_nan))
