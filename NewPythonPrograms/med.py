#this will get the correct answer for odd list only only if both are odd length list
list1=[15,3,9,1,12]
list2=[4,18,7,2,11]
Flag=True
sum=0
newlist=[list1,list2]
for i in newlist:
    print("length of list1",len(i))
    if len(i)%2!=0:
        Flag=True
        sorting=i.sort()
        print(i)
        s=len(i)//2
        first_value=i[s]
        print("duplicate value is",first_value)
        sum=sum+first_value
        print(sum)
    else:
        Flag=False
        new_sorting=i.sort()
        print(i)
        s1=len(i)//2
        first_position=s1
        second_position=s1-1
        print(i[first_position],i[second_position])
        median=(i[first_position]+i[second_position])/2
        print("Median is ",median)
if Flag:
    answer=sum/2
    print(round(answer))
else:
    final_value=(sum+median)/2
    print(final_value)
