list1=[1,2,3,4,5,6,7,8,9,10,11,43]
target=int(input("Enter the Target: "))
lower_bound=0
upper_bound=len(list1)-1
while lower_bound<=upper_bound:
    mid=(lower_bound+upper_bound)//2
    if list1[mid]==target:
        print("Found at Target",mid)
        break
    else:
        if list1[mid]<target:
            lower_bound=mid+1
        else:
            upper_bound=mid-1