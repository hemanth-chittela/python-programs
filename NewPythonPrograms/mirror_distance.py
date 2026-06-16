n=10
n=str(n)
s=n[::-1]
numbers=[]
numbers.append(int(n))
numbers.append(int(s))
resultant=max(numbers)-min(numbers)

print(resultant)
