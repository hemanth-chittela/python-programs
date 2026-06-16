Bank_balance=934.54
while True:
    try:
        Number=float(input("Enter the amount you want to Deposit: "))
        Bank_balance=Bank_balance+Number
        print(Bank_balance)
        break
    except ValueError:
        print("the input should not be an character")