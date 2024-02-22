import requests

url = "https://restcountries.com/v3.1/all"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()

