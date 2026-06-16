#to check the adjacent palindrome
string="11"
Flag=False
for i in range(len(string)-1):
        if string[i]==string[i+1]:
            Flag=True
            break
if Flag:
    print("it is a adjacent palindrome")
else:
    print("It is not a adjacent palindrome")