In Python, Every variable in Python holds an instance of an object. There are two types of objects in Python i.e. Mutable and Immutable objects. Whenever an object is instantiated, it is assigned a unique object id. The type of the object is defined at the runtime and it can’t be changed afterward. However, its state can be changed if it is a mutable object.

Mutable Data Type :

list

set

dictionary

array

bytearray

Immutable Data Type:

intergers

floating point

boolean

strings

tuples

frozen set

bytes


>>> list1 =[1,2,3] 
>>> list2 =list1
>>> list2[0]=55
>>> list1              
[55, 2, 3]
>>> list2 
[55, 2, 3]

example 2

>>> mylist1=[1,2,3] 
>>> mylist2=mylist1
>>> mylist1='chai' 
>>> mylist2
[1, 2, 3]
>>> mylist1=[1,2,3]
>>> mylist1        
[1, 2, 3]
>>> mylist2
[1, 2, 3]
>>> mylist1[0]=33
>>> mylist1       
[33, 2, 3]
>>> mylist2
[1, 2, 3]


example 3

>>> list1=[1,2,3] 
>>> list2=list1
>>> list1[0]=44 
>>> list1
[44, 2, 3]
>>> list2
[44, 2, 3]

example 4

>>> m=[1,2,3] 
>>> n=m
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3] 
>>> m==n
True
>>> m is n   
False