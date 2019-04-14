#Tom Healy 
#Taken from http://stamfordresearch.com/k-means-clustering-in-python/

#Import the packages you will need:Matplotlib for plotting, scikitlearn to load the datas
import matplotlib.pyplot as plt 
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm

import pandas as pd
import numpy as np 

#the loaded datsets will become the variable iris
iris = datasets.load_iris()
#Using Pandas we make a dataframe from the iris data and name the columns
x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']


y = pd.DataFrame(iris.target)
y.columns = ['Targets']

#Give the size of the plot you want, added greater dpi for the dots for better visibility
plt.figure(figsize=(8, 18),dpi=200)
#Add color map to for colors of the dots
colormap = np.array(['red', 'blue', 'green'])
#Plot the Sepal plot
plt.subplot(1, 2, 1)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[y.Targets], s=40)
plt.title('Sepal')
#Plot the Petal plot
plt.subplot(1,2,2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Petal')

#Commented out the first plot
#plt.show()

#Create the KMean and tell it to fit x
model =KMeans(n_clusters=3)
model.fit(x)
#Let's see what the model thought
model.labels_

#Next we plot the actual labels/classes the model came up with against the actual data
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'blue', 'green'])
 
# Plot the Original Classifications
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Classification from labels')
 
# Plot the Models Classifications
plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('K Mean Classification')


plt.show()

#So according to the tutorial the classifier has mislabeled the data. 


# The fix, we convert all the 1s to 0s and 0s to 1s to align to the way to the way we want.
predY = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)
print (model.labels_)
print (predY)

# View the results
# Set the size of the plot
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'blue', 'green'])
 
# Plot Orginal
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Classification')
 
# Plot Predicted with corrected values
plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predY], s=40)
plt.title('K Mean Classification')

plt.show()

#The above graph shows the correct red with only a few of the blues and greens being mixed

#Next we need to check how accurate the model is 

z = sm.accuracy_score(y, predY)

print(z)

# Confusion Matrix
t = sm.confusion_matrix(y, predY)
print(t)

