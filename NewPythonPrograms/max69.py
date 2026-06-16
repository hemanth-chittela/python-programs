num=9999
num=str(num)
num=list(num)
print(num)
new_list=[]
to_string=[]
for i in num:
    s=int(i)
    new_list.append(s)
for i in range(len(new_list)):
    if new_list[i]==6:
        new_list[i]=9
        break
for i in range(len(new_list)):
    to_string.append(str(new_list[i]))

to_string="".join(to_string)
print(type(int(to_string)))