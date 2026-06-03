from machine import Pin
import time
import dht
from grove_lcd import setText
import sys
import select

sensor = dht.DHT11(Pin(16))

last_temp = "--"
last_hum = "--"

last_serial_send = 0

SERIAL_INTERVAL = 600
LCD_INTERVAL = 1

usb_mode = False

while True:
    try:
        if select.select([sys.stdin], [], [], 0)[0]:
            msg = sys.stdin.readline().strip()

            if msg.startswith("LCD:"):
                lcd_text = msg.replace("LCD:", "")
                setText(lcd_text)

                if (
                    "USB" in lcd_text
                    or "BACKUP" in lcd_text
                    or "COPYING" in lcd_text
                    or "SAFE TO REMOVE" in lcd_text
                ):
                    usb_mode = True

            elif msg == "LCD_RESET":
                usb_mode = False

    except Exception:
        pass

    if not usb_mode:
        try:
            sensor.measure()

            temperature = sensor.temperature()
            humidity = sensor.humidity()

            last_temp = temperature
            last_hum = humidity

            current_time = time.time()

            if current_time - last_serial_send >= SERIAL_INTERVAL:
                print("{},{}".format(temperature, humidity))
                last_serial_send = current_time

        except Exception:
            pass

        setText(
            "Temp: {} C\nHum: {} %".format(
                last_temp,
                last_hum
            )
        )

    time.sleep(LCD_INTERVAL)