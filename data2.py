import pandas as pd
# Reading csv as DataFrames

df = pd.read_csv(r'C:\Users\Adarsh Gupta\OneDrive\Documents\Salary.csv')
'''
print(df)
print(type(df))

print('\n')

print(df.columns)
print(df.shape)  #(rows , columns)
print(df.size)  #no of cells
print(df.head(3))  #first 3 rows
print(df.tail(5))  #last 5 rows
print(df.describe())
print(df.info())
print('Total null values in csv file are : ' ,df.isnull().sum().sum())
'''

print(df.head())

print(df.replace(to_replace='Delhi' , value='Jaipur'))

print(df)