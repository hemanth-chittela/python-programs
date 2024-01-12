def factorial(a):
    result=1
    for i in range(1,a+1):
        result=result*i
    return result
result=factorial(5)
print(result)