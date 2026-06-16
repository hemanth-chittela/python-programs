string="......a....."
string=string.lower()
new_list=list(string)
special_characters=[]
print(new_list)
for i in new_list:
    if not i.isalnum():
        special_characters.append(i)
#for j in range(len(new_list)):
#    for j in new_list:
#        if j in special_characters:
#            new_list.remove(j)
filtered=[ch for ch in new_list if ch not in special_characters]
print("filtered",filtered)
print(new_list)
making_string="".join(filtered)

print(making_string)

reverse=making_string[::-1]
print(reverse)
if making_string==reverse:
    print("palindrome")
else:
    print("Non palindrome")



