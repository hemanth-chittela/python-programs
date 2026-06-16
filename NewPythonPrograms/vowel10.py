string="elephant"
count=0
flag=False
for i in string:
    if ("a" in i) or ("e" in i) or ("i" in i) or ("o" in i) or ("u" in i) or ("A" in i) or ("E" in i) or ("I" in i) or ("O" in i) or ("U" in i):
        flag=True
        count=count+1
        print(i,end=" ")
print("count is :",count)
if flag:
    print("it is a vowel")
else:
    print("it is a consonent")

