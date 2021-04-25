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

Program starts by importing the dataset. The dataset used for this analysis is stored in this repository.

*CODE:*
```python
data = pd.read_csv('irisData.csv')
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]
```

Dataset gets imported using *read_csv* from *pandas*. Because the irisData.csv file is located in the same directory as the program analysis.py, it is not necessary to define the .csv file path and only name is used to read the file. Different names were assigned to the columns. This is done for the visual purposes only (.txt file and plots) and those names will be used further in the code.

## **REFERENCES**
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://archive.ics.uci.edu/ml/datasets/iris
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

https://www.mygreatlearning.com/blog/open-source-python-libraries/
https://cs231n.github.io/python-numpy-tutorial/#numpy
https://en.wikipedia.org/wiki/Pandas_(software)
https://matplotlib.org/
https://matplotlib.org/stable/tutorials/introductory/pyplot.html

