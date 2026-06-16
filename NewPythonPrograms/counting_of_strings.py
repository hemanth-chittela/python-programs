name1="bella"
name2="label"
name3="roller"
name=[name1,name2,name3]
duplicate=[]
duplicate1=[]
new_list={}
for i in name:
    for j in range(len(i)):
        if i[j] in new_list:
            k=i[j]
            new_list[k]=new_list[k]+1
        else:
            k=i[j]
            new_list[k]=1
    #print(new_list)
    for key1,value1 in new_list.items():
        if value1>=2:
            duplicate.append(key1)
    new_list.clear()
for char in duplicate:
    duplicate1.append(char)
print(duplicate1)