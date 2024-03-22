def decorator_X(func):
    def wrapper_func():
        print("X"*20)
        func()
        print("X"*20)
    return wrapper_func

def decorator_Y(func):
    def wrapper_func():
        print("Y"*20)
        func()
        print("Y"*20)
    return wrapper_func

# @decorator_X
# @decorator_Y

def say_hello():
    print("Hello World")

hello=decorator_Y(decorator_X(say_hello))
hello()

say_hello()