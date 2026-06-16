nums=[-1,0,3,5,9,12]
Target=int(input("Enter the Number: "))
Flag=False
for i in range(len(nums)):
    if nums[i]==Target:
        Flag=True
        break
if Flag:
    print(i)
else:
    print(-1)

