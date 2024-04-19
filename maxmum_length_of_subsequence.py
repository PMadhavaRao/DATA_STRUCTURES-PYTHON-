def sub(l,k):
    right=0
    left=0
    maxlen=0
    n=len(l)
    summ=l[0]
    while right<n:
        while left<=right and summ>k:
            summ-=l[left]
            left+=1
        

        if summ==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<n:
            summ+=l[right]
        
            
        
    return maxlen

l=[1,2,3,1,1,1,1,3,3]
print(sub(l,6))
