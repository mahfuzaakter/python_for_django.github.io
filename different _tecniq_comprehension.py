#comprehension 
#iterable-> list, tuple, dictionary, set,range
#all types of for loop
#creat-> list , dictionary,set

mylist = [1,2,3,4,5,6]
#from list
newlist =[i+1 for i in mylist]
newdict = {i: i*i for i in mylist}
newset = {i**3 for i in mylist}  #unsorted result dibe
newtuple =tuple(i**4 for i in mylist) #tuple keyword diye nite hobe
newtuplelist =[(i,i**2)for i in mylist]

print(newlist)
print(newdict)
print(newset)
print(newtuple)
print(newtuplelist)

#from dictionary
mydict ={"name":"user","address":"dhaka","id":1234}

newlist1=[key for key, value in mydict.items()]
newtlist1=[(key,value) for key, value in mydict.items()]
newdict1= {key +"key": value for key ,value in mydict.items()}

print(newlist1)
print(newtlist1)
print(newdict1)