def smaller(nums:list[int]):
    count_list=[]
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                count=count+1
        count_list.append(count)
        count=0
    print(count_list)
smaller([5,2,6,1])

