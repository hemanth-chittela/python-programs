string1="harry"
new_dict={}
for i in string1:
    if i in new_dict:
        new_dict[i]=new_dict[i]+1
    else:
        new_dict[i]=1
print(new_dict)