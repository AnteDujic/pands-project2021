# Program that analyses iris data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

y = (data.groupby ("species").size()).to_string()   #dict or array
print (y)

# print (data.describe())
# summary = (data.describe(include = ["object"]))
# print (summary.loc [["count", "unique", "freq"]])



# print(data.to_string()) 

# a = (data.describe(include = ["object"]))
# print (a)
#print (data.describe(include = "all"))          # summary

# print (data.sample (10))        # ten random

# print (data.columns)              # columns

# print (data.shape)               # rows and columns

# print (a.loc [["count", "unique", "freq"]])


# species = data.groupby ("species").describe().transpose()
# print (species)

#count = data.count (axis = "columns")

#print (count)


"""
x = data.describe()

f = open("myfile.txt", "w")

f = open("myfile.txt", "a")
f.write(str (summary))
f.close()

"""


"""
REFERENCES:
- read CSV: https://www.w3schools.com/python/pandas/pandas_csv.asp
- dataset download: https://gist.github.com/curran/a08a1080b88344b0c8a7
- describe() - https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm
"""