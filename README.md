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

<p align="left">
<img src="https://github.com/tomhealy1/project/blob/master/hist.png">

## References
[CRISP-DM](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.198.5133&rep=rep1&type=pdf)

