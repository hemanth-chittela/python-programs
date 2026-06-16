arr=[1,0,2,3,0,4,5,0]
final=[]
for i in range(len(arr)):
    if len(final)==len(arr):
        break
    elif arr[i]==0:
        final.append(0)
        final.append(0)
    else:
        final.append(arr[i])
arr=final
print(arr)