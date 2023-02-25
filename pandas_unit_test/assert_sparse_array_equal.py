'''
assert_sparse_array_equal: This method is used to compare two pandas SparseArray objects. It tests for equality of the
values, fill_value, dtype, and sparse index.
'''

import pandas as pd

sa1 = pd.SparseArray([1, 2, 3], fill_value=0)
sa2 = pd.SparseArray([1, 2, 3], fill_value=0)

pd.testing.assert_sparse_array_equal(sa1, sa2)
