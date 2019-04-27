# Tom Healy 
#https://stackoverflow.com/questions/43484757/creating-a-3d-scatter-plot-from-a-csv-file
#https://matplotlib.org/gallery/mplot3d/2dcollections3d.html
#Import the packages as needed 
import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

#We plot the figure using the 3D package, add the projection, color and the data. 
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
a, b, c, d = np.loadtxt('iris.txt', delimiter=',',dtype=float, unpack=True, usecols=[0,1 ,2, 3])

#Create the 2d scatter based on the columns using the 'o' as a marker for each data point 
ax1.scatter(a, b,c, d, c='blue', marker='o')
plt.show()

#The next step here would have been to add colors to the 3d pic but I suppose this is adequate to give an overall impression of the data on a 3d scale.