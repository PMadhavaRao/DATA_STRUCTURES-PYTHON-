def find(l,target):
    left=0
    right=len(l)-1
    while left<right:
        if l[left]+l[right]==target:
            return left,right
        elif l[left]+l[right]<target:
            left+=1
        else:
            right-=1
l=[1,2,3,4]
print(find(l,7))
