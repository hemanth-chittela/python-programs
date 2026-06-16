string="kartak"
new_list=list(string)
Flag=False
if string==string[::-1]:
    print("true")
else:
    for i in range(len(new_list)-1,-1,-1):
        temp=new_list[:i]+new_list[i+1:]
        if temp==temp[::-1]:
            Flag=True
    if Flag:
        print("True")
    else:
        print("False")