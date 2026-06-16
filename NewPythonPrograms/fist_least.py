nums=[1,2,3,4]
new_list=[]
positive_list=[]
for i in range(len(nums)+1):
    if i not in nums:
        new_list.append(i)
for j in new_list:
    if j > 0:
        positive_list.append(j)
print(min(positive_list))