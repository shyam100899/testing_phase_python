#create a function that aceept any number of keyword argument and print them in format of key value.

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="ram")
print_kwargs(name="shyam",age=18)