#Tom Healy
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#basic-plotting-plot
#This was an early graph. I did not include as I found better graphs later in the project.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('iris.txt', delimiter=',', usecols=[0,1,2,3])

#Create a scatter plot of the green sepal measurements and red petal measurements
df = pd.DataFrame(iris, columns=['a', 'b', 'c', 'd'])
ax = df.plot.scatter(x='a', y='b', s=50,color='Green', label='Sepal')
df.plot.scatter(x='c', y='d', s=50, color='Red', label='Petal', ax=ax)

plt.show()

exit
