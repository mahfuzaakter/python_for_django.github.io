# multilevel inheritance
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


class C(B):
    pass

#multiple
class D(C,A):
    pass

obj=C("user","student")
print(obj.__dict__)
print(obj.__dir__)
print(dir(obj))

obj1=D("user","mentor")

print(obj1.__dict__)
print(dir(obj1))
