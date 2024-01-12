file1='cat1.txt'
file2='cat2.txt'
with open(file1,"r") as x:
    reading_file1=x.read()
with open(file2,"r") as y:
    reading_file2=y.read()
with open("cool.txt","a") as k:
    k.write(reading_file1)
    k.write("\n")
    k.write(reading_file2)
