import sys


#num1=10
#num2=5
def add(num1,num2):
    c=num1+num2
    return c

def substraction(num1,num2):
    sub=num1-num2
    return sub
    
def multipication(num1,num2):
    mul=num1*num2
    return mul

def divison(num1,num2):
    div=num1/num2
    return div


num1=int(sys.argv[1])
operator=sys.argv[2]
num2=int(sys.argv[3])


if operator=="add":
    output=add(num1,num2)
    print(output)
elif operator=="substraction":
    output1=substraction(num1,num2)
    print(output1)
elif operator=="multiplication":
    output2=multipication(num1,num2)
    print(output2)
elif operator=="division":
    output3=divison(num1,num2)
    print(output3)

