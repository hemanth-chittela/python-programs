import psutil
import os
result=[]
for i in range(5):
    value=psutil.cpu_percent(10)
    print(f"the cpu utilisation at the moment",value)
    if value>1:
        print("hot")
    else:
        print("cool")
    result.append(value)
print(result)
print("max utilisation is",max(result))