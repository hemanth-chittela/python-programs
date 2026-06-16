string1="oyiff######exwh" 
string2="oyiff#######exwh"  
newstring=""
newstring2=""
string1=list(string1)
string2=list(string2)
for i in range(len(string1)):
    try:
        if string1[0]=="#":
            string1.pop(i-i)
        elif string1[i]=="#" and string1[i-1]=="#":
            string1.pop(i-1)
            string1.pop(i-2)
        elif string1[i]=="#":
            string1.pop(i)
            string1.pop(i-1)
    except:
        for j in range(len(string1)):
            if len(string1)==0:
                break
            elif len(string1)==1:
                break
            elif string1[0]=="#":
                string1.pop(j-j)
            elif string1[j]=="#" and string1[j-1]=="#":
                string1.pop(j-1)
                string1.pop(j-2)
            elif string1[j]=="#":
                string1.pop(j)
                string1.pop(j-1)
                break
            else:
                 for x in range(len(string1)):
                    if string1[x]=="#":
                        string1.pop(x)
                        string1.pop(x-1)
                        break
                    break                        
                    

for each in string1:
    if each!="#":
        newstring=newstring+each
for k in range(len(string2)):
    try:
        if string2[0]=="#":
            string2.pop(k-k)
        elif string2[k]=="#" and string2[k-1]=="#":
                string2.pop(k-1)
                string2.pop(k-2)
        elif string2[k]=="#":
             string2.pop(k)
             string2.pop(k-1)
    except:
        for p in range(len(string2)):
            if len(string2)==0:
                break
            elif len(string2)==1:
                break
            elif string2[0]=="#":
                 string2.pop(p-p)
            elif string2[p]=="#" and string2[p-1]=="#":
                string2.pop(p-1)
                string2.pop(p-2)
            elif string2[p]=="#":
                string2.pop(p)
                string2.pop(p-1)
                break
            else:
                for y in range(len(string2)):
                    if string2[y]=="#":
                        string2.pop(y)
                        string2.pop(y-1)
                        break
                    break
    
for each1 in string2:
    if each1!="#":
        newstring2=newstring2+each1

if newstring==newstring2:
    print("True")
else:
    print("False")