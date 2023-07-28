def hof(fn):
    # print(fn._name_)
    fn()

def greet():
    print("hello!")

def hello():
    print("hello world")

hof(hello)
hof(greet)

li= [1,2,3,4,5,6]
def myfilter(fn,l):
    newl=[]
    for i in l:
        if fn(i):
            newl.append(i)
    return newl
newl= myfilter(lambda x:x%2==1,li)
print(newl)

newli = list(filter(lambda x:x%2==1,li))

print(newli )