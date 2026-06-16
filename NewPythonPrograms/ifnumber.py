name=str(input("Enter the string: "))
contains_digit=False
for char in name:
    if char.isdigit():
        contains_digit=True
        break
if contains_digit:
    print("Yes contains digit")
else:
    print("No, Doesn't contain a digit")