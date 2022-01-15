import requests

url = 'https://www.google.ru/'
resp = requests.get(url)
print(f"Request to {url}. Status code is {resp.status_code} ")

print(resp.text)
