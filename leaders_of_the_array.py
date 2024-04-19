def find(l):
    minn=-999
    l1=[]
    for i in range(len(l)-1,-1,-1):
        if l[i]>minn:
            l1.append(l[i])
            minn=l[i]
    return l1
l=[5,40,3,2,1]
print(find(l))
