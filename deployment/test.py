import requests

url = 'http://localhost:9696/predict'

sample = {}

response = requests.post(url, json=sample).json()

print(response.json())


