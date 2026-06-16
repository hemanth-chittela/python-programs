import os
count=0
files=input("Enter the path: ").split()
for file in files:
   x=os.listdir(file)
   print("----the files in-------",file)
   for file1 in x:
    print(file1)
   for i in x:
     count=count+1
   print("number of files in the",file,"",count)
   count=0