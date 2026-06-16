n=2147483645
s=bin(n)
count=0
new_string=""
new_string=new_string+s[2:]
for i in new_string:
    if i=="1":
        count=count+1
print(count)

