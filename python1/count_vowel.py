import re
name="oogway"
count=0
for char in name:
    if re.search("[aeiouAEIOU]",char):
        print(char)
        count=count+1
print("the number of vowels in the string",name,"is",count)
