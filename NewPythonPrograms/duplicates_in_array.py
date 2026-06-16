list1=[1]
new_list={}
duplicates=[]
for i in list1:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)

for key,values in new_list.items():
    if values>1:
        duplicates.append(key)
print(duplicates)