import pandas as pd

# Create a sample long-format dataframe
data = {
    'id': [1, 1, 2, 2],
    'subject': ['score_math', 'score_english', 'score_math', 'score_english'],
    'score': [90, 80, 85, 90]
}
df_long = pd.DataFrame(data)

# Convert from long to wide format
df_wide = df_long.set_index(['id', 'subject']).unstack()

# Print the result
print(df_wide)
