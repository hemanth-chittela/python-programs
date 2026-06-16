import requests
import json
import re
result=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
data=result.json()
with open("new.json","w") as file:
    file.write(json.dumps(data,indent=3))