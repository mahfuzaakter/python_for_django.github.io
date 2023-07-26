mylist = ['apple','orange','mango','banana']
mylist2=[1,2,3.4]


#enumerate function use kore
for  i, fruit in enumerate(mylist):
    print(f"{i} index of {fruit}")


#zip function diye list ke parallal e add korar jonno
for i,j in zip(mylist,mylist2):
   print(i,j)

#sequence ke sorted vabe dekhanor jonno
for i in sorted(mylist):
   print(i)


#reverse vabe dekhanor jonno
for i in reversed(sorted(mylist)):
   print(i)