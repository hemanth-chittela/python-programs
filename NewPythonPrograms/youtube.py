import requests
import json

url2="https://timeskip.io/api/tools/youtube-dislikes"

payload = {
    "url": "https://www.youtube.com/watch?v=JZvCmAgRWI0&t=128s"
    }

payload2= {
    "url":"https://www.youtube.com/watch?v=IjDDrAwxlIE"
}
headers1 = {
    "Content-Type": "application/json"
}

output=requests.post(url=url2,json=payload2,headers=headers1)
k=json.dumps(output.json(),indent=2)
print(k)
print(type(k))
dict_value=output.json()
print(type(dict_value))
print("The dislikes for the video is:",dict_value["dislikes"])
print("The likes for the video is:",dict_value["likes"])