string_bit=""
n=4
s=bin(n)
string_bit=s
string_bit=string_bit[2:]
single_bit=string_bit[0]
print(single_bit)
same_bits=[]
first_same_bit=""
for i in range(len(string_bit)):
    if int(string_bit[i])==int(single_bit) and i%2==0:
        same_bits.append(string_bit[i])
        Flag=True
    elif int(string_bit[i])!=int(single_bit) and i%2!=0:
        same_bits.append(string_bit[i])
        Flag=True
    else:
        Flag=False
        break
#first_same_bit=same_bits[0]
#print(same_bits)
#print(first_same_bit)
#for j in range(len(same_bits)):
#    if j%2==0 and int(same_bits[j])==int(first_same_bit):
#        Flag=True
#    elif int(same_bits[j])==int(first_same_bit):
#        Flag=False
#        break
if Flag:
    print("true")
else:
    print("false")
        