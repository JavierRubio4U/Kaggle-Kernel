# -*- coding: utf-8 -*-
'''
Created on Sun Mar 25 18:24:03 2018

@author: Javier Rubio
'''

#Libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#Load file
df = pd.read_csv('G:/Python/Kaggle/VideogameSales/Video_Games_Sales_as_at_22_Dec_2016.csv')

#NUMERIC ANALYSIS
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

#Check Index
df.index
#Slicing
df.iloc[10000:10005,:]
## Name, Platform, Genre, NA EU JP Sales are complete 

## Calculate number or range of parameters
print('Platforms (Unique):')
platforms = pd.unique(df.Platform)
print(platforms)
print('\nYears (Range): ' + str(min(df.Year_of_Release)) + ' - ' + str(max(df.Year_of_Release)))
df.plot(y='Year_of_Release', kind='box')
print('\nGenres (Unique):')
genres = pd.unique(df.Genre)
print(genres)
print('\nNA_Sales (Range): ' + str(min(df.NA_Sales)) + ' - ' + str(max(df.NA_Sales)))
print('EU_Sales (Range): ' + str(min(df.EU_Sales)) + ' - ' + str(max(df.EU_Sales)))
print('JP_Sales (Range): ' + str(min(df.JP_Sales)) + ' - ' + str(max(df.JP_Sales)))
print('Other Sales (Range): ' + str(min(df.Other_Sales)) + ' - ' + str(max(df.Other_Sales)))
print('Global Sales (Range): ' + str(min(df.Global_Sales)) + ' - ' + str(max(df.Global_Sales)))
print('\nCritic Score (Range): ' + str(min(df.Critic_Score)) + ' - ' + str(max(df.Critic_Score)))


## Sales analysis
df['Total_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales']+df['Other_Sales']+df['Global_Sales']
sns.jointplot(x=df['Year_of_Release'], y=df['Total_Sales'],kind='scatter',xlim=(1980,2016))
plt.show()


### Top 10 ps4
PS4=df[df.Platform == 'PS4']
sns.countplot(x="Year_of_Release", data=PS4)
plt.show()

### Top 10 ps4 titles by Critic Score
PS4=PS4[['Name','Year_of_Release','Critic_Score','User_Score','Total_Sales']].sort_values('Critic_Score',ascending=False)
PS4=PS4.iloc[:9,]
print(PS4)
sns.barplot(x="Name", y="Total_Sales", hue="Critic_Score", data=PS4)
plt.xticks(rotation=80,fontsize = 10)
plt.show()


### Top 10 XOne by Critic Score
XOne=df[df.Platform == 'XOne']
XOne=XOne[['Name','Year_of_Release','Critic_Score','User_Score','Total_Sales']].sort_values('Critic_Score',ascending=False)
XOne=XOne.iloc[:9,]
print(XOne)


### Top 10 WiiU by Critic Score
WiiU=df[df.Platform == 'WiiU']
WiiU=WiiU[['Name','Year_of_Release','Critic_Score','User_Score','Total_Sales']].sort_values('Critic_Score',ascending=False)
WiiU=WiiU.iloc[:9,]
print(WiiU)


