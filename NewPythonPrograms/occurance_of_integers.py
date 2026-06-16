list1=[1,2,3,4,10]
list2=[4,2,2,2,4,4,5,1,2,3,4,2,5,5,3,4]
count=0
for i in list1:
    for j in list2:
        if i == j:
            count=count+1
    print(i,":Occurance",count)
    count=0
