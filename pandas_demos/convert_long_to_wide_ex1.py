import pandas as pd


def convert_long_to_wide(df, index, columns, values):
    return pd.pivot_table(df, index=index, columns=columns, values=values)


# example usage
data = {
    'Year': [2010, 2010, 2011, 2011],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'Value': [1, 2, 3, 4]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Convert from long to wide
wide_df = convert_long_to_wide(df, 'Year', 'Month', 'Value')
print("Converted DataFrame (wide format):")
print(wide_df)
