countering=0
for i in range(100):
    s=str(i)
    if len(s)==1:
        countering=countering+1
    elif len(s)>1:
        for j in range(len(s)-1):
            if s[j]!=s[j+1]:
                countering=countering+1
                break
print(countering)        
