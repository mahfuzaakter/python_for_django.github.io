mylist=[letter for letter in 'bohubrihi']
print(mylist)

mylist1=[letter.upper() for letter in 'bohubrihi']
print(mylist1)


# nested loop 
# mymatrix= [[0,1,2,3],[0,1,2,3],[0,1,2,3]]#ei output ber korar jonno  nasted loop 

matrix= []
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)
print(matrix)

#nasted comprehentsion
mymatrix = [[ j for j in range(4)] for i in range(3)]
print(mymatrix)