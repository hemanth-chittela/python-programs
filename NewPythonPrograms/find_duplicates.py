list1=[3,1,3,4,2]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[i+1]:
            print(list1[i])