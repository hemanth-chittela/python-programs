import re
count=0
name=str(input("Enter the string: "))
for i in name:
    if re.search("[aeiouAEIOU]",i):
        print(i)
        count=count+1
print("the number of vowels in the string",name,"is",count)
