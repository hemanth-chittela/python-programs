new_list = ['.', 'a', '.', '.', '.']
special_characters = ['.']

for j in range(len(new_list)):        # outer loop
    for j in new_list:                # inner loop
        if j in special_characters:
            new_list.remove(j)

print("Removed:", j, "Now:", new_list)
