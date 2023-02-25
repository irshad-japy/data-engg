'''
assert_index_equal: This method is used to compare two pandas Index objects. It tests for equality of the values and name.
'''

import pandas as pd

index1 = pd.Index([1, 2, 3])
index2 = pd.Index([1, 2, 3])

pd.testing.assert_index_equal(index1, index2)
