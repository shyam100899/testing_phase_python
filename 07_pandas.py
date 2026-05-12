import pandas as pd
s1 = pd.Series([10,20,35,40,50,20,-50])
# print(s1+10)
# print(s1-10)
# print(s1*10)
# print(s1/10)
# print(s1+s1*10/100)

s11 =pd.Series([10,20,30])
s12 =pd.Series([1,2,3])
# print(s11+s12) #index match karta hai jaha nahi match karta waha nan aa jata hai

# print(s11[s11>10]*2)

s=pd.Series([10,20,35,40,50,-60])
print(s[s>30]*1.10)
print(s[s<40]-5)
print(s[s>=50]*2)
print(s[s<=20]+100)
print(s[s>40]**2)
print(s[s<30]/2)
print(s[(s>20) & (s<50)] * 1.10)
print(s[(s<0)]* -1)
print(s[(s%20==0)]* 3)
# s.loc[s > 25] += 5
s = s + (s > 25) * 5
print(s)
