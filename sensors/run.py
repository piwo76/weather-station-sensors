import time

import requests

from sensors.DHT22 import DHT22


class Reader:
    def __init__(self, delay = 10, url='http://192.168.1.112:8081/'):
        self.DHT22 = DHT22()
        self.delay = delay
        self.url = url
        self.dht22URL = self.url + 'sensors/dht22/'

    def run(self):
        while True:
            (temperature, humidity) = self.DHT22.read()
            print("Temp: {:.1f} C    Humidity: {}% ".format(temperature, humidity))
            dht22_data = {'temperature': temperature, 'humidity': humidity}
            response = requests.post(self.dht22URL, data=dht22_data)
            if not response.ok:
                print('ERROR: Could not send the DHT22 data')

            time.sleep(10.0)

def run():
    Reader().run()



