nums=[5,4,3,2,1]
Flag=False
try:
    for i in range(len(nums)):
        if nums[i]<nums[i+1]<nums[i+2]:
            Flag=True
            break
    if Flag:
        print("True")
    else:
        print("False")
except:
    if Flag:
        print("true")
    else:
        print("False")
