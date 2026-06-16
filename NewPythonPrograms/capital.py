string="Google"
new_string=""
Flag=False
new_string=new_string+string[0].upper()+string[1:].lower()
if string==string.lower():
    print("True")
elif string==new_string:
    print("True")
else:
    for i in string:
        if i!=i.upper():
            Flag=True
            break
    if Flag:
        print("False")
    else:
        print("True")
