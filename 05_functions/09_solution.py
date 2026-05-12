#Write a genarator function  that yields even number upto a specified limit

def even_generator(number):
    for i in range(2,number+1,2):
        yield i
for num in even_generator(10):
    print(num)