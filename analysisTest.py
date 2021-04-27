# Program that analyses iris data set
# Author: Ante Dujic

import pandas as pd

"""
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

# Other code - to be considered
"""
speciesName = data.groupby ("species").describe().transpose()
print (speciesName)
"""

"""
plt.hist (sepalLength, bins = 20, color = "red", alpha = 0.5)
plt.show()
plt.hist (sepalWidth, bins = 20, color = "green", alpha = 0.5)
plt.hist (petalLength, bins = 20, color = "blue", alpha = 0.5)
plt.hist (petalWidth, bins = 20, color = "yellow", alpha = 0.5)
"""
   
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
"""









# Histogram (to be customized)
fig, axs = plt.subplots(2, 2)
figsize = (20,20) # not needed
fig.suptitle ("IRIS FEATURE DISTRIBIUTION - by species", size = "xx-large")
sns.histplot (data, x = "Sepal Length (cm)", hue = "Iris Species", ax = axs[0,0], multiple = "stack")
axs[0,0].set_title ("SEPAL LENGTH")
sns.histplot (data, x = "Sepal Width (cm)", hue = "Iris Species", ax = axs[0,1], multiple = "stack")
axs[0,1].set_title ("SEPAL WIDTH")
sns.histplot (data, x = "Petal Length (cm)", hue = "Iris Species", ax = axs[1,0], multiple = "stack")
axs[1,0].set_title ("PETAL LENGTH")
sns.histplot (data, x = "Petal Width (cm)", hue = "Iris Species", ax = axs[1,1], multiple = "stack")
axs[1,1].set_title ("PETAL WIDTH")
plt.savefig ("histograms.png")
plt.show()

# Scatterplot (to be customized)
fig, axs = plt.subplots(2, 3)
figsize = (20,20)
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Sepal Width (cm)", hue = "Iris Species", ax = axs[0,0])
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Length (cm)", hue = "Iris Species", ax = axs[0,1])
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", ax = axs[1,0])
sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Length (cm)", hue = "Iris Species", ax = axs[1,1])
sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Width (cm)", hue = "Iris Species", ax = axs[0,2])
sns.scatterplot (data = data, x = "Petal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", ax = axs[1,2])
plt.savefig ("scatterplot.png")
plt.show()

# Pairplot (use as a summary of all plots)
figsize = (20,20)
sns.pairplot (data, hue = "Iris Species", diag_kind = "hist")
plt.savefig ("pairplot.png")
plt.show()

"""
speciesNumber = data.groupby ("Iris Species").size()
speciesNumber.plot.bar (color = ["green", "red", "blue"])
plt.show()

g = sns.PairGrid (data = data, vars = ["Sepal Length (cm)", "Sepal Width (cm)"], hue = "Iris Species")
g.map (sns.scatterplot)
plt.show()
"""



# DROP DOWN
<details>
<summary>Code comments</summary>
<br>



</details>