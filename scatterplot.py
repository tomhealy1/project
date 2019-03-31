#https://pythonspot.com/matplotlib-scatterplot/
#In the words of Machivelli, lets get plotting
import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt('iris.txt', delimiter=',', usecols=[0, 1, 2, 3])

a = [data[:,0]]
b = [data[:,1]]
c = [data[:,2]]
d = [data[:,3]]

df = (a, b, c, d)
colors = ("red", "green", "blue", "brown")
groups = ('sepal-length', 'sepal-width', 'petal-length', 'petal-width')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor='#E6E6E6')

for df, colors, groups in zip(df, colors, groups):
    x, y = a, b
    ax.scatter(x, y, alpha=0.8, c=colors, edgecolors='none', s=30, label=groups)

plt.title('Scatterplot of iris data')
plt.legend(loc=2)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor='#E6E6E6')

for df, colors, groups in zip(df, colors, groups):
    x, y = c, d
    ax.scatter(x, y, alpha=0.8, c=colors, edgecolors='none', s=30, label=groups)

plt.title('Scatterplot of iris data')
plt.legend(loc=2)
plt.show()

