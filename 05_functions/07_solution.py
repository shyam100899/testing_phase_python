#write a functions that takes variable number of arguments and return their sum.
# it should be *args name nothiing else you can do but not good practice

def sum_all(*args):
    # print(*args)
    # print(args)
    # for i in args:
        # print(i*2)
    return sum(args)
print(sum_all(1,2))

