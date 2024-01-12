import re
string="this is an amazing place"
pattern=r"this"

match=re.match(pattern, string)
if match:
    print("it matches",match.group())
else:
    print("it does not match")