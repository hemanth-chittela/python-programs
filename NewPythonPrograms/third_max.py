numbers=[2,2,3,1]
final=[]
new_list={}
for i in numbers:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1

for key,value in new_list.items():
    final.append(key)

sort1=sorted(final)

if len(sort1)>=3:
    print(sort1[-3])
elif len(sort1)==2:
    print(sort1[-1])
else:
    print(sort1[-1])
