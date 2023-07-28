#method resulation order
class A:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print("hello from class A")

class B: 
    def __init__(self,job): #constructor overriding
    
        self.job=job

    def hello(self):  #method 
        print(f"hello from class B ")


class C(A,B):
    def __init__(self,name,job):
        A.__init__(self,name)
        B.__init__(self, job)

    def hello(self):
        A.hello(self)
        print(f"{self.name} is {self.job}")

obj = C("takrim","student" )
obj.hello()
print(C.__mro__)  #mro call
