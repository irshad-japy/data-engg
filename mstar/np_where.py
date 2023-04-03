import pandas as pd
import numpy as np

# create sample DataFrame
df = pd.DataFrame({'Fund A': [10, 5, 8, 12],
                   'Category B': [8, 10, 5, 12]})

# create new column using np.where
output_column_name = 'Fund A vs Category B'
df[output_column_name] = np.where(df['Fund A'] < df['Category B'],
                                  'higher',
                                  np.where(df['Fund A'] > df['Category B'],
                                           'lower',
                                           np.where(df['Fund A'] == df['Category B'],
                                                    'same',
                                                    'NA'
                                                    )
                                           )
                                  )

print(df)
