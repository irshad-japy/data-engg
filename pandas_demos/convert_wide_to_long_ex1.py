import pandas as pd

'''
In this example, the original dataframe is in wide format, with different columns for each year/metric combination. The 
pd.melt() function is used to convert the dataframe to long format, with a single column for the metric/year combination
 and another column for the corresponding value. The id_vars argument specifies which columns should be kept as 
 identifier variables, while the value_vars argument specifies which columns should be converted to a long format. The 
 var_name argument specifies the name of the column that will contain the metric/year combination, while the value_name 
 argument specifies the name of the column that will contain the corresponding values.

The resulting long-format dataframe will have four columns: name, metric_year, value, and variable. The name column 
contains the unique identifiers, the metric_year column contains the metric/year combinations 
(e.g., "age_2020", "age_2021", etc.), the value column contains the corresponding values, and the variable column 
contains the original column names from the wide-format dataframe (e.g., "age_2020", "age_2021", etc.).
'''
# Create a sample dataframe
data = {
    'name': ['Alice', 'Bob'],
    'age_2020': [25, 30],
    'age_2021': [26, 31],
    'salary_2020': [50000, 60000],
    'salary_2021': [55000, 65000]
}
df = pd.DataFrame(data)

# Convert from wide to long format
id_vars = ['name']
value_vars = ['age_2020', 'age_2021', 'salary_2020', 'salary_2021']
var_name = 'metric_year'
value_name = 'value'
df_long = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

# Print the result
print(df_long)
