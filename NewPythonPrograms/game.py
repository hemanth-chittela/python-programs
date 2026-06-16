position = 0
string = input("Enter the string: ")

for char in string:
    if char == 'R':
        position += 1
    elif char == 'J':
        position += 2
    elif char == 'L':
        position -= 1

    if position > 10:
        print("Position:", position)
        print("False")
        break

if position == 10:
    print("Position:", position)
    print("True")

elif position < 10:
    print("Position:", position)
    print("False")
