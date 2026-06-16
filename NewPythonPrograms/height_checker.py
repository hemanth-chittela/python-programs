heights=[5,1,2,3,4]
counting=0
new_heights=sorted(heights)
for i in range(len(heights)):
    if heights[i]!=new_heights[i]:
        counting=counting+1
print(counting)