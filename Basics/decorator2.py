from time import time

def timing(func):
    def wrapper_func(*args,**kwargs):
        start=time()
        result=func(*args,**kwargs)
        end=time()
        print(start)
        print(end)
        print("Elapsed time : {}".format(end-start))
        return result
    
    return wrapper_func

@timing
def my_func(num):
    sum=0
    for i in range(num+1):
        sum+=i
    
    return sum
print(my_func(2000000))