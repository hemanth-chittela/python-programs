#Unique character index in Name
name=str(input("Enter the name: "))
new_dictionary={}
for i in name:
    if i in new_dictionary:
        new_dictionary[i]=new_dictionary[i]+1
    else:
        new_dictionary[i]=1
print(new_dictionary)
Flag=False
for key,values in new_dictionary.items():
    if values==1:
        Flag=True
        break
if Flag:
    index=name.index(key)
    print(index)
else:
    print("-1")