# Program that analyses iris data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

# y = (data.groupby ("species").size()).to_string()   #dict or array
# print (y)

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


   
def dataAnalysis():
    species = (data.describe(include = ["object"]))
    
    grouped = data.groupby ("species").describe().transpose()
    return ((species.loc [["count", "unique", "freq"]]), (grouped))



analysis = dataAnalysis()
with open ("analysis.txt", "wt") as f:
    f.write (str (analysis))




"""
speciesColumn = (data.describe(include = ["object"]))
print (speciesColumn.loc [["count", "unique", "freq"]])
unique = int (speciesColumn.loc [["unique"]].values[0])
frequency = int (speciesColumn.loc [["freq"]].values[0])
total = int (speciesColumn.loc [["count"]].values[0])

print ("There are {} different flowers in total, grouped into {} species. There are {} flowers in each species." .format (total, unique, frequency))

speciesName = data.groupby ("species").describe().transpose()
print (speciesName)
"""










count = data.count (axis = "columns")

print (count)

print(data.info())

print (data.corr())

"""
x = data.describe()

f = open("myfile.txt", "w")

f = open("myfile.txt", "a")
f.write(str (summary))
f.close()

with open ("layout.txt", "wt") as f:
    f.write (str (dataLayout()))


"""


"""
REFERENCES:
- read CSV: https://www.w3schools.com/python/pandas/pandas_csv.asp
- dataset download: https://gist.github.com/curran/a08a1080b88344b0c8a7
- describe() - https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm
"""