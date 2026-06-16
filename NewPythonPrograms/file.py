with open("newfile.txt", "w") as file1:
        file1.write("hello devops")
with open("newfile.txt", "r") as file1:
        print(file1.read())