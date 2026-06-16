nums=[0]
lister=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        lister.append(nums[i])
for j in range(len(nums)):
    if nums[j]%2==1:
        lister.append(nums[j])
print(lister)