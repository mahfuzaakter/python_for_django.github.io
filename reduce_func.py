# reduce
from functools import reduce
li=[1,2,3,4,6,8,9]
def func(x,y):
    return x+y

sum= reduce(func,li)
print(sum)

mul2= reduce(lambda x,y:x*y,li)
print(mul2)