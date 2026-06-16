
list1=[]
difference=[]
list1.sort()
print(list1)
Flag=False
for i in range(len(list1)-1,0,-1):
    if len(list1)>1:
        diff=list1[i]-list1[i-1]
        difference.append(diff)
        Flag=True
if Flag:
    print(list1)
    print("Maximum difference",max(difference))
else:
    print("0")


'''
def c(nums: list [int]):
        difference=[]
        nums.sort()
        Flag=False
        for i in range(len(nums)-1,0,-1):
            if len(nums)>2:
                diff=nums[i]-nums[i-1]
                difference.append(diff)
                Flag=True
        if Flag:
             return max(difference)
        else:
             return 0 
s=c([10])
print(s)
'''
