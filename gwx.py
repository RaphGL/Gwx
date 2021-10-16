import requests
from bs4 import BeautifulSoup

def get_weather_info() -> dict:
    r = requests.get('https://www.bbc.com/weather/1850147')

    weather_info = {
        'today': {
            'min_weather': None,
            'max_weather': None,
            'weather_description': None
        },
        'location': None,
    }

    if r.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        # get today's weather
        temps = soup.select('a#daylink-0 div.wr-day__temperature span span.wr-value--temperature--c')
        try: 
            weather_info['today']['max_weather'] = temps[0].text
            weather_info['today']['min_weather'] = temps[1].text
        except IndexError:
            pass

        # get today's weather description
        temps = soup.select('a#daylink-0 div.wr-day__weather-type-description-container div.wr-day__weather-type-description')
        weather_info['today']['weather_description'] = temps[0].text

        # get weather location name
        location = soup.select('h1#wr-location-name-id')[0]
        location.span.extract()
        weather_info['location'] = location.text

    # returns a dictionary with all the weather info gathered
    return weather_info

if __name__ == '__main__':
    print(get_weather_info())