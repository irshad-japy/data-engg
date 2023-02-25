'''
assert_dict_equal: This method is used to compare two dictionaries. It tests for equality of the keys and values.
'''

import pandas as pd

dict1 = {'col1': [1, 2], 'col2': [3, 4]}
dict2 = {'col1': [1, 2], 'col2': [3, 4]}

pd.testing.assert_dict_equal(dict1, dict2)
