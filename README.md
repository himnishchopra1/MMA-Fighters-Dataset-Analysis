# MMA-Fighters-Dataset-Analysis

URL for application: https://himnishchopra1-mma-fighters-dataset-analysis-main-xfygfm.streamlitapp.com/

In this project I am researching how the different statistics of mma fighters are related to each other and how they impact the result of a mma match. The dataset contains the statistics over 1300 mma fighters collected by myself from https://www.ufc.com/athletes/all. The cleaned data file is called mma_data.csv and anyne is free to explore the data themselves.

Process:

#### Data Collection
I went to the list of fighters to get the URL's to their fighter profiles, and from there visted each url to extract 23 features that would make the raw dataset

Framework Used to scrape/collect the data 
- Python Scrapy 

#### Feature Engineering
The data was cleaned by:
removing improperly formatted data/incomplete data,
feature engineering the win rate, wins, losses, draws, striking accuracy, and takedown accuracy columns,
removing outliers and incrrectly entered data

The libraries used for this were:
- Pandas
- Numpy

#### Explaratory Data Anaylysis and Visualisation

After I clean the data I made a heatmap of the all the numeric features of the data and made several histograms to see how different features were correlated with eachother and to see how the values of each feature were distributed.

The libraries used were:
- Seaborn
- Matplotlib

#### Creating the web application
After I performed exploratory data analysis I used Streamlit which is framework that can be used to make web applications for data science. There I provide a summary of my biggest insights that relate to the outcome of mma matches as well as an oppurtunity for the user to explore the findings in greater detail.
