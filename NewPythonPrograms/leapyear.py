number1=int(input("Enter the number: "))
if (number1%4==0) and (number1%100!=0) or (number1%400==0):
    print("leap year")
else:
    print("nope") 