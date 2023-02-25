'''
assert_extension_array_equal: This method is used to compare two pandas ExtensionArray objects. It tests for equality
of the values, dtype, and attributes.
'''

import pandas as pd
import numpy as np

ea1 = pd.array([1, 2, 3], dtype=np.int64)
ea2 = pd.array([1, 2, 3], dtype=np.int64)

pd.testing.assert_extension_array_equal(ea1, ea2)
