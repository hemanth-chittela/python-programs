x=int(input("enter the first value"))
y=int(input("enter the second value"))
print("Before swapping")
print(f"the first value is {x}")
print(f"the second value is {y}")
x=x+y
y=x-y
x=x-y
print("after swapping")
print(f"the first value is {x}")
print(f"the second value is {y}")
