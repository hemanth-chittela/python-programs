string="Hello@World! 123 #Python"
string1=list(string)
special_characters=[]
#string=string.replace(" ","")
for i in string:
    if not i.isalnum():
        special_characters.append(i)
print(special_characters)
for j in range(len(string1)):
    for j in string1:
        if j in special_characters:
            string1.remove(j)
string1="".join(string1)
print(string1)