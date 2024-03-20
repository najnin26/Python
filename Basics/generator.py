def my_func():
    #yield "a"
    #yield "b"
    #yield "c"
    for i in range(5):
        print("---------",i)
        yield i
    
x=my_func()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

