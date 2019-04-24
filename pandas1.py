#Using Pandas to do some description
#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
import pandas as pd 
import numpy as np


headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
data = pd.read_csv('iris.txt', sep=',', names=headings, header=None)
print("Here is a read out of all your data: \n", data)

print()

r = data

print(r.describe())


x = pd.Series(data)
print("Here are the headline details of column 1: \n", x.describe(include=[0]))
print("Here are the headline details of column 2: \n", x.describe(include=[1]))
print("Here are the headline details of column 3: \n", x.describe(include=[2]))
print("Here are the headline details of column 4: \n", x.describe(include=[3]))

print("Here are the headline details of all the numeric columns: \n", x.describe())

print("Here what the first 20 items look like: ", data.head(20))

#Check if the there are missing values


data['Sepal Length'].isnull()


data['Sepal Width'].isnull()


data['Petal Length'].isnull()


data['Petal Width'].isnull()


data['Species'].isnull()

print ("Here is the number of missing values in the set:\n",data.isnull().sum())




