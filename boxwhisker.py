import pandas
from pandas.plotting import boxplot
import matplotlib.pyplot as plt

#https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

# Assign file var iris, add names for columns and assign those to the var df
iris = "iris.txt"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pandas.read_csv(iris, names=names)

# Command to plot and show the boxwhisker plot
df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

