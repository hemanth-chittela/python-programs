num="88742133111887777"
new_list=""
#number_list=[]
new_dicto={}
maximum_numbers=[]
count=0
#finally_number_list=[]
final_string=""
for i in range(len(num)-1):
    if num[i]==num[i+1]:
        if count<=0:
            new_list=new_list+num[i]+num[i+1]
            count=count+1
        elif num[i] in new_list[-1]:
            new_list=new_list+num[i]
            count=0
other_list=list(new_list)
if len(other_list)<3:
    print(final_string)
else:
    for k in other_list:
        if k in new_dicto:
            new_dicto[k]=new_dicto[k]+1
        else:
            new_dicto[k]=1
    print(new_dicto)
    for key1,value1 in new_dicto.items():
        if value1<3:
            continue
        else:
            maximum_numbers.append((int(key1),value1))
        new_max=max(maximum_numbers)
        final_maximum=new_max[0]    
#if len(other_list)>=3:    
#    for p in range(len(other_list)):
#        i=int(other_list[p])
#        number_list.append(i)
#        maxi=max(number_list)
    if len(maximum_numbers)==0:
        print(final_string)
    else:
        for x in range(3):
            final_string=final_string+str(final_maximum)
        print(final_string)
#    print(final_string)
#else:
#     print(final_string)