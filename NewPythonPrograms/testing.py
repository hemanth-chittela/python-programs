ranges = [(33, 47), (58, 64), (91, 96), (123, 126)]

for start, end in ranges:
    for i in range(start, end + 1):
        print(i, chr(i))
        