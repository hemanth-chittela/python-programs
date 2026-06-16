import os
count=0
path=f"C:/Users/pc/Desktop/New folder/imp/python"
for list in os.listdir(path):
    count=count+1
    print(list)
print(count-1)