# write a funtion to found square of a number

p=int(input("enter your number"))
square_number=p**2
cube_number=p**3
print(f"square of given number {p} is : {square_number}") 

# or

def squar(number):
    square_number=number**2
    return square_number
result = squar(4)
print(result)