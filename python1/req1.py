import requests
import re
count=0
result=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail=result.json()
for list in complete_detail:
    output=list["user"]["login"]
    count=count+1
    print(output)
print("number: ",count)
listing={}
for list1 in complete_detail:
    names=list1["user"]["login"]
    if names in listing:
        listing[names]=listing[names]+1
    else:
        listing[names]=1
for names,count in listing.items():
    print(f"{names}={count}")
print(" ")
maximum_contributor=max(listing,key=listing.get)
print("maximum contributor is",maximum_contributor,"which is",listing[maximum_contributor])
del listing[maximum_contributor]
second_max=max(listing,key=listing.get)
print("second maximum contributor is",second_max,"which is",listing[second_max])
del listing[second_max]
third_max=max(listing,key=listing.get)
print("third maximum contributor is",third_max,"which is",listing[third_max])