# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

# Importing libraries to allow their functions to be used further in the program
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the dataset (.csv file)
    # assigning data from the file to a "data" variable - used when refering to data in code
data = pd.read_csv('irisData.csv')
# Changing the name of the columns (variables) and they will
    #  be used when calling those variables
    #  be outputted
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]

# Summary data - creating and writting to a .txt file
    # w - write (create if file doesn't exist)
    # t - text file
with open ("summary.txt", "wt") as f:
    # Writing to files
        # shape[0] gives the number of rows, and shape[1] the number of columns
    f.write ("\nThis data set consists of {} samples, grouped by {} different variables.".format ((data.shape[0]), (data.shape[1])) + "\n\n")
        # columns() gives the names of the columns
        # join() takes all items and joins them into one string
    f.write ("Dataset variables are:\n" + "\n".join (data.columns) + "\n\n")
        # describe() gives the summary of the numeric and object values in the given dataset
            # describe(include = ["object"]) includes object data only - "Iris Species" column
            # loc accesses a group of columns - only access count, unique, freq
    f.write (str ((data.describe(include = ["object"])).loc [["count", "unique", "freq"]]) + "\n\n")
        # groupby is used to specify the group of values
            # size() is used to count the elements of the given dat
            # to_string() is used to remove "dtype: int64" from the output
    f.write (str (data.groupby ("Iris Species").size().to_string()) + "\n\n")
        # head() returns the specified number of rows - 10
    f.write ("Iris Dataset - first 10 rows:\n" + str(data.head(10)) + "\n\n")
        # sample() returns the specified length in random fashion - 10
    f.write ("Iris Dataset - random 10 rows:\n" + str (data.sample(10)) + "\n\n")
        # describe() gives the summary of the numeric data by default
    f.write ("Data Summary:\n" + str (data.describe()) + "\n\n")
        # combination of groupby() and describe()
            # transpose() swaps rows and columns
    f.write ("Data Summary by species:\n" + str (data.groupby ("Iris Species").describe().transpose()) + "\n\n")
        # corr() is used to find correlation between numeric values
    f.write ("Data correlation:\n" + str (data.corr()))

# Assigning colors for the plots
colors = ["#FFB200", "#9FA91F", "#702963"]

# Bar plot function
def speciesPlot():
    # Assigning only Iris Species column for plot output
    speciesNumber = data.groupby ("Iris Species").size()
    # Creating bar plot
    speciesNumber.plot.bar (color = colors)
    # Fitting plot
    plt.tight_layout()
    # Saving image
    plt.savefig ("speciesBar.png")
    # Plot preview
    plt.show()
    # Creating pie plot
        # autopct="%.1f%%" gives percentages
        # set_ylabel("") removes y axis name
    speciesNumber.plot.pie (autopct="%.1f%%", colors = colors).set_ylabel("")
    # Saving image
    plt.savefig ("speciesPie.png")
    # Plot preview
    plt.show()

# Box plot function
def boxPlot():
    # Creating a grid for multiple plot display at once
        # 1x4 grid
        # 12 x 7 inches image
    fig, axs = plt.subplots(1, 4, figsize = (12,7))
    # Main title name and size
    fig.suptitle ("IRIS FLOWER BOXPLOT", size = "xx-large")
    # 1st boxplot + customization
    sns.boxplot (data = data, x = "Iris Species", y = "Sepal Length (cm)", palette = colors, ax = axs[0])
    # 2nd boxplot + customization
    sns.boxplot (data = data, x = "Iris Species", y = "Sepal Width (cm)", palette = colors, ax = axs[1])
    # 3rd boxplot + customization
    sns.boxplot (data = data, x = "Iris Species", y = "Petal Length (cm)", palette = colors, ax = axs[2])
    # 4th boxplot + customization
    sns.boxplot (data = data, x = "Iris Species", y = "Petal Width (cm)", palette = colors, ax = axs[3])
    # Fitting plot
    plt.tight_layout()
    # Saving plot
    plt.savefig ("boxPlots.png")
    # Plot preview
    plt.show()

# Heat map function
def correlation():
    # Creating heatmap + customization
    sns.heatmap (data = data.corr(), square = True, annot = True, cmap = "mako")
    # Rotate x axis names
    plt.xticks (rotation = 45)
    # Fitting plot
    plt.tight_layout()
    # Saving image
    plt.savefig ("correlation.png")
    # Plot Preview
    plt.show()

# Histograms function
def histograms():
    # Creating plot 1 + customization
    sns.histplot (data, x = "Sepal Length (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("SEPAL LENGTH")
    # Saving image
    plt.savefig ("Sepal_length.png")
    # Plot preview
    plt.show()
    # Creating plot 2 + customization
    sns.histplot (data, x = "Sepal Width (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("SEPAL WIDTH")
    # Saving image
    plt.savefig ("Sepal_width.png")
    # Plot preview
    plt.show()
    # Creating plot 3 + customization
    sns.histplot (data, x = "Petal Length (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("PETAL LENGTH")
    # Saving image
    plt.savefig ("Petal_length.png")
    # Plot preview
    plt.show()
    # Creating plot 4 + customization
    sns.histplot (data, x = "Petal Width (cm)", hue = "Iris Species", multiple = "stack", palette = colors).set_title ("PETAL WIDTH")
    # Saving image
    plt.savefig ("Petal_width.png")
    # Plot preview
    plt.show()

# Scatterplots functions
def scatterlots():
    # Creating plot 1 + customization
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Sepal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs SEPAL WIDTH")
    # Saving image
    plt.savefig ("Sepal_length_vs_Sepal_width.png")
    # Plot preview
    plt.show()
    # Creating plot 2 + customization
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Length (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs PETAL LENGTH")
    # Saving image
    plt.savefig ("Sepal_length_vs_Petal_length.png")
    # Plot preview
    plt.show()
    # Creating plot 3 + customization
    sns.scatterplot (data = data, x = "Sepal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL LENGTH vs PETAL WIDTH")
    # Saving image
    plt.savefig ("Sepal_length_vs_Petal_Width.png")
    # Plot preview
    plt.show()
    # Creating plot 4 + customization
    sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Length (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL WIDTH vs PETAL LENGTH")
    # Saving image
    plt.savefig ("Sepal_Width_vs_Petal_length.png")
    # Plot preview
    plt.show()
    # Creating plot 5 + customization
    sns.scatterplot (data = data, x = "Sepal Width (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("SEPAL WIDTH vs PETAL WIDTH")
    # Saving image
    plt.savefig ("Sepal_width_vs_Petal_width.png")
    # Plot preview
    plt.show()
    # Creating plot 6 + customization
    sns.scatterplot (data = data, x = "Petal Length (cm)", y = "Petal Width (cm)", hue = "Iris Species", palette = colors).set_title ("PETAL LENGTH vs PETAL WIDTH")
    # Saving image
    plt.savefig ("Petal_Length_vs_Petal_width.png")
    # Plot preview
    plt.show()

# Pairplot
def pairplot():
    # Creating plot + customization
    sns.pairplot (data, hue = "Iris Species", diag_kind = "hist", palette = colors)
    # Saving image
    plt.savefig ("pairplot.png")
    # Plot preview
    plt.show()

# Calling functions
speciesPlot()
boxPlot()
correlation()
histograms()
scatterlots()
pairplot()
