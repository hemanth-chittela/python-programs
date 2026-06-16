text="leetcode"
string1="ballon"
new={}
final=""
count_of_ballons={}
for i in text:
    if i in new:
        new[i]=new[i]+1
    else:
        new[i]=1
print(new)
for i in range(len(text)):
    for i in new:
        if new[i]==0:
            break
        elif i=="b":
            new[i]=new[i]-1
        elif i=="a":
            final=final+i
            new[i]=new[i]-1
        elif i=="l":
            new[i]=new[i]-1
        elif i=="o":
            new[i]=new[i]-1
        elif i=="n":
            new[i]=new[i]-1


