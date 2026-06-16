number=int(input("Enter the number: "))
number=str(number)
if "0" in number:
    number=number.replace("0","")
    number=number[::-1]
    print(number)