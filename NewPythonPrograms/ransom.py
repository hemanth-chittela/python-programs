magazine="a"
ransom_note="a"
new_string=""
Flag=False
count=0
for i in range(len(magazine)):
    if len(ransom_note)>count:
        if magazine[i] in ransom_note[count]:
            new_string=new_string+magazine[i]
            count=count+1
            if new_string==ransom_note:
                Flag=True
                break
if Flag:
    print("True")
else:
    print("False")