import pandas as pd
import numpy as np


#load dataframe
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

#first 5 rows
df_can.head()

#last 5 rows
df_can.tail()

#short summary of dataframe
df_can.info(verbose=False)

#colinms
df_can.columns

#indices
df_can.index

#index and colunms as list
df_can.columns.to_list()

df_can.index.to_list()

#size of dataframe
df_can.shape

#cleaning dataset
#in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

#renaming colunms
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

#add colunm
df_can['Total'] = df_can.sum(axis=1)
df_can['Total']

#to see null objects
df_can.isnull().sum()

#summary
df_can.describe()

#indexing and slicing

#filtering list of countries
df_can.Country  # returns a series

#filtering on the list of countries ('Country') and 
# he data for years: 1980 - 1985.
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]

#selecting row

#setting country colunm as index
df_can.set_index('Country', inplace=True)
df_can.head(3)

#full row data 
df_can.loc['Japan']

# alternate methods
df_can.iloc[87]

df_can[df_can.index == 'Japan']

#for year 2013
df_can.loc['Japan', 2013]

#alternate method
#year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]

#for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]

# to view the number of immigrants from Haiti for the following scenarios: 
# The full row data (all columns) 
# For year 2000
# For years 1990 to 1995
df_can.loc['Haiti']
df_can.loc['Haiti', 2000]
df_can.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]]

#convert the column names into strings: '1980' to '2013'
df_can.columns = list(map(str, df_can.columns))

#declaring a variable that will allow us to easily call upon the full range of years:
years = list(map(str, range(1980, 2014)))
years

#Creating a list named 'year' using map function for years ranging from 1990 to 2013.
#Then extract the data series from the dataframe df_can for Haiti using year list.
year = list(map(str, range(1990, 2014)))
haiti = df_can.loc['Haiti', year] # passing in years 1990 - 2013

#Filtering based on criteria

#create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

#passing this condition into the dataFrame
df_can[condition]

#filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
#note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'

#AreaName is 'Africa' and RegName is 'Southern Africa'
df_can[(df_can['Continent']=='Africa') & (df_can['Region']=='Southern Africa')]

#sorting values of a dataframe
#sorting out dataframe df_can on 'Total' column,
#in descending order to find out the top 5 countries that contributed the most to immigration to Canada.
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5

#top 3 countries that contributes the most to immigration to Canda in the year 2010.
df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010