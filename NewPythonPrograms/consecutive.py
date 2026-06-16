list1=[0]
new_list=[]
count=0
for i in range(len(list1)):
    if list1[i]==1:
        count=count+1
        new_list.append(count)
    else:
        count=0
        new_list.append(count)
print(max(new_list))
    