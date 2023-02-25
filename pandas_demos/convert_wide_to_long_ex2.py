import pandas as pd

# Create a sample dataframe
data = {
    'id': [1, 2],
    'name': ['Alice', 'Bob'],
    'score_math': [90, 85],
    'score_english': [80, 90]
}
df = pd.DataFrame(data)

# Convert from wide to long format
id_vars = ['id', 'name']
value_vars = ['score_math', 'score_english']
var_name = 'subject'
value_name = 'score'
df_long = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

# Print the result
print(df_long)
