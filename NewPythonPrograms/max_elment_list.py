#To find the maximum element in a list and minimum elements in a list
list1=[0,34,21,-23,2,456,2,4224,312446,2235,2244556]
max_element=list1[0]
for i in range(len(list1)):
        if max_element<=list1[i]:
            max_element=list1[i]
print(max_element)
print(list1)

minimum_element=list1[0]
for i in range(len(list1)):
        if minimum_element>=list1[i]:
            minimum_element=list1[i]
print(minimum_element)
print(list1)

      