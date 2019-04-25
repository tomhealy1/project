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
As mentioned earlier, the overall "business problem" is to research, analyse and summarise the data. In industry, the business case of a project may be to understand or predict churn in our workforce. As the business problem here is pretty well defined wecan move on to the next stage.

##3. Data Understanding
At this stage we are gathering the data, doing some exploratory analysis:

First we loaded the data:
<p align="left">
<img src="https://github.com/tomhealy/project/Load_data.PNG">
</p>



## References
[CRISP-DM](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.198.5133&rep=rep1&type=pdf)

