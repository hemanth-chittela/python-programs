x = int(input("Enter the number of values you want to add: "))
t=[]
for i in range(x):
    value = int(input("Enter the number: "))
    t.append(value)
print(t)
print(t[1])  # Print the entered value on the same line with a space
print(t[::-1])
print(t[-1])

  # Print a new line after all values are printed
