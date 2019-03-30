#Using Pandas to do some description
import pandas as pd 
import numpy as np


headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
data = pd.read_csv('iris.txt', sep=',', names=headings, header=None)
print("Here is a read out of all your data: ", data)

x = pd.Series([0,1,2,])
print("Here are the headline details of the set: ", x.describe())

print("Here what the first 20 items look like: ", data.head(20))
