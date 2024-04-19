def find(l):
    sum=0
    maxx=-99
    for i in l:
        sum+=i
        if sum<0:
            sum=0
        elif sum>maxx:
            max=sum
    return max

l=[1,2,3,99,-4,-5,6,1,2,3]
print(find(l))
