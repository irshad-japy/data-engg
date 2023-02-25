import pandas as pd
import unittest


def cartesian_product(df1, df2):
    df1 = df1.copy()
    df2 = df2.copy()
    df1['key'] = 0
    df2['key'] = 0
    return pd.merge(left=df1, right=df2, on='key').drop(columns=['key'])


class TestCartesianProduct(unittest.TestCase):

    def test_cartesian_product(self):
        df1 = pd.DataFrame({'A': [1, 2]})
        df2 = pd.DataFrame({'B': [3, 4]})
        expected_result = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [3, 4, 3, 4]})
        result = cartesian_product(df1, df2)
        pd.testing.assert_frame_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
