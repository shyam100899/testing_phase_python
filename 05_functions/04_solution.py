#create a function that returns both area and circumference of a circle given its radius.

import math
r= int(input("enter your radius:\n"))
def circle_stats(r):
    area          = round(math.pi*r**2,2)
    circumference = round(2*math.pi*r,2) 
    return area,circumference
a,c = circle_stats(r)
print(f"area of circle is {a} and circumference of circle {c} ")