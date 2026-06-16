print("before appending")

with open("newfile.txt","r") as file:
    print(file.read())
    file.close()
with open ("newfile1.txt","r") as file1:
    print(file1.read())
    file.close()

print("After appending")

source_file='newfile.txt'
with open(source_file,"r") as x:
    appending_the_content=x.read()

destination_file='newfile1.txt'
with open(destination_file,"a") as y:
    y.write(" ")
    y.write(appending_the_content)

with open(destination_file,"r") as t:
    print(t.read())

