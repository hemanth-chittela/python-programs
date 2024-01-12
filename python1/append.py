with open("newfile.txt","r") as file:
    print(file.read())
with open("newfile.txt","a") as file:
    file.write(" Hey There")
with open("newfile.txt","r") as file:
    print(file.read())

