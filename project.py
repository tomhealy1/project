#HDip in Computer Science (Data Analysis)
#Tom Healy
#Import packages needed
import pandas as pd
import numpy as np
#Assign csv file to df
df = pd.read_csv("iris_csv.csv")
#Print the columns names
print(df.columns)

#print the descriptive stats
y = df.describe()

print(y)

