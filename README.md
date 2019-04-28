# Programming and Scripting Project - 2019
## Project submission for Tom Healy G00376351
## GMIT HDip in Science in Computing (Data Analysis)

## <h3>1.1 Background of the dateset</h3>
R.A. Fisher's Iris Dataset AKA Anderson Dataset [Fisher Iris Data Set](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) was used in the his 1936 paper [The use of Multiple Measurements in Taxonomic Problems](http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf). The original paper can be found [here](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x).

The resulting analysis done by R.A. Fisher is performed on a dateset that was compiled by Edgar Anderson in 1935. The data were taken from the [Gaspe Peninsula](https://goo.gl/maps/yFc3grbU6NN2). The dataset is sometimes called the Anderson data set.

The dataset contains 150 observations of iris flowers. 50 from each type of iris; _iris setosa_, _iris virginica_ and _iris versicolor_.

![alt text](https://cdn-images-1.medium.com/max/2100/1*2uGt_aWJoBjqF2qTzRc2JQ.jpeg "Iris Pic")

 Anderson took the measurement of 4 characteristics of the flowers:

<h4>1. Sepal Length</h4>
<h4>2. Sepal Width</h4>
<h4>3. Petal Length</h4>
<h4>4. Petal Width</h4>

Fisher was a very interesting character. He is seen as one of the founding fathers of statistics. His influence can be seen in areas such as linear discriminant analysis, analysis of variance(ANOVA), hypothesis testing and design of experiments.

The observations recorded on the island have become one of the most popular datasets used in machine learning and data science.

## <h3>1.2 Approach to the project</h3>

In carrying out the project, I used many resourses and tools. The list of references is contained below and also within the code files where applicable. The tools I used were:
<ul>
    <li>Visual Studio Code (IDE)</li>
    <li>Anaconda3 (Python3)</li>
    <li>GitHub (Source control and versioning)</li>
    <li>GMIT Data Analytics Course files</li>
    <li>Cmder - (Command Line Interface)</li>
    <li>Jupyter Notebook - I chose to use VSC as I was more familiar. I plan to use iPython and Jupyter over the Summer to build knowledge.
</ul>

I wanted to follow a plan and make the project as "real world" as possible so I had a look at the preveiling data science project models, the ones I found most relevant were:
<ul>
    <li>CRISP-DM</li>
    <li>DELTA framework by Tom Davenport</li>
    <li>KDD Framework </li>
</ul>
After researching the various models, I have decided to apply the CRISP-DM as far as is practicible.

<p> </p>

The stages in the **CR**oss **I**ndustry **S**tandard **P**rocess for **D**ata **M**ining are:

1. <strong>Business Understanding</strong>
    <p>-In this case, we have been asked to provide analysis on the Iris Data Set</p>
2. <strong>Data Understanding</strong>
    <p>-This stage involves initial data collection, understanding data quality problems and some first insights in to the data.</p>
    <p>-What data do we have?</p>
    <p>-What are the summary details of the data</p>
    <p>-Exploratory Data Analysis</p>
3. <strong>Data Prep</strong>
    <p>-Preparation of the dataset to construct the final data set</p>
    <p>-Data Cleaning</p>
4. <strong>Modelling</strong>
    <p>-Select modelling techniques and apply</p>
    <p>-Prediction</p>
5. <strong>Evaluation</strong>
    <p>-How to evaluate the the model.</p>
    <p>-How accurate is the model?</p>

## <h3>2. Business Understanding</h3>
As mentioned earlier, the overall "business problem" is to research, analyse and summarise the data. In industry, this could be any data related task such as understand or predict churn in our workforce or customers. As the business problem here is pretty well defined we can move on to the next stage.

## <h3>3. Data Understanding</h3>
At this stage we are gathering the data, doing some exploratory analysis:

First we loaded the package we will need and the data:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/way3.PNG">
</p>

I played around with opening the file using other means such as using the ```datasets``` module from the ```sklearn``` package and also using the ```np.genfromtxt(...)``` command from the lectures.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/Load_data.PNG">
</p>


<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/open_file_%202.PNG">
</p>
Next we will take a look at the headline stats of the dataset:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/headline.PNG">
</p>

Here we can see the headline details of the set. We can see the set contains 150 row and 5 columns.
We can also see the:
     <p>1. counts   - Counts each observation in each column</p>
     <p>2. mean     - The mean or avg of the values in each column</p>
     <p>3. std      - Shows the standard deviation of the vaules in the column</p>
     <p>4. min      - The minimum values in the each column</p>
     <p>5. 25%      - Shows the IQR at 25%</p>
     <p>6. 50%      - Shows the IQR at 50%</p>
     <p>7. 75%      - Shows the IQR at 75%</p>
     <p>8. max      - Shows the max values in each column</p>

And some more info:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/mean_max_mean.PNG">

We also must check for missing values:
<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/missing_values.PNG">

Here we can see that there are no missing values in the dataset. If we did have missing values we would have to filter out the missing values using the ```numpy``` module ```nan``` . Alternatively, we could have filled in the missing data with a command like ```data1.fillna(0)```

We can take a look and the raw values also, below are the first 20 values:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/top20.PNG">

Next we will look some visualisations. The use of visualsations can detect patterns and anomalies in the data that would otherwise not be readily apparent.

A Scatterplot is a good place to start. With a scatterplot, we can get good idea of the different data points. In the next plot, we can see the ratio of the size of the sepal length to the sepal width. We can see from the below graph that data points are very well segmented. The one setosa at co-ords (41, 1) looks like an outlier which could be interesting.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/Sepal_Length_Width_Ratio.png">

We can contrast this with the plot showing the ratio of Petal Length and Petal Width.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/petal_length_petal_width.png">

Again the species seem very well segmented. 

We can use a scatter matrix to get an overall impression of the dataset, We can see that the sepal width is quite normally distrubuted along the species with not a lot of difference in the measurements. We can compare this with the petal width where the observations are more segmented. We can also see that the distribution of the petal width of the setosa is not that distributed widely and so the standard deviation (how spread out the data is) would be small.


<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/scattermatrix.png">

We have can use more graphs and plots to understand the data better.

The 3dscatter plot can useful for understand data visually in 3 dimensions. When the code is ran in the terminal, you can rotate the plot and inspect it. 

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/3d.png">

The histogram is an excellent basic graph to understand the data.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/hist.png">

Here we have broken the data out in to 4 different histograms. We can see from the graphs that there are distinct spikes or groupings in the set when broken down by Sepal Length & Width and Petal Length & Width. This would suggest that the data is clustered around certain points and is not uniformly distributed however this is most likely caused by the different species.

The second last graph we will use is the boxwhisker plot. This is a useful plot for as it display a lot of data. It shows, moving top to bottom:

<ul>
    <li>Outliers        - Shown by the rings or circles</li>
    <li>Max             - Indicated by the top horizontal line connected by a vertical line</li>
    <li>Upper Quartile  - Indicated by the top of the "box"</li>
    <li>Median          - Indicated by the line in the middle of the "box"</li>
    <li>Lower Quartile  - Indicated by the line at the bottom of the "box"</li>
    <li>Min             - Indicated by the bottom horizontal line connected by a vertical line</li>
    <li>Outliers        - Lowest value outliers</li>
</ul>


<p align="centre">
<img width="800" height="600" src="https://github.com/tomhealy1/project/blob/master/box.png">
</p>

We can see that we have a few outliers in the Sepal Width box whisker plot. This would be interesting and would prompt questions about the characterics of those observations. Were they incorrectly identified? 

The final graph may shed some light:

<p align="centre">
<img width="800" height="700" src="https://github.com/tomhealy1/project/blob/master/scatterwithlegend.png">
</p>

Here we can see that our outliers at the top and bottom are both setosas. They are still well with their segments.

We now have good understanding of the data. We know it's shape, summary statistics, overall structure, the data integrity or quality and we can move on to the next stage of the process.

## 3. Data Prep

So we have checked the data for missing values and have mentioned how we would have corrected and filled in the missing values.

## 4. Modelling

Next we are going to use K-Means Clustering to predict the the classses for our Iris data set. This algorithm is using the mean values of the clusters to identify and segment the class within which the data point belongs. This is an unsupervised method as the inputs are being used to group rather than any intervention being given by us.

First we load the data and the packages:

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans1.PNG">
</p>

The next picture shows the 3 lines of code needed to create the model. We are basically saying here that the model is a kmeans model with 3 clusters or groups. 

The model then fits the centroids of the cluster around the mean of the groups. Based on that it assigns the data point a color within those groups.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans2.PNG">
</p>

Next we will see the classification of the data from the set compared with what the clustering has produced.  

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans3.png">
</p>

We can see that there is a small error in the colors. We fix that and then re-plot.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans4.png">
</p>

So we now have our model but we need to check that it is accurate and precise. For this we will use two tools, the accuracy measure which compares the original values to the model values.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/Accuracy.PNG">
</p>

<p></p>
<p>We have an accuracy of nearly 90%, not too bad at all.</p>

<p>It is worth noting that another model may have yielded better results or we could have tuned this model to increase accuracy.

Next we will use a confusion matrix to understand the number of correctly label model outputs and incorrectly labelled instances.

<p align="center">
<img src="https://github.com/tomhealy1/project/blob/master/confusion.PNG">
</p>






<p> </p>

Confusion Matrix

| Predicted Class     | Real Class         |
| ----                 | ----                |
|                     | 0    -   1  -    2| 
|                       |----------         |
|                   0 | 50   -    0   -   0  |
|                   1 | 0    -   48    -  2  |
|                   2 | 0    -   14    -  36 |
                    

The table above shows that the model:
<ul>
    <li>correctly identified all 0 classes as 0 s.</li>
    <li>correctly identified 48 class 1s but incorrectly classified two instances of class 1s as class 2s</li>
    <li>correctly identifed 36 class 2s but incorrectly classified 14 instances of class 2s as class 1s.</li>
</ul>

I have included the code to perform Principal Componant Analysis also.

I also added a linear regression model also. Here is the output showing the y intercept and the coeffiecients.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/linear.png"



## <h3>5. Evaluation</h3>

In the final stage, we would look at the model's performance. The accuracy figure of 89.3% is quite good but another model may have yielded better results. 

We have used Python to understand the details, shape and characteristics of the dataset. We have seen that data points are well segmented regarding their species which makes the dataset a strong candidate for simple machine learning models. We gathered the headline details such as the min, average, max, standard deviation (how spreadout the data is) and the inter quartile range. We then checked the data for any missing values and provided means of fixing them. 

Next we visualised the data using scatterplots, scatter matrices, 3D Scatter plots and histograms. Visualisation of the data can give a greater understanding of the data that summary statistics alone.

We also applied an unsupervised model to the data called KMeans. KMeans uses the average of the clusters (in our case 3) to group the data.

We also provided some information regarding other models, namely, PCA and linear regression.

,<em>P.S. I incorporated the feedback for the earlier assisgnment in this projects such as:</em>
    <h4>1. Evidence of learning new knowledge</h4>
    <h4>2. Commented out "dead end" or code/approaches that did not work instead of deleting to show other options evaluated</h4>
    <h4>3. Developed a plan, I chose CRISP-DM and I started to use HIPO paper charts and white board (€19.99 Aldi a few months ago :-) ) at the end</h4>
    <h4>4. I had a lot of the project done early (plot, stats and models) but I commit and push on nearly every edit which inflates my commit/push count</h4>
    <h4>5. I tried to comment in simple to understand terms and reword other comment in an approachable way</h4>
    <h4>6. I used the Data Science and Big Data Analytics book to map the outline and provide a design, the CRISP-DM model was very helpful also.

## References
[CRISP-DM](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.198.5133&rep=rep1&type=pdf)


[Box Plot](https://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot/)

Data Science and Big Data Analytics - Discovering, Analysing, Visualising and Presenting Data

Python for Data Analysis - Data Wrangling with Pandas, Numpy and Ipython , Wes McKinney

Statistics and Machine Learning in Python -Release 0.2 -Edouard Duchesnay - Mar 14, 2019

Python Data Science Handbook by Jake VanderPlas

Mastering Machine Learning with Python in Six Steps A Practical Implementation Guide to Predictive Data Analytics Using Python —Manohar Swamynathan

Hands-On Machine Learning with Scikit-Learn & TensorFlow - CONCEPTS, TOOLS, AND TECHNIQUES TO BUILD INTELLIGENT SYSTEMS

Introduction to Machine Learning with Python A GUIDE FOR DATA SCIENTISTS Andreas C. Müller & Sarah Guido

Python Cookbook 3rd Edition - by David Beazley and Brian K. Jones

An Introduction to Statistical Learning - with application in R ( I used this to understand intercepts and coefficients ) -Gareth James • Daniela Witten • Trevor Hastie
Robert Tibshirani



