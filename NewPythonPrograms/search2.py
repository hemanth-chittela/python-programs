Flag=False
nums=[4,5,6,7,0,1,2]
target=2
for i in range(len(nums)):
    if nums[i]==target:
        Flag=True
        break
    else:
        Flag=False
if Flag:
    print(i)
else:
    print(-1)