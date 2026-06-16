number=5
number=bin(number)
new_string=""
remove=number[2:]
for i in remove:
    if i=="1":
        new_string=new_string+"0"
    else:
        new_string=new_string+"1"
to_convert_to_number=int(new_string,2)
print(to_convert_to_number)