DHT11 -> GP16
LCD -> I2C GP6/GP7
Relay -> GP15
Pico -> USB -> Raspberry Pix
# My-co-Lab Wiring

DHT11 Sensor -> GP16
LCD Grove -> I2C GP6 / GP7
Relay -> GP15
Raspberry Pi Pico -> USB -> Raspberry Pi 4

Data flow:
Sensor -> Pico -> Serial -> Raspberry -> CSV -> USB -> GitHub
