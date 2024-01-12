import os
number=input("Enter the list of folders: ").split()
count=0
for i in number:
    try:
        files=os.listdir(i)
    except FileNotFoundError:
        print("file not found which is",i)
    except PermissionError:
        print("Permission required for this file", i)
        break
    else:
        print("files in the folder",i)
        for files1 in files:
            print(files1)
        for i in files:
            count=count+1
        print("the number of files are",count)
        count=0
    
    