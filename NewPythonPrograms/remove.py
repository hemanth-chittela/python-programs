# to remove the elements from the list. I have writtten in two ways can be used accordingly by giving ''' 
list1=[3,2,2,3]
Number=int(input("Enter the Number: "))
for i in range(len(list1)):
    if Number in list1:
        remove=list1.remove(Number)
print(list1)

def remove(nums: list[int], val: int):
    for i in range(len(nums)):
        if val in nums:
            removed=nums.remove(val)
    return nums
s=remove([3,2,2,3],3)
print(s)

