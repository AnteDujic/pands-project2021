# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

def dataLayout():
    x = ("This data set consists of {} samples, grouped by {} different variables:\n".format ((data.shape[0]), (data.shape[1])))
    
    x += "\n".join (data.columns)

    x += ("\n\nThe general layout of the data: \n\n{}\n*First 10 rows \n\n{}\n*Random 10 rows" .format ((data.head(10)), data.sample(10)))
    return x

with open ("layout.txt", "wt") as f:
    f.write (str (dataLayout()))