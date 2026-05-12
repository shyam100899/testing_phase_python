#write a function that greets a user if no name provided,it should be greet with a default name.

def greet(name='user'):   #default parameter
    return "Hello, "+name+" !"
print(greet("chai"))