#http://stamfordresearch.com/pca-in-python-with-scikit-learn/
import numpy as np
import pandas as pd
 
import matplotlib
import matplotlib.pyplot as plt
 
 
from sklearn.decomposition import PCA
from sklearn import datasets

# Pandas Options (optional)
pd_maxrows = 10
pd.set_option("display.max_rows",pd_maxrows)
 
pd.set_option("display.max_columns",30)

iris = datasets.load_iris()
X = iris.data
y = iris.target

print(iris.feature_names)
 
print(iris.target_names)



df = pd.DataFrame(X)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
 
# Add the class names
df['labels'] = iris.target_names[y]
 
print(df)

	
labels = df['labels'].unique().tolist()


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


X = df.iloc[:,0:4]

pca = PCA(n_components=2)
pca.fit(X)
X_ = pca.transform(X)

dfPCA = pd.DataFrame({'x1': X_[:,0], 'x2': X_[:,1]})
dfPCA['labels'] = df['labels']
dfPCA

plt.figure(figsize=(7,5))
for lab in labels:
    plt.scatter(dfPCA.loc[dfPCA['labels'] == lab, 'x1'],  dfPCA.loc[dfPCA['labels'] == lab, 'x2'], label=lab)
    plt.legend()

plt.show()

