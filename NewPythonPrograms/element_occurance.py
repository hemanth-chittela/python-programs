numbers=[1,2,2,1]
numbers_list=[]
major={}
for i in numbers:
    if i in major:
        major[i]=major[i]+1
    else:
        major[i]=1
for i,j in major.items():
    numbers_list.append(j)

max_number=max(numbers_list)

for j,k in major.items():
    if k==max_number:
        final_number=j
print(final_number)
