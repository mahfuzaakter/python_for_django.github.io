mydict = {'key1':"user",'key2':1234}
print(mydict)

mydict = {}#empty dictionary
print(mydict)

mydict = dict()  #dict function use kore
print(mydict)


mydict['key3'] = "number"  #new valu add korar jonno
print(mydict)

mydict['key4'] ="address"
print(mydict)
del mydict['key3']   # remove korte
print(mydict)


#creat dictionary
a= dict(key1='shirin',key2='diu',key3='23')
print(a)
b= {'key1':"user",'key2':"diu"}
print(b)

#zip akare dictionary creat korte
c=dict(zip(['key1','key2'],['user','diu']))
print(c)

#dictionary creat korte arrayr vitor tuple pass kore
d=dict([('key1','user0'),('key2','ice')])
print(d)

x=list(d)
print(x)

