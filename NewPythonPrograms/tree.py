#this is a tree and diamond program for the first for loop will make a tree and the second one will make look like a diamond.
Number=int(input("Enter the number: "))
for i in range(1,Number+1):
    print(" "*(Number-i)+"*"*(2*i-1))
for i in range(Number,0,-1):
    print(" "*(Number-i)+"*"*(2*i-1))
