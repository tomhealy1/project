#Tom Healy
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#basic-plotting-plot
#Import packages as needed
#This was an early graph. I did not include as I found better graphs later in the project.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#Load the data as tetx separated by a "," and the columns we will be using are the 1st, 2nd, 3rd and 4th. Assign the data to the var "iris"
iris = np.loadtxt('iris.txt', delimiter=',', usecols=[0,1,2,3])

#We create a dataframe from the data used in the iris var.
df = pd.DataFrame(iris, columns=['a', 'b', 'c', 'd'])
ax = df.plot.scatter(x='a', y='b', s=50,color='DarkBlue', label='Sepal')
df.plot.scatter(x='c', y='d', s=50, color='Red', label='Petal', ax=ax)

plt.show()

exit

