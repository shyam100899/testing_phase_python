#write a function  to found factorail of a number

def factorial(num):
    if num==0:
        return 1
    else:
        fact = num*factorial(num-1)
        return fact
print(factorial(5))