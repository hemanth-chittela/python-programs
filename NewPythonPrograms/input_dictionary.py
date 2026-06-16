new_list={}

for i in range(2):
    Name=str(input("Name: "))
    Age=str(input("Age: "))
    City=str(input("City: "))

    new_list['Name']=Name
    new_list['Age']=Age
    new_list['City']=City

    print(new_list)

list1=[2,4,5,6,7,8,10]
list2=[3,4,5,6,7,78,9]
adddition=[]
for i in range(len(list1)):
    adddition.append(list1[i]+list2[i])
print(adddition)
