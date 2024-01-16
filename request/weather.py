import requests

resoponse = requests.get("https://weather.tsukumijima.net/api/forecast?city=400040")
print(resoponse.text)
j = resoponse.json()