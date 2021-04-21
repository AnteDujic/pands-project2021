# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Read the dataset
data = pd.read_csv('irisData.csv')
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]

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
speciesNames = data.groupby ("Iris Species").size().to_string()
speciesDetail = (data.describe(include = ["object"])).loc [["count", "unique", "freq"]]
dataSummary = data.describe ()
dataCorrelation = data.corr()

with open ("analysis.txt", "wt") as f:
    f.write ("Species Info:\n" + str (speciesDetail) + "\n\n")
    f.write ("Species of Iris:\n" + str (speciesNames) + "\n\n")
    f.write ("Data Summary:\n" + str (dataSummary) + "\n\n")
    f.write ("Data correlation:\n" + str (dataCorrelation))

# Histogram (to be customized)
fig, axs = plt.subplots(2, 2)
figsize = (20,20)
fig.suptitle ("IRIS FEATURE DISTRIBIUTION - by species", size = "xx-large")
sns.histplot (data, x = "Sepal Length (cm)", hue = "Iris Species", ax = axs[0,0], multiple = "stack")
axs[0,0].set_title ("SEPAL LENGTH")
sns.histplot (data, x = "Sepal Width (cm)", hue = "Iris Species", ax = axs[0,1], multiple = "stack")
axs[0,1].set_title ("SEPAL WIDTH")
sns.histplot (data, x = "Petal Length (cm)", hue = "Iris Species", ax = axs[1,0], multiple = "stack")
axs[1,0].set_title ("PETAL LENGTH")
sns.histplot (data, x = "Petal Width (cm)", hue = "Iris Species", ax = axs[1,1], multiple = "stack")
axs[1,1].set_title ("PETAL WIDTH")
plt.show()
