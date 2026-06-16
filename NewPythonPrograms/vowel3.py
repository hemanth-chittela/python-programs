import re

string="hello world"
count=0
for i in string:
    if re.search("[aeiouAEIOU]",i):
        count=count+1
print(count)
