# PROGRAMING AND SCRIPTING
# PROJECT
## AUTHOR: ANTE DUJIC

This repository contains the code written as a project for Programing and Scripting Module. The project is to show how Pyton can be used to analyse the Iris flower data set.

## **INTRODUCTION**

The Iris flower data set, aslo called Fisher's Iris data set, is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in 1936. The dataset consists of 150 instances, made up of 50 samples each of 3 species of iris.

There were 4 features measured from each sample:
1. Sepal length in cm's
2. Sepal width in cm's
3. Petal length in cm's
4. Petal width in cm's

Based on the combination of these four features, we can distinguish 3 species of iris:
1. Iris Setosa
2. Iris Versicolour
3. Iris Virginica

The dataset is often used in data mining, classification and clustering examples and to test algorithms.


## **DATASET ANALYSIS**

Many others have done the analysis of the Iris Dataset before and it has been aproached in many different ways. Further in this Readme file will be explained how Python can be used to achive the same.

### **LIBRARIES**

Python Libraries are a set of useful functions that eliminate the need for writing codes from scratch. There are over 137,000 python libraries present today. Libraries used for this analysis are listed below.

- **NumPy** - the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.
- **Pandas** -  a library for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.
- **Matplotlib.pyplot** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
- **Seaborn** - a data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

*CODE:*
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

To allow the usage of the mentioned libaries they first need to be imported. That is done with *import* statement, at the start of the program. Where it is not essential, it is a common practice to assign abbreviation for the each libary using *as* statement. This abbreviation will be used further in the program. 

### **DATASET IMPORT**

Program starts by importing the dataset *irisData.csv*. It is stored in this repository.

*CODE:*
```python
data = pd.read_csv('irisData.csv')
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]
```

Dataset gets imported using *read_csv* from *pandas*. Because the *irisData.csv* file is located in the same directory as the program *analysis.py*, it is not necessary to define the .csv file path and only name is used to read the file. Also, different names were assigned to the columns. This is done for the visual purposes only (.txt file and plots) and those names will be used further in the code.

### **DATASET SUMMARY**

Summary of the dataset contains the basic information on the given dataset and the analysis of the data contained within. It is outputted to the *summary.txt* file. This file is also stored in this repository.

*CODE:*
```python
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
```
To create a file and work with it *open()* function is used. The best practice is to use the *with open()* format, as this closes the file automatically at the end. It is also specified that this file is opened for writing (*w* - also creates the file if it doesn't exist) and it is to be opened in text mode (*t*). *f* is assigned to this file and it is used further in the code. File name created and the one to be written to is defined as *summary.txt*. To write to this file *write()* method is used. The methods to get specific data from the dataset and its analysis is listed below. To get a better visualisation and make the .txt file easily readable, certain options are used in combinaton with those methods.

- *shape()* returns the shape of an array (dataset) - *shape[0]* gives the number of rows, and *shape[1]* the number of columns

<details>
<summary>OUTPUT</summary>
<br>
This data set consists of 150 samples, grouped by 5 different variables.

Dataset variables are:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Iris SpeciesThis is how you dropdown.
</details>

- *columns()* gives the names of the columns. *join()* takes all items and joins them into one string and is used here to list column names in a tidy fashion
- *describe()* gives the summary of the numeric and object values in the given dataset. For the object values it is the count number (*count*), the number of unique values (*unique*), values frequency (*freq*) and the most common value (*top*). *describe(include = ["object"])* includes object data only (strings or timestamps) - "Iris Species" column. *loc* is used to access a group of columns (or rows). Only *count*, *unique* and *top* values are specified for the output as the *top* return different values every time program is run, due to the same number of all 3 values (species).
- *groupby* is used to specify the group of values, Iris Species in this case. *size()* is used to count the elements of the given data. *to_string()* is used to remove "dtype: int64" from the output, as this information is considered irrelevant for a common user, who this analysis is designed for.
- *head()* returns the specified number of rows - 10 in this case.
- *sample()* returns the specified length in random fashion - 10 in this case
- *describe()* default output is summary of the numeric data. It shows the count of variables and calculates the mean, standard deviation, minimum and maximum value, and also 1st, 2nd and 3rd percentile.
- *data.groupby ("Iris Species").describe().transpose()*




## **REFERENCES**
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://archive.ics.uci.edu/ml/datasets/iris
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

https://www.mygreatlearning.com/blog/open-source-python-libraries/
https://cs231n.github.io/python-numpy-tutorial/#numpy
https://en.wikipedia.org/wiki/Pandas_(software)
https://matplotlib.org/
https://matplotlib.org/stable/tutorials/introductory/pyplot.html

