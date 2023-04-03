import pandas as pd

df = pd.DataFrame({'FundName': ['Fund A', 'Fund B', 'Fund C', 'Fund D'],
                   'FundRisk': ['High', 'Medium', 'Low', 'High']})

risk_scale_map = {'High': 3, 'Medium': 2, 'Low': 1}

df['FundRiskLevel'] = df['FundRisk'].map(risk_scale_map)

print(df)
