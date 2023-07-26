# for i in tuple, range, dictionary, list
mytuple = ("a","b","c","d")
mylist =[("a",1),("b",2),("c",3)]
mydict = {"name":"user","add":"ice","country":"bangladesh"}
mystr ="daffo"
myset ={"bd","tk"}
for x,y in mylist:
    print(x)
    print(f"{x},{y}")


for key,value in mydict.items():
    print(f"{key} => {value}")

for i in mystr:
    print(i)

for currency in myset:
    print(currency)