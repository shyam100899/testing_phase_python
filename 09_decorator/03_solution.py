import time
def debug(func):
    cached_value={}
    print(cached_value)
    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result= func(*args)
        cached_value[args]=result
        return result

    return wrapper

@debug
def addition(a,b):
   time.sleep(4)
   return a+b

print(addition(4,3))
print(addition(4,3))