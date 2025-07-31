import requests , pprint

# url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
url = "https://catfact.ninja/fact"

response = requests.get(url, timeout=10);
response.raise_for_status()
weather = response.json()
pprint.pp(weather)