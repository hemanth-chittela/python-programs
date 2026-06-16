#to check if i add a for range to see how the execution happens.
string="Helloworld"
new_list={}
for i in range(len(string)):
    for i in string:
        if i in new_list:
            new_list[i]=new_list[i]+1
        else:
            new_list[i]=1
print(new_list)