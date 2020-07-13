# https://earthquake.usgs.gov/fdsnws/event/1/

import requests
import sqlite3


def save_earthquakes(earthquakes_list):
    connect = sqlite3.connect('earthquakes.db')
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", earthquakes_list)
    connect.commit()
    connect.close()


def select_earthquakes():
    connect = sqlite3.connect('earthquakes.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    data = cursor.fetchall()
    [print(row) for row in data]
    connect.commit()
    connect.close()


def get_earthquake():
    starttime = input('Enter the start time (YYYY-MM-DD): ')
    endtime = input('Enter the end time (YYYY-MM-DD): ')
    latitude = input('Enter the latitude (-90..90): ')
    longitude = input('Enter the longitude (-180..180): ')
    maxradiuskm = input('Enter the max radius in km (0..20000): ')
    minmagnitude = input('Enter the min magnitude: (0..10): ')
    method = 'query'
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/{method}?'

    response = requests.get(url,
                            headers={
                                'Accept': 'application/json'
                            },
                            params={
                                'format': 'geojson',
                                'limit': '1000',
                                'starttime': starttime,  # default: NOW - 30 days
                                'endtime': endtime,  # default: present time
                                'latitude': latitude,  # default: null
                                'longitude': longitude,  # default: null
                                'maxradiuskm': maxradiuskm,  # default: 20001.6
                                'minmagnitude': minmagnitude  # default: null
                            })
    data = response.json()
    earthquakes_list = []

    for i in data['features']:
        print(i['properties']['time'])
        earthquakes_list.append((i['properties']['place'], i['properties']['mag']))
    return earthquakes_list
