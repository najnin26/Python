def my_func():
    yield "a"
    yield "b"
    yield "c"
    
x=my_func()
print(next(x))
print(next(x))
print(next(x))
print(next(x))