#Tom Healy
#Verbatim - https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset 

#This is also a good graph to remember, simple and a good way to compare the ratios of observations
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
iris["ID"] = iris.index
iris["ratio"] = iris["sepal_length"]/iris["sepal_width"]

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()

iris["ratio"] = iris["petal_length"]/iris["petal_width"]

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()