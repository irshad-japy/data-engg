import pandas as pd
import numpy as np

data = {'first_set': [1, 2, 3, 4, 5, np.nan, 6, 7, np.nan, np.nan],
        'second_set': ['a', 'b', np.nan, np.nan, 'c', 'd', 'e', np.nan, np.nan, 'f'],
        'third_set': ['aa', np.nan, 'bb', 'cc', np.nan, np.nan, 'dd', np.nan, np.nan, 'ee']
        }

df = pd.DataFrame(data, columns=['first_set', 'second_set', 'third_set'])

"""
# (1) Count NaN values under a single DataFrame column
syntax:df['column name'].isna().sum()

(2) Count NaN values under the entire DataFrame
syntax:df.isna().sum().sum()

(3) Count NaN values across a single DataFrame row:
syntax:df.loc[[index value]].isna().sum().sum()
example:df.loc[[7]].isna().sum().sum()

"""

count_nan = df['first_set'].isna().sum()
# below seems incorrect code for NaN count
#df[df['first_set'].isna()].count()
print(count_nan)
