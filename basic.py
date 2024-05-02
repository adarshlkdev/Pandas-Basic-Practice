import pandas as pd

list = [1 , 3 ,4 ,5]

#Python Series with list
a = pd.Series(list)


print(a)
print(type(a))

empty = pd.Series([])
print(empty)

a = pd.Series(['a' , 'e', 'i' , 'o' , 'u'] , index = [10 , 11 , 12 , 13 ,14])
print(a)

a = pd.Series(['a' , 'e', 'i' , 'o' , 'u'] , index = [10 , 11 , 12 , 13 ,14] , name = 'vowels')
print(a)


#Python Series with Dictionary

dict_series = pd.Series({'p' : 1 , 'q' : 3 , 'r' : 6})
print(dict_series)
print(max(dict_series))

dict_series = pd.Series({'p' : [2 , 4 , 5] , 'q' : [3 , 5 , 6] , 'r' : [1 , 6 ,8]})
print(dict_series)

