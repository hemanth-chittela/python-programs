import requests
import re
count=0
result=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail=result.json()
for details in range (len(complete_detail)):
    count=count+1
    x=complete_detail[details]["user"]["login"]
    print(x)
print("number of users:",count)

result={}
for details in complete_detail:
    name=details["user"]["login"]
    if name in result:
        result[name]=result[name]+1
    else:
        result[name]=1
for name,count in result.items():
    print(f"{name}={count}")
    
max_contributor=max(result,key=result.get)
print(f"max contributor is {max_contributor} which is {result[max_contributor]}")
del result[max_contributor]
second_max=max(result,key=result.get)
print(f"second max is {second_max} which is {result[second_max]}")