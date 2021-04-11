# MODULE: Programming and scripting
# PROJECT: Program that analyses the Iris Data set
# Author: Ante Dujic

import pandas as pd

data = pd.read_csv('irisData.csv')

def dataLayout():
    print ("This data set consists of {} samples, grouped by {} different variables:".format ((data.shape[0]), (data.shape[1])))
    
    for col in data.columns:
        print (col)

    print ("The general layout of the data: \n{}\n*First 10 rows \n{}\n*Random 10 rows" .format ((data.head(10)), data.sample(10)))

dataLayout()