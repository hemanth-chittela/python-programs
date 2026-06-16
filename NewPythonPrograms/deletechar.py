string="aab"
count=0
new_string=" "
k=0
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        if count<1:
            if string[i] not in new_string[-1]:
                for j in range(2):
                    new_string=new_string+string[i+1]
                    count=count+1

            elif k<1: 
                for k in range(1):
                    new_string=new_string+string[i+1]
                    k=k+1
                    count=count+1
                    k=0
            else:
                continue
    elif string[i] in new_string:
        new_string=new_string+string[i+1]
        count=0
    else:
        new_string=new_string+string[i]
        count=0
print(new_string[1:])


