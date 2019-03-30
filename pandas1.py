#Using Pandas to do some description
import pandas as pd 

headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
data = pd.read_csv('iris.txt', sep=',', names=headings, header=None)
print(data)

print(data.shape)

x = pd.Series([0,1,2,])
print(x.describe())



