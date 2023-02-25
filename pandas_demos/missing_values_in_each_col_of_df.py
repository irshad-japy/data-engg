import pandas as pd
import numpy as np

data = {'first_set': [1, 2, 3, 4, 5, np.nan, 6, 7, np.nan, np.nan],
        'second_set': ['a', 'b', np.nan, np.nan, 'c', 'd', 'e', np.nan, np.nan, 'f'],
        'third_set': ['aa', np.nan, 'bb', 'cc', np.nan, np.nan, 'dd', np.nan, np.nan, 'ee']
        }

df = pd.DataFrame(data, columns=['first_set', 'second_set', 'third_set'])


def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    print('1' * 30)
    print(mis_val_table)
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})
    print('2' * 30)
    print(mis_val_table_ren_columns)
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
                                                              "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")
    print('3' * 30)
    print(mis_val_table_ren_columns)
    return mis_val_table_ren_columns


mis_val_table_ren_columns = missing_values_table(df)
