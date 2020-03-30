import pandas as pd
import numpy
import scipy
import matplotlib



'''Lib Pandas'''



'''Series'''
my_series = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
# create new Series with special index
print(my_series)
print(my_series.index)
# print index
print(my_series.values)
# print values
my_series.name = 'numbers'
# create a name for Series
my_series.index.name = 'letters'
# create a name for indexes
print(my_series)
my_series.index = ['A', 'B', 'C', 'D', 'E', 'F']
# change indexes
print(my_series)
my_series = pd.Series({'a': 1, 'B': 4})
# create new Series in form of a dict
print(my_series)
print(my_series[my_series>3])
# print element with an antecedent



'''DataFrame'''
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
# create a new DataFrame
print(df)
print(df['square'])
# print on index
print(df.index)
# print indexes
df.index = ['KZ', 'RU', "BY", 'UK']
# change indexes
print(df)
df.index.name = "country code"
# create a name for indexes
print(df)
print(df.iloc[1])
# print a numbered list
print(df.loc["UK"])
# print word-named indexes
print(df.loc[["UK", "KZ"], "square"])
# print word-named indexes in only one column
print(df.loc["KZ" : 'BY', :])
# print with a slice
print(df[df.population>10][["square"]])
# print with an antecedent
df.reset_index()
print(df.reset_index())
# clearing indexes; it works only inline
df['density'] = df['population'] / df['square'] * 1000000
# create a new column
print(df)
df.drop(['density'], axis='columns')
print(df.drop(['density'], axis='columns'))
# delete a new column; it works only inline
df['density'] = df['population'] / df['square'] * 1000000
del df['density']
# delete a new column
print(df)
# rename - didn't work



'''Read and write data'''
df.to_csv("test_lib.csv")
# create a new csv file with data from df
df = pd.read_csv("test_lib.csv", sep=',')
# df has now data from csv
print(df)


'''Grouping and aggregation'''
titanic_df = pd.read_csv('titanic.csv')
# read csv file
print(titanic_df.head())
# print the main text
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
# print the number and sexes of survived and not survived people
print(titanic_df.groupby(["PClass", "Survived"])["PassengerID"].count())

'''Analysis of time series'''
apple_df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
# create DatatimeIndex in column 'Date'
apple_df = apple_df.sort_index()
# sorting Date
print(apple_df.info())
# print df
print(apple_df.loc['2012-Feb':"2015-Feb", 'Close'].mean())
# print df for a gap
print(apple_df.resample('W')['Close'].mean())
# print df for a week

'''Visual data'''
import matplotlib.pyplot as plt
# import lib
visual_df = apple_df.loc['2012-Feb':"2015-Feb", 'Close']
# create var with df
visual_df.plot()
# create plot
plt.show()
# show plot



'''all info from 'https://khashtamov.com/ru/pandas-introduction/' '''