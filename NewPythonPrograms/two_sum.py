new_list=[]
index_list=[]
numbers=int(input("Enter the number of numbers: "))
for i in range (numbers):
    s=int(input(f"Enter the number {i+1}: "))
    new_list.append(s)
print(new_list)
selection=int(input("select the number of indexes: "))
sum=0
for i in range(selection):
    j=int(input(f"Enter the index {i+1}: "))
    index_list.append(new_list[j])
    sum=sum+new_list[j]
print(index_list)
print(sum)
    