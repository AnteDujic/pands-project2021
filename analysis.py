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
species = data.groupby ("species").size()
with open ("layout.txt", "wt") as f:
    f.write (str (layout) + "\n\n")
    f.write (str (species))
 
"""
speciesColumn = (data.describe(include = ["object"]))
print (speciesColumn.loc [["count", "unique", "freq"]])

speciesName = data.groupby ("species").describe().transpose()
print (speciesName)
"""