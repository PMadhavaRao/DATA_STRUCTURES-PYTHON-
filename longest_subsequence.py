def find(l):
    cnt=1
    longest=1
    s=set(l)
    for i in s:
        if i-1 not in s:
            cnt=1
            x=1
            while x+1 in s:
                cnt+=1
                x+=1
        longest=max(longest,cnt)
        
    return longest

l=[101,2,1,1,2,2,102,103,3,4]
print(find(l))
