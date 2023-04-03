import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a dataframe
df = pd.DataFrame({'Age': [25, 30, 40], 'Salary': [50000, 60000, 70000]})

# Fit a linear regression model
lr = LinearRegression()
lr.fit(df[['Age']], df['Salary'])

# Predict the salary for a 35 year old
predicted_salary = lr.predict([[35]])
print(predicted_salary)
