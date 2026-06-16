string="helloworld"
for i in range(len(string)):
    for i in string:
        if i=="l":
            string=string.replace(string[i],"w")
print(string)