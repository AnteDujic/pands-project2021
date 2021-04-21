# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the dataset
data = pd.read_csv('irisData.csv')
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]

# Summary data

with open ("summary.txt", "wt") as f:
    f.write ("\nThis data set consists of {} samples, grouped by {} different variables.".format ((data.shape[0]), (data.shape[1])) + "\n\n")
    f.write ("Dataset variables are:\n" + "\n".join (data.columns) + "\n\n")
    f.write (str ((data.describe(include = ["object"])).loc [["count", "unique", "freq"]]) + "\n\n")
    f.write (str (data.groupby ("Iris Species").size().to_string()) + "\n\n")
    f.write ("Iris Dataset - first 10 rows:\n" + str(data.head(10)) + "\n\n")
    f.write ("Iris Dataset - random 10 rows:\n" + str (data.sample(10)) + "\n\n")
    f.write ("Data Summary:\n" + str (data.describe()) + "\n\n")
    f.write ("Data Summary by species:\n" + str (data.groupby ("Iris Species").describe().transpose()) + "\n\n")
    f.write ("Data correlation:\n" + str (data.corr()))

# Bar plot
figsize = (20,20)
speciesNumber = data.groupby ("Iris Species").size()
speciesNumber.plot.bar (color = ["green", "red", "blue"])
plt.tight_layout()
#plt.savefig ("species_bar.png")
plt.show()


# Histogram (to be customized)

figsize = (20,20)
sns.histplot (data, x = "Sepal Length (cm)", hue = "Iris Species", multiple = "stack").set_title ("SEPAL LENGTH")
plt.show()
sns.histplot (data, x = "Sepal Width (cm)", hue = "Iris Species", multiple = "stack").set_title ("SEPAL WIDTH")
plt.show()
sns.histplot (data, x = "Petal Length (cm)", hue = "Iris Species", multiple = "stack").set_title ("PETAL LENGTH")
plt.show()
sns.histplot (data, x = "Petal Width (cm)", hue = "Iris Species", multiple = "stack").set_title ("PETAL WIDTH")
#plt.savefig ("histograms.png")
plt.show()

# Scatterplot (to be customized)
figsize = (20,20)
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Sepal Width (cm)", hue = "Iris Species").set_title ("SEPAL LENGTH vs SEPAL WIDTH")
plt.show()
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Length (cm)", hue = "Iris Species").set_title ("SEPAL LENGTH vs PETAL LENGTH")
plt.show()
sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species").set_title ("SEPAL LENGTH vs PETAL WIDTH")
plt.show()
sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Length (cm)", hue = "Iris Species").set_title ("SEPAL WIDTH vs PETAL LENGTH")
plt.show()
sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Width (cm)", hue = "Iris Species").set_title ("SEPAL WIDTH vs PETAL WIDTH")
plt.show()
sns.scatterplot (data = data, x = "Petal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species").set_title ("PETAL LENGTH vs PETAL WIDTH")
#plt.savefig ("scatterplot.png")
plt.show()

# Pairplot (use as a summary of all plots)
figsize = (20,20)
sns.pairplot (data, hue = "Iris Species", diag_kind = "hist")
#plt.savefig ("pairplot.png")
plt.show()

"""
speciesNumber = data.groupby ("Iris Species").size()
speciesNumber.plot.bar (color = ["green", "red", "blue"])
plt.show()

g = sns.PairGrid (data = data, vars = ["Sepal Length (cm)", "Sepal Width (cm)"], hue = "Iris Species")
g.map (sns.scatterplot)
plt.show()
"""