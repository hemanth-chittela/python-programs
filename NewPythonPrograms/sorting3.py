nums=[5]
target=5
final=[]
true_false=[]
if len(nums)==0:
    print([-1,-1])
else:
    for i in range(len(nums)):
        Flag=False
        if nums[i]==target:
            final.append(i)
            Flag=True
            true_false.append(str(Flag))
        else:
            Flag=False
            true_false.append(str(Flag))
if "True" in true_false:
    print([final[0],final[-1]])
else:
    print([-1,-1])