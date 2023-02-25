# assert_series_equal
'''
there are other methods in the pd.testing module that you can use for unit testing in pandas. Here are a few examples:
assert_series_equal: This method is used to compare two pandas Series. It tests for equality of the values, dtype, and
index.
'''
import pandas as pd

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([1, 2, 3])

pd.testing.assert_series_equal(s1, s2)


