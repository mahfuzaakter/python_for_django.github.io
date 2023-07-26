#sequence unpacking
mytuple =("bangladesh","india","pakistan")
c1,c2,c3 = mytuple
print(c1)
print(c2)
print(c3)

mylist =["bangladesh","india","pakistan","usa"]
c1,c2,*c3 = mylist
print(c1)
print(c2)
print(c3)