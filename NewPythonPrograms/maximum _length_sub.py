nums1=[0,0,0,0,1]
nums2=[1,0,0,0,0]
final=[]
x=0
for i in range(len(nums2)):
    for j in range(len(nums1)):
        if x==len(nums1):
            break
        elif nums1[j]!=nums2[i]:
            x=x+1
            continue
        elif nums1[j]==nums2[i]:
            final.append(nums1[j])
            i=i+1
            x=x+1
print(len(final))
            

