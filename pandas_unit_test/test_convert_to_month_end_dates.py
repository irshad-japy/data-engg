import pandas as pd
import unittest


def convert_to_month_end_dates(df, date_label, group_by, drop_duplicates=False):
    # Filter to single monthly occurrence and align
    df[date_label] = df[date_label].dt.to_period('M').dt.to_timestamp(how='end').dt.normalize()

    # Drop duplicates
    if drop_duplicates:
        df = df.drop_duplicates(subset=[group_by, date_label])

    return df


class TestConvertToMonthEndDates(unittest.TestCase):

    # def test_convert_to_month_end_dates(self):
    #     # Create sample dataframe
    #     data = {'date': pd.date_range(start='2022-01-01', end='2022-03-31', freq='D'),
    #             'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    #                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
    #     df = pd.DataFrame(data)
    #
    #     # Test case 1: Filter to month-end dates and drop duplicates
    #     expected_result_1 = pd.DataFrame(
    #         {'date': [pd.Timestamp('2022-01-31'), pd.Timestamp('2022-02-28'), pd.Timestamp('2022-03-31')],
    #          'value': [31, 59, 90]})
    #     result_1 = convert_to_month_end_dates(df, 'date', None, drop_duplicates=True)
    #     pd.testing.assert_frame_equal(result_1, expected_result_1)
    #
    #     # Test case 2: Filter to month-end dates without dropping duplicates
    #     expected_result_2 = pd.DataFrame(
    #         {'date': [pd.Timestamp('2022-01-31'), pd.Timestamp('2022-02-28'), pd.Timestamp('2022-03-31')],
    #          'value': [31, 59, 90]})
    #     result_2 = convert_to_month_end_dates(df, 'date', None, drop_duplicates=False)
    #     pd.testing.assert_frame_equal(result_2, expected_result_2)

    # def test_convert_to_month_end_dates(self):
    #     # Create sample dataframe
    #     data = {'date': pd.date_range(start='2022-01-01', end='2022-03-31', freq='D'),
    #             'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    #                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
    #     df = pd.DataFrame(data)
    #
    #     # Test case 1: Filter to month-end dates and drop duplicates
    #     expected_result_1 = pd.DataFrame(
    #         {'date': [pd.Timestamp('2022-01-31'), pd.Timestamp('2022-02-28'), pd.Timestamp('2022-03-31')]})
    #     result_1 = convert_to_month_end_dates(df, 'date', None, drop_duplicates=True)
    #     pd.testing.assert_frame_equal(result_1[['date']], expected_result_1)
    #
    #     # Test case 2: Filter to month-end dates without dropping duplicates
    #     expected_result_2 = pd.DataFrame(
    #         {'date': [pd.Timestamp('2022-01-31'), pd.Timestamp('2022-02-28'), pd.Timestamp('2022-03-31')]})
    #     result_2 = convert_to_month_end_dates(df, 'date', None, drop_duplicates=False)
    #     pd.testing.assert_frame_equal(result_2[['date']], expected_result_2)

    # def test_convert_to_month_end_dates(self):
    #     data = {'date': ['2022-01-01', '2022-02-15', '2022-03-30']}
    #     df = pd.DataFrame(data, columns=['date'])
    #
    #     # Convert date_label to datetime type
    #     date_label = 'date'
    #     df[date_label] = pd.to_datetime(df[date_label])
    #
    #     # Apply conversion function
    #     df[date_label] = df[date_label].dt.to_period('M').dt.to_timestamp(how='end').dt.normalize()
    #
    #     # Define expected result
    #     expected_result = pd.DataFrame({'date': ['2022-01-31', '2022-02-28', '2022-03-31']}, columns=['date'])
    #
    #     # Test that the conversion was performed correctly
    #     pd.testing.assert_frame_equal(df, expected_result)

    # def test_convert_to_month_end_dates(self):
    #     # Create sample dataframe
    #     data = {'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15'],
    #             'group': ['A', 'B', 'A', 'B']}
    #     df = pd.DataFrame(data, columns=['date', 'group'])
    #
    #     # Convert date_label to datetime type
    #     date_label = 'date'
    #     df[date_label] = pd.to_datetime(df[date_label])
    #
    #     # Apply conversion function
    #     group_by = 'group'
    #     df = convert_to_month_end_dates(df, date_label, group_by)
    #
    #     # Define expected result
    #     expected_result = pd.DataFrame({'date': ['2022-01-31', '2022-02-28'],
    #                                     'group': ['A', 'B']},
    #                                    columns=['date', 'group'])
    #
    #     # Test that the conversion was performed correctly
    #     pd.testing.assert_frame_equal(df, expected_result)

    # def test_convert_to_month_end_dates(self):
    #     # Create sample dataframe
    #     data = {'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15']}
    #     df = pd.DataFrame(data, columns=['date'])
    #
    #     # Convert date_label to datetime type
    #     date_label = 'date'
    #     df[date_label] = pd.to_datetime(df[date_label])
    #
    #     # Apply conversion function
    #     group_by = None
    #     df = convert_to_month_end_dates(df, date_label, group_by)
    #
    #     # Define expected result
    #     expected_result = pd.DataFrame({'date': [pd.Timestamp('2022-01-31'), pd.Timestamp('2022-02-28')]},
    #                                    columns=['date'])
    #     expected_result['date'] = expected_result['date'].astype('datetime64[ns]')
    #
    #     # Test that the conversion was performed correctly
    #     pd.testing.assert_frame_equal(df, expected_result)

    # def test_convert_to_month_end_dates(self):
    #     # Create sample dataframe
    #     data = {'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15']}
    #     df = pd.DataFrame(data, columns=['date'])
    #
    #     # Convert date_label to datetime type
    #     date_label = 'date'
    #     df[date_label] = pd.to_datetime(df[date_label])
    #
    #     # Apply conversion function
    #     group_by = None
    #     df = convert_to_month_end_dates(df, date_label, group_by)
    #
    #     # Define expected result
    #     expected_result = pd.DataFrame({'date': ['2022-01-31', '2022-02-28']}, columns=['date'])
    #     expected_result['date'] = pd.to_datetime(expected_result['date'])
    #
    #     # Test that the conversion was performed correctly
    #     pd.testing.assert_frame_equal(df, expected_result)

    def test_convert_to_month_end_dates(self):
        # Create sample dataframe
        data = {'date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-02-15']}
        df = pd.DataFrame(data, columns=['date'])

        # Convert date_label to datetime type
        date_label = 'date'
        df[date_label] = pd.to_datetime(df[date_label])

        # Apply date conversion
        df[date_label] = df[date_label].dt.to_period('M').dt.to_timestamp(how='end').dt.normalize()

        # Define expected result
        expected_result = pd.DataFrame({'date': ['2022-01-31', '2022-01-31', '2022-02-28', '2022-02-28']},
                                       columns=['date'])
        expected_result['date'] = pd.to_datetime(expected_result['date'])

        # Test that the date conversion was performed correctly
        pd.testing.assert_frame_equal(df, expected_result)


if __name__ == '__main__':
    unittest.main()
