string="xyz"
new_string=""
for char in string:
    for i in range(97,125):
        if chr(i)=="z":
            new_string=new_string+chr(97)
        elif chr(i)==char:
            new_string=new_string+chr(i+1)
            break
print(new_string)

