'''
assert_categorical_equal: This method is used to compare two pandas Categorical objects. It tests for equality of the
categories, codes, ordered attribute, and dtype.
'''

import pandas as pd

cat1 = pd.Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c'], ordered=False)
cat2 = pd.Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c'], ordered=False)

pd.testing.assert_categorical_equal(cat1, cat2)
