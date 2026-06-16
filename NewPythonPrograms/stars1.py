rows=10
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))
print(" "*(rows-2)+"*"*(rows+3-i))
for j in range(0,2):
    print(" "*(rows-2)+"*"*(rows+3-i))
#for k in range(2):
    #print("*"*rows*2)