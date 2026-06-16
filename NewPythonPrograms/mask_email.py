s="hemanthch1337@outlook.com"
new=[]
s=s.lower()
s1=list(s)
position_of_asterik=[]
for x in range(len(s)):
    if s[x]=="@":
        position_of_asterik.append(x)
        break
for i in range(len(s)):
    if i==0:
        new.append(s[i])
    elif i==1:
        new.append("*****")
    elif s[i]=="@":
        new.append(s[i-1])
        new.append(s[i])
    elif i==2 and s[i-1]=="@":
        new.append(s[i-1])
        new.append(s[i])
    elif i>=position_of_asterik[0]:
        new.append(s[i])
fully_lower_email_masked="".join(new)
print(fully_lower_email_masked)

