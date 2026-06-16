s=[1,2,3,4,5,6,7,8]
for i in range(len(s)//2,len(s)):
    for j in range(i+1,len(s)):
        if s[i]<s[j]:
            s[i],s[j]=s[j],s[i]
print(s)