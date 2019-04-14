#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#basic-plotting-plot
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('iris.txt', delimiter=',', usecols=[0,1,2,3])


df = pd.DataFrame(iris, columns=['a', 'b', 'c', 'd'])
ax = df.plot.scatter(x='a', y='b', s=50,color='Green', label='Sepal')
df.plot.scatter(x='c', y='d', s=50, color='Red', label='Petal', ax=ax)

plt.show()

exit
