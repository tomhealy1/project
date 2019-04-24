# Tom Healy 
#https://stackoverflow.com/questions/43484757/creating-a-3d-scatter-plot-from-a-csv-file
#https://matplotlib.org/gallery/mplot3d/2dcollections3d.html

import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
#I am trying add color to each different column but cant find a way yet
a, b, c, d = np.loadtxt('iris.txt', delimiter=',',dtype=float, unpack=True, usecols=[0,1 ,2, 3])


ax1.scatter(a, b,c, d, c='blue', marker='o')
plt.show()