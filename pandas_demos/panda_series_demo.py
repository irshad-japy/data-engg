import pandas as pd

# create a Pandas series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# create a list
l = [2, 4, 6, 8, 10]

# use the isin() function to check if elements of s are present in the list
result = s.isin(l)

# print the result
print(result)
