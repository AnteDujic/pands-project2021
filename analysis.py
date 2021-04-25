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

# Heat map
def correlation():
    sns.heatmap (data = data.corr(), square = True, annot = True, cmap = "mako")
    plt.xticks (rotation = 45)
    plt.tight_layout()
    plt.savefig ("correlation.png")
    plt.show()

colors = ["#FFB200", "#9FA91F", "#702963"]

# Box plot
def boxPlot():
    fig, axs = plt.subplots(1, 4, figsize = (12,7))
    fig.suptitle ("IRIS FLOWER BOXPLOT", size = "xx-large")
    sns.boxplot (data = data, x = "Iris Species", y = "Sepal Length (cm)", palette = colors, ax = axs[0])
    sns.boxplot (data = data, x = "Iris Species", y = "Sepal Width (cm)", palette = colors, ax = axs[1])
    sns.boxplot (data = data, x = "Iris Species", y = "Petal Length (cm)", palette = colors, ax = axs[2])
    sns.boxplot (data = data, x = "Iris Species", y = "Petal Width (cm)", palette = colors, ax = axs[3])
    plt.tight_layout()
    plt.savefig ("boxPlots.png")
    plt.show()

# Bar plot
def speciesPlot():
    speciesNumber = data.groupby ("Iris Species").size()
    speciesNumber.plot.bar (color = colors)
    plt.tight_layout()
    plt.savefig ("speciesBar.png")
    plt.show()
    speciesNumber.plot.pie (autopct="%.1f%%", colors = colors).set_ylabel("")
    plt.savefig ("speciesPie.png")
    plt.show()

# Histograms
def histograms():
    sns.histplot (data, x = "Sepal Length (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("SEPAL LENGTH")
    plt.savefig ("Sepal_length.png")
    plt.show()
    sns.histplot (data, x = "Sepal Width (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("SEPAL WIDTH")
    plt.savefig ("Sepal_width.png")
    plt.show()
    sns.histplot (data, x = "Petal Length (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("PETAL LENGTH")
    plt.savefig ("Petal_length.png")
    plt.show()
    sns.histplot (data, x = "Petal Width (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("PETAL WIDTH")
    plt.savefig ("Petal_width.png")
    plt.show()

# Scatterplots
def scatterlots():
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Sepal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs SEPAL WIDTH")
    plt.savefig ("Sepal_length_vs_Sepal_width.png")
    plt.show()
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Length (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs PETAL LENGTH")
    plt.savefig ("Sepal_length_vs_Petal_length.png")
    plt.show()
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs PETAL WIDTH")
    plt.savefig ("Sepal_length_vs_Petal_Width.png")
    plt.show()
    sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Length (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL WIDTH vs PETAL LENGTH")
    plt.savefig ("Sepal_Width_vs_Petal_length.png")
    plt.show()
    sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL WIDTH vs PETAL WIDTH")
    plt.savefig ("Sepal_width_vs_Petal_width.png")
    plt.show()
    sns.scatterplot (data = data, x = "Petal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("PETAL LENGTH vs PETAL WIDTH")
    plt.savefig ("scatterplot.png")
    plt.show()

# Pairplot
def pairplot():
    sns.pairplot (data, hue = "Iris Species", diag_kind = "hist", palette = colors)
    plt.savefig ("pairplot.png")
    plt.show()

# Calling functions
correlation()
boxPlot()
speciesPlot()
histograms()
scatterlots()
pairplot()
