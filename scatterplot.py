#https://pythonspot.com/matplotlib-scatterplot/
#In the words of Machivelli, lets get plotting
#import numpy as np 
#import matplotlib.pyplot as plt
#
#data = np.loadtxt('iris.txt', delimiter=',', usecols=[0, 1, 2, 3])
#
#a = [data[:,0]]
#b = [data[:,1]]
#c = [data[:,2]]
#d = [data[:,3]]
#
#df = (a, b, c, d)
#colors = ("red", "green", "blue")
#groups = ('setosa', 'versicolor', 'virginica')
#
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1, facecolor='#E7E7E7')
#
#for df, colors, groups in zip(df, colors, groups):
#    x, y = a, b
#    ax.scatter(x, y, alpha=0.8, c=colors, edgecolors='none', s=30, label=groups)
#plt.title('Scatterplot of iris data')
#plt.legend(loc=2)
#plt.show()

# I could not get the above code to work so I looked for a simpler way to do it and I found this:

#https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
iris["ID"] = iris.index
iris["ratio"] = iris["sepal_length"]/iris["sepal_width"] # Sepal Length and Width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()


iris["ratio"] = iris["petal_length"]/iris["petal_width"] # Petal Length and Width

sns.lmplot(x="ID", y="ratio", data=iris, hue="species", fit_reg=False, legend=False)

plt.legend()
plt.show()

