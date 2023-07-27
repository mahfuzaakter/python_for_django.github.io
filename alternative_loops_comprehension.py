
mylist = [1,4,5,2,9,6]
newlist = []

for i in mylist:
    newlist.append(i*i)

print(mylist)
print(newlist)

#comprehension diye


for i in mylist:
    newlist.append(i*i)

comlist = [i*i for i in mylist]   #this is called compresion

print(comlist)


#list of the squere of tha odd number


for i in mylist:
    if i%2 ==1:
      newlist.append(i*i)

print(newlist)


comlist = [i*i for i in mylist if i%2==1]   #this is called compresion

print(comlist)