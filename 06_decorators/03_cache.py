import time

def cache(func):
    cache_values = {}
    print(cache_values)
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(3)
    return a + b

print(long_running_function(2,4))
print(long_running_function(2,4)) #this will be printed immediatly as the values 
                                  # are same so they will be fetched from cache_values
print(long_running_function(5,4))
