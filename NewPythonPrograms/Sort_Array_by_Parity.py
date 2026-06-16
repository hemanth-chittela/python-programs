nums=[2,3]
final=[]
i=0
reduction=1
counting_numbers={}
for j in range(len(nums)):
    if nums[j] in counting_numbers:
        counting_numbers[nums[j]]=counting_numbers[nums[j]]+1
    else:
        counting_numbers[nums[j]]=1
while i<len(nums):
    for x in range(len(nums)):
        if i%2==0:
            if counting_numbers[nums[x]]==0:
                continue
            elif nums[x]%2==0:
                final.append(nums[x])
                i=i+1
                counting_numbers[nums[x]]=counting_numbers[nums[x]]-reduction
        elif i%2!=0:
            if counting_numbers[nums[x]]==0:
                continue
            elif nums[x]%2!=0:
                final.append(nums[x])
                i=i+1
                counting_numbers[nums[x]]=counting_numbers[nums[x]]-reduction
print(final)