import re
number="12345678"
result=re.split("(4)",number)
print(result[0]+result[1])