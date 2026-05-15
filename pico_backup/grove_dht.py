from machine import Pin
import dht

class DHT:
    def __init__(self, pin):
        self.sensor = dht.DHT11(Pin(pin))

    def read_temp_hum(self):
        self.sensor.measure()
        temp = self.sensor.temperature()
        hum = self.sensor.humidity()
        return temp, hum

