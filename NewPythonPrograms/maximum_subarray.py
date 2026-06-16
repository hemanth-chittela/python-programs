# I am adding the list and pop 1 element out from the 0 index and adding once again and storing in the compare list
sum=0
compare_list=[]
list1=[5,4,-1,7,8]
if len(list1)==1:
    print(list1[0])
else:
    for j in range(len(list1)):
        for i in list1:
            if len(list1)==1:
                compare_list.append(list1[0])
                break
            else:
                sum=sum+i
        compare_list.append(sum)
        sum=0
        if len(list1)%2==0:
            j=-1
            compare_list.append(list1[-1])
            list1.pop(j)
        else:
            j=0
            list1.pop(j)
        print(list1)
        print(compare_list)
    compare_list.pop(-1)
    print(max(compare_list))
    