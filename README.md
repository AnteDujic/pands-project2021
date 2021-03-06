# PROGRAMMING AND SCRIPTING | PROJECT | APRIL 2021
### AUTHOR: ANTE DUJIC

This repository contains the analysis of the Iris Flower data set, done as a project for Programming and Scripting Module. The aim of the project is to show how Python can be used to do the analysis.

## **INTRODUCTION**

The Iris flower data set, also called Fisher's Iris data set, is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in 1936. The dataset consists of 150 instances, made up of 50 samples each of 3 species of iris.[1]

There were 4 features measured from each sample:
1. Sepal length in cm's
2. Sepal width in cm's
3. Petal length in cm's
4. Petal width in cm's

Based on the combination of these four features, we can distinguish 3 species of Iris:
1. Iris Setosa
2. Iris Versicolour
3. Iris Virginica

One class, Setosa, is linearly separable from the other two. The latter are not linearly separable from each other.[2] Linearly separable data is data that if graphed in two dimensions, can be separated by a straight line. [3]

![](https://github.com/AnteDujic/pands-project2021/blob/main/Iris%20Flowers.png)

The dataset is often used in data mining, classification and clustering examples and to test algorithms.[4]


## **DATASET ANALYSIS**

Iris Dataset has been analysed many times before, using various tools and approaches. Further down in this Readme file will be explained how Python can be used to achive the same. Dataset Analysis part consists of the codes used to analyse the data, explanation (comments) of the codes, their output and a brief explanation of the output - which should also confirm what we've already learned about the Iris Flowers. It is important to say that the explanation of the code will be very detailed. Where it is not a practice to comment the "simple" code, the aim here is to show the understanding of the code used.

### **LIBRARIES**

Python Libraries are a set of useful functions that eliminate the need for writing codes from scratch. There are over 137,000 python libraries present today. [5] Libraries used for this analysis are listed below.

- **NumPy** - the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. [6]
- **Pandas** -  a library for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.[7]
- **Matplotlib.pyplot** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. [8] matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. [9]
- **Seaborn** - a data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. [10]

*CODE:*
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
<details>
<summary>Code comments</summary>
<br>

To allow the usage of the mentioned libaries they first need to be imported. That is done with *import* statement, at the start of the program. [11] Where it is not essential, it is a common practice to assign abbreviation for the each libary using *as* statement. This abbreviation will be used further in the program. 

</details>

### **DATASET IMPORT**

Program starts by importing the dataset *irisData.csv*. [49] It is saved into this repository.

*CODE:*
```python
data = pd.read_csv('irisData.csv')
data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Iris Species"]
```
<details>
<summary>Code comments</summary>
<br>

Dataset gets imported using *read_csv* from *pandas* [12]. Because the *irisData.csv* file is located in the same directory as the program *analysis.py*, it is not necessary to define the .csv file path and only name is used to read the file. Also, different names were assigned to the columns. This is done for the visual purposes only (.txt file and plots) and those names will be used further in the code.

</details>

### **DATASET SUMMARY**

Summary of the dataset contains the basic information on the given dataset and the analysis of the data contained within. It is outputted to the *summary.txt* file. This file is also saved into this repository.

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
<details>
<summary>Code comments</summary>
<br>

To create a file and work with it *open()* function is used. The best practice is to use the *with open()* format, as this closes the file automatically at the end. It is also specified that this file is opened for writing (*w* - also creates the file if it doesn't exist) and it is to be opened in text mode (*t*). *f* is assigned to this file and it is used further in the code. File name created and the one to be written to is defined as *summary.txt*. To write to this file *write()* method is used. [13] The methods to get specific data from the dataset and its analysis is listed below. To get a better visualisation and make the .txt file easily readable, certain options are used in combinaton with those methods.

</details>

<details>
<summary>Code comments</summary>
<br>

- *shape()* returns the shape of an array (dataset) - *shape[0]* gives the number of rows, and *shape[1]* the number of columns [14]

</details>

```
This data set consists of 150 samples, grouped by 5 different variables.

```

<details>
<summary>Code comments</summary>
<br>

- *columns()* gives the names of the columns. [15] *join()* takes all items and joins them into one string and is used here to list column names in a tidy fashion. [16]

</details>

```
Dataset variables are:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Iris Species
```

<details>
<summary>Code comments</summary>
<br>

- *describe()* gives the summary of the numeric and object values in the given dataset. For the object values it is the count number (*count*), the number of unique values (*unique*), values frequency (*freq*) and the most common value (*top*). *describe(include = ["object"])* includes object data only (strings or timestamps) - "Iris Species" column. [17] *loc* is used to access a group of columns (or rows). [18] Only *count*, *unique* and *top* values are specified for the output as the *top* return different values every time program is run, due to the same number of all 3 values (species).

</details>

```
       Iris Species
count           150
unique            3
freq             50
```

<details>
<summary>Code comments</summary>
<br>

- *groupby* is used to specify the group of values, Iris Species in this case. [19] *size()* is used to count the elements of the given data. [20] *to_string()* is used to remove "dtype: int64" from the output, as this information is considered irrelevant for a common user, who this analysis is designed for. [21]

</details>

```
Iris Species
setosa        50
versicolor    50
virginica     50
```

<details>
<summary>Code comments</summary>
<br>

- *head()* returns the specified number of rows - 10 in this case. [22]

</details>

```
Iris Dataset - first 10 rows:
   Sepal Length (cm)  Sepal Width (cm)  Petal Length (cm)  Petal Width (cm) Iris Species
0                5.1               3.5                1.4               0.2       setosa
1                4.9               3.0                1.4               0.2       setosa
2                4.7               3.2                1.3               0.2       setosa
3                4.6               3.1                1.5               0.2       setosa
4                5.0               3.6                1.4               0.2       setosa
5                5.4               3.9                1.7               0.4       setosa
6                4.6               3.4                1.4               0.3       setosa
7                5.0               3.4                1.5               0.2       setosa
8                4.4               2.9                1.4               0.2       setosa
9                4.9               3.1                1.5               0.1       setosa
```

<details>
<summary>Code comments</summary>
<br>

- *sample()* returns the specified length in random fashion - 10 in this case [23]

</details>

```
Iris Dataset - random 10 rows:
     Sepal Length (cm)  Sepal Width (cm)  Petal Length (cm)  Petal Width (cm) Iris Species
26                 5.0               3.4                1.6               0.4       setosa
86                 6.7               3.1                4.7               1.5   versicolor
118                7.7               2.6                6.9               2.3    virginica
36                 5.5               3.5                1.3               0.2       setosa
134                6.1               2.6                5.6               1.4    virginica
38                 4.4               3.0                1.3               0.2       setosa
29                 4.7               3.2                1.6               0.2       setosa
54                 6.5               2.8                4.6               1.5   versicolor
104                6.5               3.0                5.8               2.2    virginica
103                6.3               2.9                5.6               1.8    virginica
```

<details>
<summary>Code comments</summary>
<br>

- *describe()* default output is summary of the numeric data. It shows the count of variables and calculates the mean, standard deviation, minimum and maximum value, and also 1st, 2nd and 3rd percentile. [17]

</details>

```
Data Summary:
       Sepal Length (cm)  Sepal Width (cm)  Petal Length (cm)  Petal Width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.054000           3.758667          1.198667
std             0.828066          0.433594           1.764420          0.763161
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000
```

<details>
<summary>Code comments</summary>
<br>

- *groupby()* [19] and *describe()* [17] paired together gave the *describe()* output as described above, but grouped by Iris Species. *transpose()* is used to swap rows and columns. [24] This was done for visual purposes only.

</details>

```
Data Summary by species:
Iris Species                setosa  versicolor  virginica
Sepal Length (cm) count  50.000000   50.000000  50.000000
                  mean    5.006000    5.936000   6.588000
                  std     0.352490    0.516171   0.635880
                  min     4.300000    4.900000   4.900000
                  25%     4.800000    5.600000   6.225000
                  50%     5.000000    5.900000   6.500000
                  75%     5.200000    6.300000   6.900000
                  max     5.800000    7.000000   7.900000
Sepal Width (cm)  count  50.000000   50.000000  50.000000
                  mean    3.418000    2.770000   2.974000
                  std     0.381024    0.313798   0.322497
                  min     2.300000    2.000000   2.200000
                  25%     3.125000    2.525000   2.800000
                  50%     3.400000    2.800000   3.000000
                  75%     3.675000    3.000000   3.175000
                  max     4.400000    3.400000   3.800000
Petal Length (cm) count  50.000000   50.000000  50.000000
                  mean    1.464000    4.260000   5.552000
                  std     0.173511    0.469911   0.551895
                  min     1.000000    3.000000   4.500000
                  25%     1.400000    4.000000   5.100000
                  50%     1.500000    4.350000   5.550000
                  75%     1.575000    4.600000   5.875000
                  max     1.900000    5.100000   6.900000
Petal Width (cm)  count  50.000000   50.000000  50.000000
                  mean    0.244000    1.326000   2.026000
                  std     0.107210    0.197753   0.274650
                  min     0.100000    1.000000   1.400000
                  25%     0.200000    1.200000   1.800000
                  50%     0.200000    1.300000   2.000000
                  75%     0.300000    1.500000   2.300000
                  max     0.600000    1.800000   2.500000
```

<details>
<summary>Code comments</summary>
<br>

- *corr()* is used to find correlation between numeric values - Sepal Length (cm), Sepal Width (cm), Petal Length (cm), Petal Width (cm). [25]

</details>

```
Data correlation:
                   Sepal Length (cm)  Sepal Width (cm)  Petal Length (cm)  Petal Width (cm)
Sepal Length (cm)           1.000000         -0.109369           0.871754          0.817954
Sepal Width (cm)           -0.109369          1.000000          -0.420516         -0.356544
Petal Length (cm)           0.871754         -0.420516           1.000000          0.962757
Petal Width (cm)            0.817954         -0.356544           0.962757          1.000000

```

### **DATASET VISUALISATION**

Python, with its libraries, is a powerful tool for a data visualisation. There are multiple ways and aproaches but the following ones were deemed the best for the given data:
- bar plot and pie plot
- boxplots
- correlation heat map
- histograms
- scatterplots
- pairplot

Each visual represantation (plot) has been defined as a function using *def* keyword. [26] Those functions are called at the end of the program. Mentioned plots have also been customized for the easier interpretation and a better visual appeal (e.g. titles, font size, color palette, etc.) Where there are multiple options available in Python for visual plot customization, minimum number was used to keep the code short and tidy. All plots are saved as .png images using *plt.savefig()* method. [27] Plots are also displayed using *plt.show()* to give a preview of how the saved images will look like. [28]

*CODE:*
```python
colors = ["#FFB200", "#9FA91F", "#702963"]
```
<details>
<summary>Code comments</summary>
<br>

*color* variable is defined to minimize the code, and to assign the same colors for the same species in each plot. Color codes (hex triplet) were used to give specific color values. [29]

</details>

#### BAR PLOT & PIE PLOT

A bar plot represents an estimate of central tendency for a numeric variable with the height of each rectangle. [30] A pie plot is a circular statistical graphic, which is divided into slices to illustrate numerical proportion. [31]

*CODE:*
```python
def speciesPlot():
    speciesNumber = data.groupby ("Iris Species").size()
    speciesNumber.plot.bar (color = colors)
    plt.tight_layout()
    plt.savefig ("speciesBar.png")
    plt.show()
    speciesNumber.plot.pie (autopct="%.1f%%", colors = colors).set_ylabel("")
    plt.savefig ("speciesPie.png")
    plt.show()
```
<details>
<summary>Code comments</summary>
<br>

Both bar [32] and pie plot [33] are defined under the same function - *speciesPlot()*. First, the data grouped under Iris Species column is defined as a data for the mentioned plots. *color* is also defined for both plots. *plt.tight_layout()* was used for the bar plot to fit to the image cleanly (didn't fit by default). [34] As for the pie plot, *autopct="%.1f%%"* [35] was used to display percentages and *set_ylabel("")* to remove the y axis name, which was deemed unnecesary. [36]

</details>

<p float="left">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/speciesBar.png" width="400" />
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/speciesPie.png" width="400" /> 
</p>

Both the bar and the pie plot are a visual representation of the object data in Iris Species column, which was already written to the *summary.txt* file. It shows there are 3 species of the Iris Flower: Setosa, Versicolor and Virginica and there is an equal number of each - 50. We can also see that each species represents 33,33% of the total number of flowers.

#### BOXPLOT

Box plots are useful as they provide a visual summary of the data enabling researchers to quickly identify mean values, the dispersion of the data set, and signs of skewness. Data shown in the box plot are the minimum score, first (lower) quartile, median, third (upper) quartile, and maximum score. [37]

*CODE:*
```python
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
```
<details>
<summary>Code comments</summary>
<br>

Box plots [38] were displayed as one figure using *subplots()*. The grid was defined to have 1 row and 4 columns, and the *figsize()*, that represents the size of the displayed/saved image, is set up to be 12 inches wide and 7 inches high. The main title is set and also the *size* of the title font. Each boxplot is given its data (full dataset), x and y axis, color and also the position in the grid using *ax = axs[]*. [39] Same as the bar plot, this plot was also fitted better using *plt.tight_layout()*. [34]

</details>

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/boxPlots.png" />
</p>

It is clearly visible that Setosa has the smallest Sepal length, Petal length and Petal width. However, it has the largest Sepal width. Other highest values belong to Virginica. It has the largest Sepal length, Petal length and Petal Width. Versicolor has the smallest Sepal width.

#### CORRELATION HEAT MAP

A correlation heatmap uses colored cells to show a 2D correlation matrix (table) between two discrete dimensions or event types. [40] They show which variables are correlated and to what degree. Correlation ranges from -1 to 1, where correlation closer to 1 indicates there is a strong relationship between values, and closer to -1 indicates there is a higher chance one value will decrease if the other one increases.

*CODE:*
```python
def correlation():
    sns.heatmap (data = data.corr(), square = True, annot = True, cmap = "mako")
    plt.xticks (rotation = 45)
    plt.tight_layout()
    plt.savefig ("correlation.png")
    plt.show()
```
<details>
<summary>Code comments</summary>
<br>

Correlation data outputted before into the *summary.txt* file was visualised using the heat map. *square = True* sets the cells to be squares (rectangles by default), *annot = True* displays values within cells, and color palette (*cmap*) was defined as *mako*. [41] x axis names are rotated by setting *rotation* within *plt.xticks* [42] and the plot was fitted better with *plt.tight_layout()*. [34]

</details>

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/correlation.png" />
</p>

We can see there is a very high correlation between Petal lenght and Petal width. Correlation between Sepal length and both Petal length and width is very high too. On the other side, we can see that Sepal width has negative correlation with all other variables (features), smallest with Sepal length and highest with Petal lenght. It is also visible that Sepal data varies more then the Petal data.

#### HISTOGRAMS

A histogram is an approximate representation of the distribution of numerical data. [43] It is similar to a Bar Plot, but a histogram groups numbers into ranges. The height of each bar shows how many fall into each range. [44]

*CODE:*
```python
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
```
<details>
<summary>Code comments</summary>
<br>

Total of 4 histograms are displayed and saved individually. Data is set to be the dataset imported at the start of the program. *x* axis is set up for each plot, as is the color *palette*. *hue* was used to separate the bars by *Iris Species* and *multiple = "stack"* for different species bar with the same value range to be stacked on top of eachother, instead of overlapping. [45]

</details>

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_length.png" />
</p>

Sepal length values don't fluctuate as much as the other values, which will be visible in the images below. We can see that mainly Setosa has the shortest Sepal, while Viginica has the longest. Virginica Sepal values varies the most.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_width.png" />
</p>

Sepal width values fluctuate more then Sepal length. It is visible there is the most flowers with the Sepal width approx. 3cm, of which most fit under Virginica. As the Sepal width decreases or increases from 3cm the number of flowers decreses. Setosa has the widest Sepal, which confirms the statement from before.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Petal_length.png" />
</p>

It is clearly visible there are the most flowers with the lowest value range, and those are Setosa. Virginica has the longest Petal, but the number of the flowers in the highest range is the smallest of all.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Petal_width.png" />
</p>

Petal width histogram is very similar to the Petal lenght one, which confirms the high correlation between the two values. Setosa, again, stands out as the flower with the smallest width. The number of flowers in the lowest range is the highest.


#### SCATTERPLOTS

A scatterplot is a type of data display that shows the relationship between two numerical variables. Each member of the dataset gets plotted as a point whose (x, y) coordinates relates to its values for the two variables. Scatter plots show how much one variable is affected by another. [46]

*CODE:*
```python
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
    plt.savefig ("Petal_Length_vs_Petal_width.png")
    plt.show()
```
<details>
<summary>Code comments</summary>
<br>

There are total of 12 possible scatterplots to be displayed from the given data - 6 with different values and other 6 with those same values, but inverted axes. Only 6 were defined in the *scatterplot()* function and are displayed/saved individually. Code is very similar to the one on histagrams. Dataset is defined to be *data*, *x* and *y* axes are set up for each plot, as is the color *palette*. *hue* was again used to show the plot output by *Iris Species*. [47]

</details>

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_length_vs_Sepal_width.png" />
</p>

It is clearly visible on this plot, but also on the plots below, how Setosa is easier to distinguish from the other two species. It confirms the statement from the introduction, which says that Setosa is linearly seperable from the other two species. Sepal width of Setosa is trending higher.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_length_vs_Petal_length.png" />
</p>

This plot, again, confirms Setosa flower is different to Versicolor and Virginica. Petal lenght of Setosa is much smaller then on the other flowers. Petal length of Virginica is trending high. Data is also more condensed here, for all three species.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_length_vs_Petal_Width.png" />
</p>

The seperation of Setosa from the other two flowers is even more distinctive in this plot. Where not fully seperable, Versicolor and Virginica are also easier to distinguish then on the previous plots. Setosa has the smalles Petal width and Virginica the largest.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_Width_vs_Petal_length.png" />
</p>

It's even more visible how Setosa has the widest Sepal on this plot and, once again, we can see the clear difference between Setosa and the other two species, Virginica and Versicolor.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Sepal_width_vs_Petal_width.png" />
</p>

Data on this plot is not as condensed when comparing Sepal width and Petal length of the flowers. Petal lenght of Virginica is trending higher and once again we can clearly see how Setosa has the highest Sepal Width.

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/Petal_Length_vs_Petal_width.png" />
</p>

Setosa data is very condensed when comparing two Petal variables. As on all previous plots, we can once more confirm that Setosa is lineraly seperable to the other two flowers. Both Petal Width and Petal Length of Setosa is trending lower.

#### PAIRPLOT

Pairplot is a very useful function in Seaborn. The simplest invocation displays scatterplot for each pairing of the variables and histplot for the marginal plots along the diagonal.[48]

*CODE:*
```python
def pairplot():
    sns.pairplot (data, hue = "Iris Species", diag_kind = "hist", palette = colors)
    plt.savefig ("pairplot.png")
    plt.show()
```
<details>
<summary>Code comments</summary>
<br>

Code for pairplot is very similar to the other Seaborn plot codes. The *data*, *hue* and *palette* are defined, as they were in the other plots shown before. *diag_kind = "hist"* is used to show histograms on the diagonal. Pairplot contains all posible combinations of both mentioned plots. [48]

</details>

<p align="center">
  <img src="https://github.com/AnteDujic/pands-project2021/blob/main/pairplot.png" />
</p>

This plot serves as an overview of the scatterplot and histograms shown before in this analysis. There are 4 different attributes (variables) that were analysed, therefore 12 different scatterplots and 4 different histograms. There are 6 other scatterplots, with inverted axes included, in this pairplot. Also, blocks on histograms are not stacked up, but they overlap. We can see that pairplot is effective way to show the separation of Setosa flower, compared to the other two flowers.


#### CALLING FUNCTIONS

*CODE:*
```python
speciesPlot()
boxPlot()
correlation()
histograms()
scatterlots()
pairplot()
```
<details>
<summary>Code comments</summary>
<br>

For code written under the functions to be executed the functions have to be called. That is done by the name of the function we want to call.

</details>

## **CONCLUSION**

This Readme file shows how Python can be used to analyse the data. It was first explained what the Iris Flower is and what its main characteristics are. It was then shown how program can be written in Python to analyse the given data in details and confirm what was stated in the Introduction. This analysis gave a better understanding of Python as a tool for data analysis but aslo a very good understanding of the Iris Flower dataset.

## **REFERENCES**

### **MAIN**
- [1]   www.wikipedia.org 2021, *Iris flower data set*, Wikipedia, viewed on 25th Mar 2021,  https://en.wikipedia.org/wiki/Iris_flower_data_set
- [2]   www.archive.ics 2021, *Iris Data Set*, R.A.Fisher, viewed on 25th Mar 2021, https://archive.ics.uci.edu/ml/datasets/iris
- [3]   www.jamesmccaffrey.wordpress.com, *The difference between Linearly Seperable Data...*, J.D.McCaffrey, viewed on 28th Apr 2021, https://jamesmccaffrey.wordpress.com/2019/04/27/
- [4]   www.lac.inpe.br 2021, *Data Science Example - Iris Dataset*, Rafael Santos, viewed on 28th Mar 2021, http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
- [5]   www.mygreatlearnings.com 2021, *Open-Source Python Libraries You Should Know About*, V. Advani, viewed on 29th Mar 2021, https://www.mygreatlearning.com/blog/open-source-python-libraries/
- [6]   www.cs231n.github.io 2021, *Python Numpy Tutorial*, J.Johnson, viewed on 30 Mar 2021, https://cs231n.github.io/python-numpy-tutorial/#numpy
- [7]   www.wikipedia.org 2021, *pandas (software)*, wikipedia, viewed on 30 Mar 2021, https://en.wikipedia.org/wiki/Pandas_(software)
- [8]   www.maplotlib.org 2021, *Matplotlib: Visualisation with Python*, J.Hunter et al, viewed on 30 Mar 2021, https://matplotlib.org/
- [9]   www.maplotlib. org 2021, *Pyplot tutorial*, J.Hunter et al, viewed on 30 Mar 2021, https://matplotlib.org/stable/tutorials/introductory/pyplot.html
- [10]  www.seaborn.pydata.org 2021, *Seaborn*, M.Waskom, viewed on 31 Mar 2021, https://seaborn.pydata.org/
- [11]  www.realpython.com 2021, *Python import*, G.A.Hjelle, viewed on 30th Mar 2021, https://realpython.com/python-import/
- [12]  www.realpython.com 2021, *Reading and Writing CSV Files in Python*, J.Fincher, viewed on 1st Apr 2021, https://realpython.com/python-csv/
- [13]  www.programiz.com 2021, *Python File I/O*, Parewa Labs Pvt.Ltd., viewed on 1st Apr 2021, https://www.programiz.com/python-programming/file-operation
- [14]  www.stockoverflow 2021, *What does.shape[] do...*, Stack Exchange (Head and Tail), viewed on 7th Apr 2021, https://stackoverflow.com/questions/10200268/what-does-shape-do-in-for-i-in-rangey-shape0/21200291
- [15]  www.geeksforgeeks.org 2021, *Python|Pandas DataFrame.columns*, S.Ranjan, viewed on 7th Apr, https://www.geeksforgeeks.org/python-pandas-dataframe-columns/
- [16]  www.w3schools.com 2021, *Python String join() Method*, Refsnes Data, viewed on 11th Apr 2021, https://www.w3schools.com/python/ref_string_join.asp
- [17]  www.pandas.pydata.org 2021, *pandas.DataFrame.describe*, Pandas Dev team, viewed on 11th Apr 2021, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- [18]  www.pandas.pydata.org 2021, *pandas.DataFrame.loc*, Pandas Dev team, viewed on 11th Apr 2021, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
- [19]  www.geeksforgeeks.org 2021, *Python|Pandas dataframe.groupby()*, S.Ranjan, viewed on 11th Apr 2021, https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/
- [20]  www.note.nkmk.me 2021, *NumPy:...*, nkmk.me, viewed on 11th Apr 2021, https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/
- [21]  www.stockoverflow 2021, *Remove name, dtype from pandas output of dataframe or series*, Stack Exchange (ALollz), viewed on 11th Apr 2021, https://stackoverflow.com/questions/29645153/remove-name-dtype-from-pandas-output-of-dataframe-or-series?noredirect=1
- [22]  www.w3resources.com 2021, *DataFrame - head() function*, w3resource.com, viewed on 11th Apr 2021, https://www.w3resource.com/pandas/dataframe/dataframe-head.php
- [23]  www.pandas.pydata.org 2021, *pandas.DataFrame.sample*, Pandas Dev team, viewed on 11th Apr 2021, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
- [24]  www.w3resources.com 2021, *NumPy Array manipulation: transpose() function*, w3resource.com, viewed on 11th Apr 2021, https://www.w3resource.com/numpy/manipulation/transpose.php
- [25]  www.geeksforgeeks.org 2021, *Python|Pandas dataframe.corr()*, S.Ranjan, viewed on 11th Apr 2021, https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
- [26]  www.w3schools.com 2021, *Python Functions*, Refsnes Data, viewed on 28th Apr 2021,https://www.w3schools.com/python/python_functions.asp
- [27]   www.maplotlib.org 2021, *matplotlib.pyplot.savefig*, J.Hunter et al, viewed on 21st Apr 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
- [28]  www.maplotlib.org 2021, *matplotlib.pyplot.show*, J.Hunter et al, viewed on 21st Apr 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
- [29]  www.wikipedia.org 2021, *List of colors: A-F*, wikipedia, viewed on 21st Apr 2021, https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F
- [30]  www.seaborn.pydata.org 2021, *seaborn.barplot*, M.Waskom, viewed on 21st Apr 2021, https://seaborn.pydata.org/generated/seaborn.barplot.html
- [31]  www.wikipedia.org 2021, *Pie chart*, wikipedia, viewed on 21st Apr 2021,https://en.wikipedia.org/wiki/Pie_chart
- [32]  www.maplotlib.org 2021, *matplotlib.pyplot.bar*, J.Hunter et al, viewed on 21st Apr 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
- [33]  www.maplotlib.org 2021, *matplotlib.pyplot.pie*, J.Hunter et al, viewed on 21st Apr 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
- [34]  www.maplotlib.org 2021, *Tight Layout guide*, J.Hunter et al, viewed on 21st Apr 2021, https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html
- [35]  www.learningaboutelectronics.com 2021, *How to Create a Pie Chart in Matplotlib with Python*, viewed on 21st Apr 2021, http://www.learningaboutelectronics.com/Articles/How-to-create-a-pie-chart-in-matplotlib-with-Python.php
- [36]  www.stockoverflow 2021, *Python matplotlib.pyplot pie charts...*, Stack Exchange (tmdavison), viewed on 21st Apr 2021, https://stackoverflow.com/questions/34094596/python-matplotlib-pyplot-pie-charts-how-to-remove-the-label-on-the-left-side
- [37]  www.simplypsychology.org 2021, *What does a box plot tell you?*, S.McLeod, viewed on 25th Apr, https://www.simplypsychology.org/boxplots.html
- [38]  www.seaborn.pydata.org 2021, *seaborn.boxplot*, M.Waskom, viewed on 25th Apr 2021, https://seaborn.pydata.org/generated/seaborn.boxplot.html
- [39]  www.stockoverflow 2021, *How do I get multiple subplots in matplotlib?*, Stack Exchange (K.A.Hooti), viewed on 19th Apr 2021, https://stackoverflow.com/questions/31726643/how-do-i-get-multiple-subplots-in-matplotlib
- [40]  www.cloudera.com 2021, *Correlation heatmaps*, Cloudera Inc., viewed on 25th Apr 2021, https://docs.cloudera.com/data-visualization/cloud/howto-visuals/topics/viz-visual-corr-heatmap.html
- [41]  www.seaborn.pydata.org 2021, *seaborn.heatmap*, M.Waskom, viewed on 25th Apr 2021, https://seaborn.pydata.org/generated/seaborn.heatmap.html
- [42]  www.stockoverflow 2021, *Rotate axis text in python matplotlib*, Stack Exchange (scottlittle), viewed on 25th Apr 2021,https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
- [43]  www.wikipedia.org 2021, *Histogram*, wikipedia, viewed on 21st Apr 2021, https://en.wikipedia.org/wiki/Histogram
- [44]  www.mathisfun.com 2021, *Histograms*, MathisFun, viewed on 21st Apr 2021, https://www.mathsisfun.com/data/histograms.html
- [45]  www.seaborn.pydata.org 2021, *seaborn.histplot*, M.Waskom, viewed on 21st Apr 2021, https://seaborn.pydata.org/generated/seaborn.histplot.html
- [46]  www.khanacademy.org 2021, *Scatterplots and correlation review*, Khan Academy, viewd on 21st Apr 2021, https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/introduction-to-scatterplots/a/scatterplots-and-correlation-review
- [47]  www.seaborn.pydata.org 2021, *seaborn.scatterplot*, M.Waskom, viewed on 21st Apr 2021, https://seaborn.pydata.org/generated/seaborn.scatterplot.html
- [48]  www.seaborn.pydata.org 2021, *seaborn.pairplot*, M.Waskom, viewed on 21st Apr 2021, https://seaborn.pydata.org/generated/seaborn.pairplot.html
- [49]  www.gist.github.com 2021, *Readme*, curran, viewed on 31st Mar 2021, https://gist.github.com/curran/a08a1080b88344b0c8a7
- Iris flowers image | https://miro.medium.com/max/1000/1*Hh53mOF4Xy4eORjLilKOwA.png


### **OTHERS ANALYSIS**

1. http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
2. https://www.maplesoft.com/support/help/maple/view.aspx?path=examples/IrisData
3. https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
4. https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
5. http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html
6. https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40
7. http://statweb.stanford.edu/~jtaylo/courses/stats202/visualization.html


### **README FORMATTING**

1. Basic writing and formatting syntax | https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
2. Display images side by side | https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md
3. Cener images | https://stackoverflow.com/questions/12090472/github-readme-md-center-image
4. Dropdown | https://gist.github.com/citrusui/07978f14b11adada364ff901e27c7f61
