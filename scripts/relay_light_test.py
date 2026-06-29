from machine import Pin
import time

relay = Pin(18, Pin.OUT)

while True:
    relay.value(1)
    print("LIGHT ON")
    time.sleep(5)

    relay.value(0)
    print("LIGHT OFF")
    time.sleep(5)

