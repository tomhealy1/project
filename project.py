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
print('The mean petal width is',meanpw)
print(' ')
#We are going to show the max of each column and print to screen
maxsl=np.max(df[:,0]).round(3)
print('The max sepal length is',maxsl)
maxsw=np.max(df[:,1]).round(3)
print('The max sepal width is',maxsw)
maxpl=np.max(df[:,2]).round(3)
print('The max petal length is',maxpl)
maxpw=np.max(df[:,3]).round(3)
print('The max petal width is',maxpw)
print(' ')

#We are going to show the min of each column and print to screen

minsl=np.min(df[:,0]).round(3)
print('The min sepal length is',minsl)
minsw=np.min(df[:,1]).round(3)
print('The min sepal width is',minsw)
minpl=np.min(df[:,2]).round(3)
print('The min petal length is',minpl)
minpw=np.min(df[:,3]).round(3)
print('The min petal width is',minpw)
print(' ')
