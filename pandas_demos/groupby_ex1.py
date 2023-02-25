import pandas as pd
import numpy as np

'''
In this example, we first create a sample DataFrame df that contains the data we want to analyze. We then use the 
groupby method to group the data by the 'Gender' column. Next, we use the agg method to calculate the mean age and 
income for each group. Finally, we print the resulting DataFrame, which shows the mean age and income for each gender.  
Note that you can use any function in the agg method, not just np.mean. You can also group by multiple columns, 
perform multiple operations on each group, and perform custom operations on each group using a lambda function. 
groupby is a very flexible and powerful tool that can be used in many different ways to analyze data in a Pandas 
DataFrame.
'''
# create a sample dataframe
data = {'Gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
        'Age': [25, 32, 45, 19, 28, 36, 50, 42, 33, 27],
        'Income': [50000, 75000, 60000, 30000, 80000, 90000, 40000, 65000, 55000, 70000]}

df = pd.DataFrame(data)

# group the data by gender and calculate the mean age and income for each group
grouped = df.groupby('Gender').agg({'Age': np.mean, 'Income': np.mean})

print(grouped)
