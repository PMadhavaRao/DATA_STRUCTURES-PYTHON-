def find(l):
    ind=-1
    for i in range(len(l)-2,-1,-1):
        if l[i]<l[i+1]:
            ind=i
            break
    if ind==-1:
        l.reverse()
    for i in range(len(l)-1,-1,-1):
        if l[i]>l[ind]:
            l[i],l[ind]=l[ind],l[i]
            break
    l1=l[:ind+1]
    l2=l[ind+1:]
    l2.reverse()

    return l1+l2

l=[2,1,5,4,3,0,0]
print(find(l))
