#Using Pandas to do some explortory analysis
#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
import pandas as pd 
import numpy as np


headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
data1 = pd.read_csv('iris.txt', sep=',', names=headings, header=None)
print("Here is a read out of all your data: \n", data1)

#print()

#r = data1 Commenting out as not needed

#print("Here ", r.describe()) No longer needed

#data2 = data1[['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']] I comment this out as I did not need it

x = pd.DataFrame(data1)

index = x.index
columns1=x.columns
print("Here is some info about the rows",index)
print(columns1)
print("Here is the shape of your data", x.shape, "rows and columns respectively.")


print("Here are the headline details of all the numeric columns: \n" ,x.describe())

print("Here what the first 20 items look like: \n", data1.head(20))

#Check if the there are missing values and sum the totals in the last command


data1['Sepal Length'].isnull()


data1['Sepal Width'].isnull()


data1['Petal Length'].isnull()


data1['Petal Width'].isnull()


data1['Species'].isnull()


print ("Here is the number of missing values in the set:\n",data1.isnull().sum())




