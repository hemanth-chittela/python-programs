s="LALL"
new_list={}
Flag=False
for i in s:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)

for key,values in new_list.items():
    if (key=="A" and values<2) or key=="L" and values<3:
        Flag=True
        break
    elif key=="L" and values>=3:
        Flag=False
if Flag:
    print("True")
else:
    print("False")

