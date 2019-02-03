import requests
url = "https://icanhazdadjoke.com/"


response = requests.get(url, headers={"Accept":"application/jason"})
print(response.text)
print(response.json())