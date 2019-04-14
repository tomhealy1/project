#Adapted from Chris Albon https://chrisalbon.com/machine_learning/linear_regression/linear_regression_using_scikit-learn/
#Load the libraries we will need
#This is just to play round with Linear regression more that anything else
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
import warnings
import numpy as np 
import pandas as pd 

#HE recommends to suppress the warnings 
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

#Load the data and assign the X and y to the data and target respectively 
iris = load_iris()
X = iris.data
y = iris.target



#Create a linear regression
regr = LinearRegression()
#Fit the model
model = regr.fit(X, y)
#View the intercept 
model.intercept_
#Print the intercept, so this where the data hits the y axis (I wish I paid more attention in Algebra......)
print(model.intercept_)

#View the coefficients
model.coef_

print(model.coef_)





