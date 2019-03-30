#HDip in Computer Science (Data Analysis)
#Tom Healy
#Import packages needed
import pandas as pd
import numpy as np
#Assign txt file to df

df = np.genfromtxt('iris.txt', delimiter=',')

#We are going to show the mean of each column and print to screen
meansl=np.mean(df[:,0]).round(3)
print('The mean sepal length is',meansl)

meansw=np.mean(df[:,1]).round(3)
print('The mean sepal width is',meansw)

meanpl=np.mean(df[:,2]).round(3)
print('The mean petal length is',meanpl)

meanpw=np.mean(df[:,3]).round(3)
print('The mean petal length is',meanpw)


