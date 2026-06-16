import os
count=0
path="C:/Users/pc/Desktop/New folder/imp/python"
for i in os.listdir(path):
    count=count+1
    print(i)
print(count)
