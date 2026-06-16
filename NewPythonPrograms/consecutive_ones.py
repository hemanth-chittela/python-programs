list1=[1,1,1,0,0,0,1,1,1,1,0]
count=2
starting=0
number_of_consecutive_ones=0
for i in range(len(list1)):
        if list1[i]==0 and count>starting:
            list1[i]=1
            starting=starting+1
print(list1)
for number in list1:
    if number==1:
        number_of_consecutive_ones=number_of_consecutive_ones+1
    else:
         break
print(number_of_consecutive_ones)
