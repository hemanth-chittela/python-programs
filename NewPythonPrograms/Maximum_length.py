nums1=[0,0,0,0,1]
nums2=[1,0,0,0,0]
string1=""
string2=""
final=[]
for i in range(len(nums1)):
    S=str(nums1[i])
    string1=string1+S
for i in range(len(nums2)):
    X=str(nums2[i])
    string2=string2+X

for a in range(len(string1)):
    if string1[a:len(string1)+1] in string2:
        final.append(len(string1[a:len(string1)+1]))
    else:
        continue
