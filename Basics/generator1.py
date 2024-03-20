def ListIterator(list):
    for i in list:
        yield i
    
a=[1,2,3,4,5]
mylist=ListIterator(a)

#print(next(mylist))
#print(next(mylist))
#print(next(mylist))
#print(next(mylist))
#print(next(mylist))

for x in mylist:
    print(x)