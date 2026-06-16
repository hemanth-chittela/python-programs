import os

def files(paths):
    for path in paths:
        x = os.listdir(path)
        print("------------------")
        for file_name in x:
            print(file_name)

# Take user input for the paths
result = input("Enter the file paths: ").split()
files(result)
