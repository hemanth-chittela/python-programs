import os

designated_path=str(input("Enter the Path"))
path=f"C:/Users/pc/{designated_path}"
reduce_spaces=path.replace(" ","")
print(reduce_spaces)
files=os.listdir(reduce_spaces)
i=0
for list_of_files in (files):
    i=i+1
    print(list_of_files, i)
print(f"number of files {i}")

