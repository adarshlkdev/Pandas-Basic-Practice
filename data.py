#Pandas DataFrame

import pandas as pd


#Data Frame in List

list = [3 , 5 ,6]
df = pd.DataFrame(list)
print(df)

list_of_list = [[2 , 4 , 5] , [2 , 7 , 9]]
df = pd.DataFrame(list_of_list)
print(df)

#Data Frame in Dictionary

a  = [{'a ' : 3 , 'b' : 5} , {'a' : 7 , 'b' : 2}]
df = pd.DataFrame(a)
print(df)

b = {'Rollno' : pd.Series([2 , 4 , 5 ,7]) ,
     'Maths' : pd.Series([67 , 89 , 34 , 90]) ,
     'English' : pd.Series([23 , 67 , 89 , 34])}
df = pd.DataFrame(b)
print(df)
