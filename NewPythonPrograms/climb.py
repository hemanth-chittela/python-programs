def fibonacci(n):
    number1=1
    number2=2
    print(number1,end=" ")
    print(number2,end=" ")
    for i in range(3,n+1):
        result=number1+number2  result=3  number1=2 number2=3
        number1=number2
        number2=result
        print(result,end=" ")
fibonacci(10)
