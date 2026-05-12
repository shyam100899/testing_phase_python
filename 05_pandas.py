
import pandas as pd
s1 = pd.Series([1,2,3,4,5,None,2], index=['a','b','c','d','e','f','g'])
print(s1.describe())      # Statistical summary
print(s1.value_counts())  #how much time a element in serires none ko count nhi karta hai
print(s1.unique())        #list of unique element in serires including none value
print(s1.nunique())       #number of element in serires ecept none value
print(s1.sort_values())   #sorting of element by value with its indexing in serires
print(s1.sort_index())    #sorting of element by index with its value in serires
print(s1.agg(['sum', 'mean', 'std']))   #aggregate of same type function in serires just like sum ,mea,std mode etc