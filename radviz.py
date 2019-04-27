#Tom Healy
#This graph works on the idea that each point is "connected to a spring from the centre" . Shows the level of correlation also. Pretty cool graph.
import pandas as pd 
from pandas.plotting import radviz
import matplotlib.pyplot as plt

data = pd.read_csv('iris1.txt')

#print(data)

radviz(data, 'Name')

plt.show()


