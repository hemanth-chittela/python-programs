nums=[-4,-1,0,3,10]
nums=[x**2 for x in nums]
for i in range(len(nums)-1,-1,-1):
    for j in range(i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
