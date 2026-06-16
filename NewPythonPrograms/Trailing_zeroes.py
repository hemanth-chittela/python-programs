#trailing_zeros
import sys
Number=int(input("Enter the Number: "))
sys.set_int_max_str_digits(100000)
sum=1
count=0
for i in range(1,Number+1):
    sum=sum*i
print(sum)
sum=str(sum)
for i in range(len(sum)-1,-1,-1):
    if int(sum[i])==0:
        count=count+1
    else:
        break
print(count)