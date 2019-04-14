#Verbatim- https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html  I chaged a few things order of import, color etc
# Load the data
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

#Assign data to the iris var
iris = load_iris()

# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

#Plot the figure
plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()