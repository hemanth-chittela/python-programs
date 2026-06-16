'''
given_string="dog cat cat fish"
a="dog"
b="cat"
pattern=str(input("enter the pattern: "))
new_list=list(pattern)
given_string=given_string.split(" ")
for i in given_string:
    if i==a:
        print(i)
    elif i==b:
        print(i)
    else:
        print("it is othter which is",i)
'''

dictionary={ "a":"dog",
            "b" :"cat"
}
new_list=[]
pattern=str(input("enter the pattern: "))
s="dog cat cat fish"
s=s.split(" ")
print("s: ",s)
for i in pattern:
        if i in dictionary:
            new_list.append(dictionary[i])
print("new_list is",new_list)
for i in range(len(s)):
    if s[i]==new_list[i]:
        Flag=True
    else:
        Flag=False
        break
if Flag:
    print("True")
else:
    print("False")