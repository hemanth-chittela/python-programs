list1=["cat","bat","rat"]
string="the cattle was rattled by the battery"
string=list(string.split(" "))
print(string)
for i in range(len(list1)):
    for j in range(len(string)):
        if list1[i][0]==string[j][0]: 
            if len(string[j])==2:
                print(string)
            else:
                string[j]=list1[i]
string=" ".join(string)
print(string)
        
