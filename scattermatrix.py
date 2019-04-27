#Tom Healy
#https://stackoverflow.com/questions/46383645/seaborn-and-pd-scatter-matrix-plot-color-issues

#import pandas
#from pandas.plotting import scatter_matrix
#import matplotlib.pyplot as plt

# Assign the file to var iris, assign names to the cols and pass the panda read file to df
#iris = "iris.txt"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#df = pandas.read_csv(iris, names=names)

#Call on the scatter_matrix mod in pandas to create a simple scatter matrix 
#scatter_matrix(df, figsize=None,color=colors,diagonal='hist')
#plt.show()

#Commenting out the above as the code is shorter and it adds color aligned with the species/names

#Verbatim https://stackoverflow.com/questions/46383645/seaborn-and-pd-scatter-matrix-plot-color-issues
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")

plt.show()
