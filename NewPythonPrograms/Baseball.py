list1=["1","C"]
sum=0
total_value=0
new_list=[]
for i in list1:
    if i.isdigit():
        new_list.append(int(i))
    elif i=="C":
        length=len(new_list)
        new_list.pop(length-1)
    elif i=="D":
        length=len(new_list)-1
        index_value=new_list[length]
        result=int(index_value)
        new_value=result*2
        new_list.append(new_value)
    elif i=="+":
        length=len(new_list)-1
        sum=new_list[-1]+new_list[-2]
        new_list.append(sum)
    elif int(i)<0:
        new_list.append(int(i))

for j in new_list:
    total_value=total_value+j
print("total value is = ",total_value)    

