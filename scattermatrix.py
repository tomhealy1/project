import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Assign the file to var iris, assign names to the cols and pass the panda read file to df
iris = "iris.txt"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pandas.read_csv(iris, names=names)

#Call on the scatter_matrix mod in pandas to create a simple scatter matrix 
scatter_matrix(df, figsize=None,diagonal='hist')
plt.show()

