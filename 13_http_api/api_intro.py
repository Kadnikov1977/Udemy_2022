import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=1980-01-01&endtime=2022-01-15&latitude=51.21&longitude=51.37&maxradiuskm=250"

resp = requests.get(url, headers={"Accept":"aplication/json"})

data = resp.json()
for i in data['features']:
    print('магнитуда =', i['properties']['mag'], 'место = ', i['properties']['place'], sep="    ")
