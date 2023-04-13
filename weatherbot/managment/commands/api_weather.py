import requests


def get_weather(city):
    cord = city.split(';')


    KEY = '137d62f3c460fac41edca5930e84af7c'

    parameters = {
        'appid': KEY,
        'units': 'metric',
        'lang': 'ru',
        'lat': cord[0],
        'lon': cord[1],
    }
    try:
        data = requests.get(params=parameters, url=f'https://api.openweathermap.org/data/2.5/weather').json()
        temp = data['main']['temp']
        clouds = data['clouds']['all']
        humidity =data['main']['humidity']
        wind = data['wind']['speed']
        send = f'''
    Температура - <b>{temp}°C</b>
    Влажность - <b>{humidity}%</b>
    Скорость ветра - <b>{wind} м/с</b>
    Облочность - <b>{clouds}%</b>'''

        return send.strip()
    except Exception as e:
        print(e)
        send_ex = f'На запрос <b>{city}</b> ничеги не найдено'
        return send_ex
