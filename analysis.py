# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Read the dataset
data = pd.read_csv('irisData.csv')

# Layout of the data (to be reviewed - merge with other text file)
def dataLayout():
    l = ("\nDATASET LAYOUT\n")
    l += ("\nThis data set consists of {} samples, grouped by {} different variables:\n".format ((data.shape[0]), (data.shape[1])))
    l += "\n".join (data.columns)
    l += ("\n\nThe general layout of the data: \n\n{}\n*First 10 rows \n\n{}\n*Random 10 rows" .format ((data.head(10)), data.sample(10)))
    return l

layout = dataLayout()
with open ("layout.txt", "wt") as f:
    f.write (str (layout))

# Summary data
speciesNames = data.groupby ("species").size().to_string()
speciesDetail = (data.describe(include = ["object"])).loc [["count", "unique", "freq"]]
dataSummary = data.describe ()
dataCorrelation = data.corr()

with open ("analysis.txt", "wt") as f:
    f.write ("Species Info:\n" + str (speciesDetail) + "\n\n")
    f.write ("Species of Iris:\n" + str (speciesNames) + "\n\n")
    f.write ("Data Summary:\n" + str (dataSummary) + "\n\n")
    f.write ("Data correlation:\n" + str (dataCorrelation))

# Histogram (to be optimized)

sepalLength = data ["sepal_length"]
sepalWidth = data ["sepal_width"]
petalLength = data["petal_length"]
petalWidth = data ["petal_width"]
species = data ["species"]


# seaborn (better solution?)
fig, axs = plt.subplots(2, 2)
figsize = (20,20)
sns.histplot (data, x = "sepal_length", hue = "species", ax = axs[0,0], multiple = "stack")
sns.histplot (data, x = "sepal_width", hue = "species", ax = axs[0,1], multiple = "stack")
sns.histplot (data, x = "petal_length", hue = "species", ax = axs[1,0], multiple = "stack")
sns.histplot (data, x = "petal_width", hue = "species", ax = axs[1,1], multiple = "stack")
plt.show()
