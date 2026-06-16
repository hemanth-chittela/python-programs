nums = [-2,0,-1]
list1=[]
try:
    if len(nums)==1:
        print(nums[0])
    else:
        for i in range(len(nums)):
            list1.append(nums[i]*nums[i+1])
except:
    print(max(list1))
