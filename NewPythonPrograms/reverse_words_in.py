string="Let's take LeetCode contest"
new_string=[]
string=list(string.split(" "))
for i in range(len(string)):
    new_string.append(string[i][::-1])

new_string=" ".join(new_string)
print(new_string)