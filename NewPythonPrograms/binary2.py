num=[1,2,0,0] 
k=34
to_string=""
to_list_number=[]
for i in range(len(num)):
    to_string=to_string+str(num[i])
to_number=int(to_string)
result=to_number+k
convert_result_to_string=str(result)
for i in convert_result_to_string:
    i=int(i)
    to_list_number.append(i)
print(to_list_number)