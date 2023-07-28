
def myfunc():
    def hello():
        print("hello")

    return hello
f=myfunc()
f()

#wrapper
def mywrapper(fn):
    def test():
        print("before!")
        fn()
        print("after")

    return test

def hello():
    print("hi")

hello= mywrapper(hello)
hello()

def greet():
    print("hello")

greet = mywrapper(greet)
greet()


#decorators
@mywrapper
def funct():
    print("bello")

funct()