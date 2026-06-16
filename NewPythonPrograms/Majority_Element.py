new_list={}
max_list=[]
nums=[2,2,1,1,1,2,2]
for i in nums:
    to_string=str(i)
    if to_string in new_list:
        new_list[to_string]=new_list[to_string]+1
    else:
        new_list[to_string]=1
for i in new_list:
    max_list.append((new_list[i],i))
print(int(max(max_list)[1]))