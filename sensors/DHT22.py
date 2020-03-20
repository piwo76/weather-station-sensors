import time
import board
import adafruit_dht

class DHT22:
    def __init__(self):
        self.device = adafruit_dht.DHT22(board.D4)

    def read(self, delay_on_failure = 1):
        temperature_c = None
        humidity = None
        while not temperature_c or not humidity:
            try:
                # Print the values to the serial port
                temperature_c = self.device.temperature
                humidity = self.device.humidity
                if temperature_c > -50.0 and temperature_c < 80.0 and humidity > 0.0 and humidity < 100.0:
                    return (temperature_c, humidity)
                else:
                    temperature_c = None
                    humidity = None

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                temperature_c = None
                humidity = None
                time.sleep(delay_on_failure)
