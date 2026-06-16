Name="abc"
new_string=""
for i in Name:
    for j in range(65,124):
        if chr(j)==i:
            new_string=new_string+chr(j+1)
print(new_string)
