nums=[4,1,2,1]
final=[]
i=0
reduction=1
counting_numbers={}
for j in range(len(nums)):
    if j in counting_numbers:
        counting_numbers[nums[j]]=counting_numbers[nums[j]]+1
    else:
        counting_numbers[nums[j]]=1
print(counting_numbers[4]-1)
print(counting_numbers[4])