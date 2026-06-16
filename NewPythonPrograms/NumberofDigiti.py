import re
Number=int(input("Enter the number: "))
string=""
string2=""
count=0
count1=0
result=Number//2
print(result)
for i in range(0,result+1):
    i=str(i)
    string=string+i
print(string)
for c in string:
    if c=="1":
        count=count+1
print("first count is",count)
for j in range(result+1,Number+1):
    j=str(j)
    string2=string2+j
print(string2)
for k in string2:
    if k=="1":
        count1=count1+1
print("second count",count1)
final=count+count1
print("the number of 1's in final count is",final)
