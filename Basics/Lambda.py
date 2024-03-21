#def double(x):
#    return x*2
#def add(x,y):
#   return x+y
#def product(x,y,z):
#    return x*y*z

double =lambda x : x*2
add=lambda x,y : x+y
product=lambda x,y,z: x*y*z

print(double(10))
print(add(10,20))
print(product(10,20,30))

#map
my_list=[2,5,8,10,9,3]
my_list2=[1,4,7,8,5,1]

a=map(lambda x: x*2, my_list)
print(list(a))
b=map(lambda x,y: x+y,my_list, my_list2)
print(list(b))