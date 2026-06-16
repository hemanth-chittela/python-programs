nums=[1,2,2,4]
count=0
new_list=[]
counting={}
final_list=[]
for i in nums:
    if i in counting:
        counting[i]=counting[i]+1
    else:
        counting[i]=1
for i,j in counting.items():
    if j>=2:
        new_list.append(i)

for x in nums:
    count=count+1
    if count not in nums:
            new_list.append(count)
print((new_list))