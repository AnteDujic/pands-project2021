# Program that analyses iris data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

# print(data.to_string()) 
print (data.describe())



"""
REFERENCES:
- https://www.w3schools.com/python/pandas/pandas_csv.asp
"""