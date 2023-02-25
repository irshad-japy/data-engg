'''
assert_almost_equal: This method is used to compare two float values. It tests for equality within a certain tolerance.
'''

import pandas as pd

value1 = 0.123456789
value2 = 0.123456780

pd.testing.assert_almost_equal(value1, value2, decimal=6)

