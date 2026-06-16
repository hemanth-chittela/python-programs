# Result should be in lexicographical order
string="cbacdcbc"
string=list(string)
new_list={}
for i in string:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)
for key,value in new_list.items():
    while value>1:
        string.remove(key)
        value=value-1
    else:
        continue
string="".join(string)
print(string) 
