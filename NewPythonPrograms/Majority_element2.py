nums=[1]
new_list={}
output=[]
for i in nums:
    if i in new_list:
        new_list[i]=new_list[i]+1
    else:
        new_list[i]=1
print(new_list)

Length=len(nums)
print("Length is",Length)
appear=Length/3
print("Appear is",int(appear))
for key,value in new_list.items():
    if value>appear:
        output.append(key)
    elif len(nums)==1:
        print(nums)
        break
print(output)