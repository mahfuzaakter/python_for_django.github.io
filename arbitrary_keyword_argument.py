#function
def hello (fname="diu",lname="ice"):
    print(f"fullname:{fname} {lname}")
hello()

#arbitrary keywords argument
def fun(**kwargs):
    print(kwargs)


fun(fname="illo",lname="millo",age=23)

def hello3(*args, **kwargs):
    print(args, kwargs)

hello3("villo","thullo", 23,True,False, lname="millo",age=22)