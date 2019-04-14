import pandas as pd 
from pandas.plotting import radviz
import matplotlib.pyplot as plt

data = pd.read_csv('iris1.txt')

#print(data)

radviz(data, 'Name')

plt.show()


