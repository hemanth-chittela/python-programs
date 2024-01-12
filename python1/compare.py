list1=[1,2,3,4,5]
list2=[1,2,3,5,5]
print(list1)
print(list2)
result=[]
for i in range(len(list1)):
    result.append(list1[i]==list2[i])
print(result)