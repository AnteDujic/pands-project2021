# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

def dataLayout():
    l = ("\nDATASET LAYOUT\n")
    l += ("\nThis data set consists of {} samples, grouped by {} different variables:\n".format ((data.shape[0]), (data.shape[1])))
    l += "\n".join (data.columns)
    l += ("\n\nThe general layout of the data: \n\n{}\n*First 10 rows \n\n{}\n*Random 10 rows" .format ((data.head(10)), data.sample(10)))
    return l

layout = dataLayout()
with open ("layout.txt", "wt") as f:
    f.write (str (layout))

speciesNames = data.groupby ("species").size().to_string()
speciesDetail = (data.describe(include = ["object"])).loc [["count", "unique", "freq"]]
dataSummary = data.describe ()
dataCorrelation = data.corr()

with open ("analysis.txt", "wt") as f:
    f.write ("Species Info:\n" + str (speciesDetail) + "\n\n")
    f.write ("Species of Iris:\n" + str (speciesNames) + "\n\n")
    f.write ("Data Summary:\n" + str (dataSummary) + "\n\n")
    f.write ("Data correlation:\n" + str (dataCorrelation))


"""


speciesName = data.groupby ("species").describe().transpose()
print (speciesName)
"""