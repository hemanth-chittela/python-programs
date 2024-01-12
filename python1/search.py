import re
list=['cat','Carrot','dog','dinosaur','fish','dc']
filtered_list=[items for items in list if re.search("^[cC]",items)]
x=sorted(filtered_list)
print(x)

# Python3 code to demonstrate
# Words starting with specific letter
# using list comprehension + lower()

# initializing list
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat','mka']

# initializing check letter
check = 'A'

res=[list for list in test_list if list[0].upper()==check.upper()]

# print result
print("The list of matching first letter : ",res)
