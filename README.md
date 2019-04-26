# Programming and Scripting Project
## Project submission for Tom Healy 
## GMIT HDip in Science in Computing (Data Analysis)

## 1.1 Background of the dateset
R.A. Fisher's Iris Dataset AKA Anderson Dataset [Fisher Iris Data Set](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) was used in the his 1936 paper [The use of Multiple Measurements in Taxonomic Problems](http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf). The original paper can be found [here](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x).

The resulting analysis done by R.A. Fisher is performed on a dateset that was compiled by  Edgar Anderson in 1935. The iris were The data were taken from the [Gaspe Peninsula](https://goo.gl/maps/yFc3grbU6NN2). The dataset is sometimes called the Anderson data set.

The dataset contains 150 observations of iris flowers. 50 form each type of iris; _iris setosa_, _iris virginica_ and _iris versicolor_.

![alt text](https://cdn-images-1.medium.com/max/2100/1*2uGt_aWJoBjqF2qTzRc2JQ.jpeg "Iris Pic")

 Anderson took the measurement of 4 characterics of the flowers:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

Fisher was a very interesting character. He is seen as one of the founding fathers of statistics. His influence can be seen in areas such as linear discrimant analysis, analysis of variance(ANOVA), hypothesis testing and design of experiments.

The observations recorded on the island have become one of the most popular datasets used in machine learning and data science.

## 1.2 Approach to the project

In the carrying out of the project I used many resourses and tools. The list of references in contained below and also within the code files where applicable. The tools I used were:
<ul>
    <li>Visual Studio Code (IDE)</li>
    <li>Anaconda3 (Python3)</li>
    <li>GitHub (Source control and versioning)</li>
    <li>GMIT Data Analytics Course files</li>
    <li>Cmder - (Command Line Interface)</li>
</ul>

I had a look at the preveiling data science project models, the ones I found most relevant were:
<ul>
    <li>CRISP-DM</li>
    <li>DELTA framework by Tom Davenport</li>
    <li>KDD Framework </li>
</ul>
After researching the various models, I have decided to apply the CRISP-DM as far as is practicible.

The stages in the **CR**oss **I**ndustry **S**tandard **P**rocess for **D**ata **M**ining   are:

1. Business Understanding
    <p>-In this case, we have been asked to provide analysis on the Iris Data Set</p>
2. Data Understanding
    <p>-This stage involves initial data collection,understanding data quality problems and  some first insights in to the data.</p>
    <p>-What data do we have?</p>
    <p>-What are the summary details of the data</p>
    <p>-Exploratory Data Analysis</p>
3. Data Prep
    <p>-Preparation of the dataset to construct the final data set</p>
    <p>-Data Cleaning</p>
4. Modelling
    <p>-Select modelling techniques and apply</p>
    <p>-Prediction</p>
5. Evaluation
    <p>-How to evaluate the the model.</p>
    <p>-How accurate is the model?</p>

## 2. Business Understanding
As mentioned earlier, the overall "business problem" is to research, analyse and summarise the data. In industry, the business case of a project may be to understand or predict churn in our workforce. As the business problem here is pretty well defined we can move on to the next stage.

## 3. Data Understanding
At this stage we are gathering the data, doing some exploratory analysis:

First we loaded the package we will need and the data:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/way3.PNG">

I played around with opening the file using other means such as using the ```datasets``` module from the ```sklearn``` package and also using the ```np.genfromtxt(...)``` from the lectures.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/Load_data.PNG">
</p>


<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/open_file_%202.PNG">

Next we will take a look at the headline stats of the dataset:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/headline.PNG">

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

Next we will look some visualisations. The use of visualsations can detect patterns and anomolies in the data that would other wise not be readily apparent.

A Scatterplot is a good place to start. With a scatterplot , we can get good isea of the different data points. In the next plot, we can see the ratio of the size of the sepal length to the sepal width. We can see from the below that data points are very well segmented. The one setosa at co-ords (41, 1) looks like an outlier which could be interesting.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/Sepal_Length_Width_Ratio.png">

We can contrast this with the plot showing the ratio of Petal Length and Petal Width.

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/petal_length_petal_width.png">

Again the species seem very well segmented. 

We can use a scatter matrix to get an overall impression of the dataset:

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/scattermatrix.png">

We have can use more graphs and plots to understand the data better.

The 3dscatter plot can useful for understand data visually in 3 dimensions. When the code is ran in the terminal, you can rotate the plot and inspect it. 

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/3d.png">

The histogram is an excellent basic graph to understand the data.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/hist.png">

Here we have broken the data out in to 4 different histograms. We can see from the graphs that there are distinct spikes or groupings in the set when broken down by Sepal Length & Width and Petal Length & Width. This would suggest that the data is clustered around certain points and is not uniformly distributed.

The second last graph we will use is the boxwhisker plot. This is a useful plot for as it display a lot of data. It shows, moving top to bottom:

<ul>
    <li>Outliers        - Shown by the rings or circles</li>
    <li>Max             - Indictaed by the top horizontal line connected by a vertical line</li>
    <li>Upper Quartile  - Indicted by the top of the "box"</li>
    <li>Median          - Indicted by the line in the middle of the "box"</li>
    <li>Lower Quartile  - Indicted by the line at the bottom of the "box"</li>
    <li>Min             - Indicted by the bottom horizontal line connected by a vertical line</li>
    <li>Outliers        - Lowest valiue outliers</li>
</ul>


<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/box.png">

We can see that we have a few outlier in the Sepal Width box whisker plot. This would be interesting and would prompt question questions about characterics of those observations. Were they incorrectly identified? 

The final graph may shed some light:

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/scatterwithlegend.png">

Here we can see that our outliers at the top and bottom are both setosas. They are still well with their segments.

We now have good understanding of the data. We know it's shape, summary statistics, overall structure, the data integrity or quality and we can move on to the next stage of the process.

## 3. Data Prep

So we have checked the data for missing values and have mentioned how we would have corrected and filled in the missing values.

## 4. Modelling

Next we are going to use K-Means Clustering to predict the the classses for our Iris data set. This algorithm is using the mean values of the clusters to identify and segment the class within which the data point belongs. This is an unsupervised method as the inputs are being used to group rather than any intervention being given by us.

First we load the data and the packages:

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans1.PNG"

The next picture show the 3 lines of code to create the model. We are basically sayiinng here that the model is a kmeans model with 3 clusters or groups. 

The model then fits the centroids of the cluster around the mean of the groups. Based on that it assigns the data point a color.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans2.PNG"

Next we will see the classification of the dat from the set compared with what the clustering has produced.  

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans3.png"

We can see that there is a small error in the colors. We fix that and then re-plot.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/kmeans4.png"

So we now have our model but we need to check that it is accurate and precise. For this we will use two tools, the accuracy measure which compares the original values to the model values.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/Accuracy.PNG"

<p></p>
<p>We have an accuracy of nearly 90%, not too bad at all.</p>

Next we will use a confusion matrix to understand the number of correctly label model outputs and incorrectly labelled instances.

<p align="centre">
<img src="https://github.com/tomhealy1/project/blob/master/confusion.PNG"




|Predicted Class   |Real Class         |
| ---              |---                |
|                  |  0        1     2 | 
|                0 | 50       0      0 |
|                1 | 0       48     2  |
|                2 | 0       14     36 |



| Name     | Character |
| ---      | ---       |
|        0 | `         |
|        1 | \|        |
                    






## References
[CRISP-DM](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.198.5133&rep=rep1&type=pdf)
[Box Plot](https://flowingdata.com/2008/02/15/how-to-read-and-use-a-box-and-whisker-plot/)
