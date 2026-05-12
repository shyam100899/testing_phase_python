# compute factorail of a number using
number = 5
factorial = 1
while (number>0):
    factorial *= number
    number    -= number
print("factorial of number is",factorial)