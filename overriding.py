class A:  
    # for object create
    def __init__(self, name):
        self.name =name
    def hello(self): # method declare 
        print("hello form class A")

class B(A): #child class interit from class A
    def __init__(self,name,job): #constructor overriding
        super().__init__(name) #parent  class er attribute access er jonno
        self.job=job

    def hello(self):  #method overriding
        print(f"hello from class B {self.name} and {self.job}")

obj= B("user","student")
obj.hello()