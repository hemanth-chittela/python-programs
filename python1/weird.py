import csv
i=0
with open('C:/Users/pc/Desktop/cat/disney.csv') as file1:
    new_file=csv.reader(file1)
    for cat in new_file:
        i=i+1
        print(cat)
print("number of records =",i)