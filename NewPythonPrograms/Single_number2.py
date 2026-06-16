nums=[0,1]
new_list={}
occurance_once=[]
for i in nums:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)
for key,value in new_list.items():
    if value==1:
        occurance_once.append(key)
print(occurance_once)
        