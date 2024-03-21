#NESTED FUNCTION


# def OuterFunction(text):
#     def InnerFunction():
#         print(text)
#     InnerFunction()
    
# OuterFunction("Hello")

def pop(list):
    def get_last_item(my_list):
        return my_list[len(list)-1]
    
    list.remove(get_last_item(list))
    return list

a=[1,2,3,4,6]
print(pop(a))
print(pop(a))
print(pop(a))

#CLOSURE

# def OuterFunction(text):
#     def InnerFunction():
#         print(text)
#     return InnerFunction
    
# a=OuterFunction("Hello")
# del OuterFunction
# a()

def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

s=nth_power(2)
print(s(2))
print(s(3))
print(s(4))
print(s(5))

cube=nth_power(3)
print(cube(2))
print(cube(3))
print(cube(4))
print(cube(5))
