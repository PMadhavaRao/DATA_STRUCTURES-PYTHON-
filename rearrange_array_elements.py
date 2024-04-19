def finds(l):
    pos=[]
    neg=[]
    new=[]
    for i in range(len(l)):
        if l[i]<0:
            neg.append(l[i])
        else:
            pos.append(l[i])
    if len(pos)>len(neg):
        for i in range(len(neg)):
            l[2*i]=pos[i]
            l[2*i+1]=neg[i]
    ind=len(neg)*2
    for i in range(len(neg),len(pos)):
        l[ind]=pos[i]
        ind+=1
    return l
l=[-1,2,3,4,-3,1]
print(finds(l))
    
    
        











    
