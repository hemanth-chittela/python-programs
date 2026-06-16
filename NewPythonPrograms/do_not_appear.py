i=1
new_list=[]
nums=[4,3,2,7,8,2,3,1]
for i in range(i,len(nums)+1):
    if i not in nums:
        new_list.append(i)
print(new_list)
