Sum=0
Sum1=0
Sum2=0
new_list=[]
Number=int(input("Enter the Number: "))
while Number>0:
    Sum=Sum+Number%10
    Number=Number//10
addition=Sum
for ch in str(addition):
    new_list.append(int(ch))
for ch1 in new_list:
    Sum1=Sum1+ch1
while Sum1 > 0:
    Sum2=Sum2+Sum1%10
    Sum1=Sum1//10
final_value=Sum2
print(final_value)
print(new_list)