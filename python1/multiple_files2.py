import os
def files(path):
    for paths in path:
        for list in (paths):
            x=os.listdir(paths)
        print("------------------")
        for list2 in x:
            print(list2)

result=input("Enter the file path: ").split()
files(result)