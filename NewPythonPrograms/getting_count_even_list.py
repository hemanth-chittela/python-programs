new_list=[1,222,442334,4422,42]
another_list=[]
for i in new_list:
    strings=str(i)
    if len(strings)%2==0:
        another_list.append(strings)
print(another_list)
print(len(another_list))