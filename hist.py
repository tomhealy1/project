#Import our 
import pandas
from pandas.plotting import boxplot
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

#Referenece https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Assign file to the var iris, add names for columns and assign those to the var df
iris = "iris.txt"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pandas.read_csv(iris, names=names)

#Create the histogram and show the graph based on the dataframe df
df.hist()
plt.show()






