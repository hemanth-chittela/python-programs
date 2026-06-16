#duplicate lists
list1=[10,2,4,22,34,22,23,1,2,3,1]
new_list={}
duplicates=[]
for i in list1:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)
for key,value in new_list.items():
    if value>1:
        duplicates.append(key)
print(duplicates)
    