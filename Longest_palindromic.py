'''
s=input()
print(s)
if(len(s)==1):
    print(s)
l=[]
i,j=0,0
k=0
t=""
for i in range(len(s)):
    
    t=s[i]
    j=i+1
    while j<len(s):
    
        t+=s[j]
        if (t==t[::-1]):
            l.append(t)
        j=j+1
if l==[]:
    m=''.join(sorted(s))
    print(m[0])
else:
    res=max(l,key=len)
    print(res)
    
'''
s=input()
print(s[0:3])
ans = s
rev = ans[::-1]
num = len(ans)
if ans==rev:
    print(ans)
else:
    while num:
        num = num-1
        print(num)
        for i in range(len(s)-num+1):
            ans = s[i:i+num]
            rev = ans[::-1]
            if ans==rev:
                print(ans)


