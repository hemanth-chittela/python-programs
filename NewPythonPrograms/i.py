string="abciief"
final_string=""

for i in string:
    if i=="i":
        final_string=final_string[::-1]
    else:
        final_string=final_string+i
print(final_string)