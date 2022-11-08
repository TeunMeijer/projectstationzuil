import requests


r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=den haag,nl&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
response_data = r.json()

for key in response_data.keys():
    print(f"{key}: {response_data[key]}")

r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=haarlem&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
response_data = r.json()

for key in response_data.keys():
    print(f"{key}: {response_data[key]}")


r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=zaandam&appid=5d6cab63d757ea8d87737b1f23d0de49&units=metric")
response_data = r.json()

for key in response_data.keys():
    print(f"{key}: {response_data[key]}")