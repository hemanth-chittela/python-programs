nums=[-1,-100,3,99]
for i in range(2):
    length=len(nums)
    temp=nums[len(nums)-1]
    nums.pop(length-1)
    nums.insert(0,temp)
print(nums)