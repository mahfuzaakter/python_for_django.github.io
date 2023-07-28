# map function
def func(n):
    return n*n*n
l=[1,2,3,4,0,6]

newl= tuple(map(func,l))

print(newl)

new2=list(map(lambda n:n*n*n,l))
print(new2)