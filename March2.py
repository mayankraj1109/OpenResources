s=input()
count=0

for i in range(0,len(s)-1):
    if (s[i]==str(0) and s[i+1]==str(1)):
        count=count+1

print(count)
