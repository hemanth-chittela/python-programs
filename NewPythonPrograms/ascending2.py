list1=[5,2,-9,3,5,33,7,366,353,2,3,-9]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)