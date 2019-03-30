import pandas
from pandas.plotting import boxplot
import matplotlib.pyplot as plt

# Assign file var iris, add names for columns and assign those to the var df
iris = "iris.txt"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pandas.read_csv(iris, names=names)

# 
df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()