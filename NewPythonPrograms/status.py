import requests

url="https://github.com"
response=requests.get(url)
status_code=response.status_code
print(f"status code for the url: {url} is {status_code}")
