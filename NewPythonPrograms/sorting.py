nums=[342,43,33,0,9,223,43,5,3]
for i in range(len(nums)-1):
    for j in range(0,len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
