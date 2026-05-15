from machine import Pin
import time
import dht
from grove_lcd import setText

sensor = dht.DHT11(Pin(16))

last_temp = "--"
last_hum = "--"

last_serial_send = 0

SERIAL_INTERVAL = 600
LCD_INTERVAL = 30

while True:

    try:
        sensor.measure()

        temperature = sensor.temperature()
        humidity = sensor.humidity()

        last_temp = temperature
        last_hum = humidity

        current_time = time.time()

        # enviar serial apenas de 10 em 10 minutos
        if current_time - last_serial_send >= SERIAL_INTERVAL:

            print("{},{}".format(
                temperature,
                humidity
            ))

            last_serial_send = current_time

    except Exception:
        pass

    # atualizar LCD sempre
    setText(
        "Temp: {} C\nHum: {} %".format(
            last_temp,
            last_hum
        )
    )

    time.sleep(LCD_INTERVAL)
