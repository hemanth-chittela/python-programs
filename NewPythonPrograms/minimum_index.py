list1=["Shogun","Tapioca Express","Burger King","KFC"]
list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
new_list={}
sum=0
new=0
number_list=[]
final_list=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            sum=i+j
            new_list[list1[i]]=sum
            sum=0
for i,j in new_list.items():
    number_list.append(j)
min_number=min(number_list)
for x,y in new_list.items():
    if min_number==y:
        final_list.append(x)
print(final_list)


