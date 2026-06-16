list1=[33,45,23,3,0,9,34,98,294]
maximum=list1[0]
minimum=list1[0]
for i in list1:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(maximum)
print(minimum)