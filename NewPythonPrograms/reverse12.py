number=int(input("Enter the number: "))
if number>0:
    number=str(number)
    reversing=(number[::-1])
    print(int(reversing))
else:
    number<0
    number=str(number)
    number=number.replace("-","")
    number=number[::-1]
    print(-int(number))
