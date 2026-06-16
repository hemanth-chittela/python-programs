#important thing we need to convert to json and then only we can start fetching lol
import requests
import json
response=requests.get("https://api.thecatapi.com/v1/images/search")
json_output=json.dumps(response.json(),indent=2)
print(json_output)
print(response.text)
print(type(response))
if response.status_code==200:
    result=response.json()
    print(result[0]['url'])
    if result[0]['width']>600:
        print("it is not")
    else:
        print("it is")