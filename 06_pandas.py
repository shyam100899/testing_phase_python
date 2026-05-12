import pandas as pd
s1 = pd.Series([10,20,35,40,50,20,-50])
print(s1[[True,False,True,False,False,True,False]])  
print(s1[s1>20])
print(s1[(s1>20) & (s1<50)])
print(s1[(s1%2 == 0)])
print(s1[(s1%2 != 0)])
print(s1[(s1 != 0) & (s1 <=-1)])
