import requests
import sys

city = str(sys.argv[1])
url = f"http://api.openweathermap.org/data/2.5/weather"
params = {
    'q' : city,
    'appid' : '252c27f2e1719ba2bc6b2d8cb403ce89',
    'lang' : 'ru',
    'units' : 'metric'
}
data = requests.get(url, params=params).json()

template = 'Текущая темпреатура в городе {} составляет {} градуса Цельсия'
print(template.format(city.upper(), data['main']['temp']))