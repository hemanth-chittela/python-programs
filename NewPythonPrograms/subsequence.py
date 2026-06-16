s="acb"
t="ahcgdb"
t=list(t)
count=0
Flag=False
increasing=[]
for i in range(len(s)):
    for k in range(len(t)):
        try:
            if s[i]==t[k]:
                increasing.append(k)
                t.remove(t[k])
                count=count+1
                Flag=True
        except:
            continue
if count==len(s):
    Flag=True
    for x in range(len(increasing)-1):
        if increasing[x]<increasing[x+1]:
            Flag=True
        else:
            Flag=False
            break
else:
    Flag=False

if Flag:
    print("true")
else:
    print("false")

