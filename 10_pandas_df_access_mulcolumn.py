import pandas as pd

#by dictionary
df =pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
print(df["age"])
print(df.age)   # for single column value
print(df[["age","name"]])
print(df.iloc[0])
print(df.iloc[0:4])
print(df.loc[0:4])
print(df.iloc[0:4,0:3])
print(df.loc[0:3,["name","age"]])
df.index=['a','b','c','d','e']
print(df.loc['a':'c'])
