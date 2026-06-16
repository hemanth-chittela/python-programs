n=20
sum=0
final_sum=0
count=0
number_list=[]
for i in range((n//7)+1):
    for j in range(1,8):
        sum=sum+i+j
        number_list.append(sum)
        sum=0
for x in range(len(number_list)):
    final_sum=final_sum+number_list[x]
    count=count+1
    if count==n:
        break
print(final_sum)



    