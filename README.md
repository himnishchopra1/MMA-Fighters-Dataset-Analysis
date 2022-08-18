# MMA-Fighters-Dataset-Analysis
In this project I am researching how the different statistics of mma fighters are related to each other and how they impact the result of a mma match. The dataset contains the statistics over 1300 mma fighters collected by myself from https://www.ufc.com/athletes/all.

Process:

#### Data Collection
I went to the list of fighters to get the URL's to their fighter profiles, and from there visted each url to extract 23 features that would make the raw dataset
The framework used to scrape/collect the data was scrapy.  

#### Feature Engineering
The data was cleaned by:
removing improperly formatted data/incomplete data,
feature engineering the win rate, wins, losses, draws, striking accuracy, and takedown accuracy columns,
removing outliers and incrrectly entered data

The libraries used for this were:
Pandas
Numpy

#### Explaratory Data Anaylysis and Visualisation

Visaluised the data
