s="azxxzy"
s1=list(s)
for x in range(len(s)):
    for i in range(len(s)):
        try:
            if s1[i]==s1[i+1]:
                s1.pop(i)
                s1.pop(i)
                break
        except:
            if len(s)<=x+1:
                break
together="".join(s1)
print(together)