class A:  
    # for object create
    def __init__(self, name):
        self.name =name
    def hello(self): # method declare 
        print("hello form class A")

#object calling
obj= A("user")
obj.hello() #method call

class B(A): #inherate from A class
    pass
objb= B("surah")
objb.hello()
        