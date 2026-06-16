def sum_of_digits():  
    adding=0
    Number=int(input("Enter the number you like: "))
    while Number>0:
        adding=adding+Number%10
        Number=Number//10
    print(adding)
sum_of_digits()