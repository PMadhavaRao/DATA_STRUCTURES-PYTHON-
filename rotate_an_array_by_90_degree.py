def rotate(l):
    n=len(l)-1
    for i in range(len(l)-1):
        for j in range(len(l)):
            l[i][j]=l[j][i]
    for i in l:
        l[l.index(i)]=i[::-1]

    return l

l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate(l))
