import csv
import os
import time
from datetime import datetime
import serial

SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 115200
LOG_DIR = "/home/zerocool/My-co-Lab/data/environment"

os.makedirs(LOG_DIR, exist_ok=True)

while True:
    try:
        with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=10) as pico:
            while True:
                line = pico.readline().decode("utf-8").strip()

                if not line or "ERROR" in line:
                    continue

                try:
                    temperature, humidity = line.split(",")
                except ValueError:
                    continue

                now = datetime.now()
                filename = now.strftime("%Y-%m-%d_environment.csv")
                filepath = os.path.join(LOG_DIR, filename)
                file_exists = os.path.exists(filepath)

                with open(filepath, "a", newline="") as file:
                    writer = csv.writer(file)

                    if not file_exists:
                        writer.writerow([
                            "datetime",
                            "temperature_c",
                            "humidity_percent"
                        ])

                    writer.writerow([
                        now.strftime("%Y-%m-%d %H:%M:%S"),
                        temperature,
                        humidity
                    ])

                print(now.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity)

    except Exception as e:
        print("Logger error:", e)
        time.sleep(5)

