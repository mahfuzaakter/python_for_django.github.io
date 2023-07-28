# filter function

l=[1,2,5,6,9,7]

def func(n):
    return n%2==1

new =tuple(filter(func,l))
new1 = list(filter(func,l))
print(new1)
print(new)

new2=tuple(filter(lambda n: n%2 !=1,l))
print(new2)