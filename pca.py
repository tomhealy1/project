#Tom Healy
#http://stamfordresearch.com/pca-in-python-with-scikit-learn/
#Import pandas, numpy and matplotlib
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#Import the sklearn package 
from sklearn.decomposition import PCA
from sklearn import datasets

#Tell pandas to not display too much
pd_maxrows = 10
pd.set_option("display.max_rows",pd_maxrows)
pd.set_option("display.max_columns",30)

#Assign the oloaded dataset to the variable iris. X = inputs and y = outputs
iris = datasets.load_iris()
X = iris.data
y = iris.target


print("Here are the inputs", iris.feature_names)
 
print("Here are the outputs", iris.target_names)



df = pd.DataFrame(X)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
 
#Add the class names or output names
df['labels'] = iris.target_names[y]
 
print(df)

	
labels = df['labels'].unique().tolist()

#Here we are plotting the Sepal measure(LHS Chart) and Petal (RHS Chart)
plt.figure(figsize=(15,5))
plt.subplot(121)
for lab in labels:
    plt.scatter(df.loc[df['labels'] == lab, 'sepal_length'],  df.loc[df['labels'] == lab, 'sepal_width'], label=lab)
    plt.legend()
    
plt.subplot(122)
for lab in labels:
    plt.scatter(df.loc[df['labels'] == lab, 'petal_length'],  df.loc[df['labels'] == lab, 'petal_width'], label=lab)
    plt.legend()

plt.show()

#This is the PCA part of the script
#Creates an array
X = df.iloc[:,0:4]

#Fit the PCA
pca = PCA(n_components=2)
pca.fit(X)
X_ = pca.transform(X)

#Create a dataframe called dfPCA
dfPCA = pd.DataFrame({'x1': X_[:,0], 'x2': X_[:,1]})
dfPCA['labels'] = df['labels']
dfPCA
print(dfPCA)

#We then plot the PCA
plt.figure(figsize=(7,5))
for lab in labels:
    plt.scatter(dfPCA.loc[dfPCA['labels'] == lab, 'x1'],  dfPCA.loc[dfPCA['labels'] == lab, 'x2'], label=lab)
    plt.legend()

plt.show()

