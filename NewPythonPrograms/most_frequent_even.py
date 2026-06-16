numbers=[2,10000,10000,10000,2]
new_list={}
even_list=[]
for i in numbers:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1

print(new_list)
Flag=False
for key,values in new_list.items():
    if (key%2==0 and values >1) or len(numbers)==1:
        even_list.append((key,values))
        print(even_list)
        Flag=True
if Flag:
    print(min(even_list)[1])
else:
    print(-1)

12345678910111213