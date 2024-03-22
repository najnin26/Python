def decorator_func(func):
    def wrapper_func():
        print("X"*20)
        func()
        print("Y"*20)
    return wrapper_func

def say_hello():
    print("Hello World")

hello=decorator_func(say_hello)
hello()