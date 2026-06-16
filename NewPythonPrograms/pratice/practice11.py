import requests
url=requests.get("https://reqres.in/api/users?page=2")
output=url.json()
list=[]
x=output['page'],output['per_page'],output['total'],output['total_pages']
list.append(x)
print(list)