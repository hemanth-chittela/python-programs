s="harry"
new_string=""
new={}
character=[]
temp=0
for i in s:
    if i in new:
        new[i]=new[i]+1
    else:
        new[i]=1
for i,j in new.items():
    character.append(j)
sorting=sorted(character)[::-1]
for i in range(len(sorting)):
    for l,m in new.items():
        if sorting[i]==m:
            while temp<sorting[i]:
                temp=temp+1
                if f"{l*m}" in new_string:
                    continue
                else:
                    new_string=new_string+l
            temp=0
print(new_string)
