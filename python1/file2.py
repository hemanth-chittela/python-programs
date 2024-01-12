with open("newfile1.txt","w") as file2:
    file2.write("this is file 2")
with open("newfile1.txt","r") as file2:
    print(file2.read())