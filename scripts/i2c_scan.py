from machine import Pin, I2C

tests = [
    ("I2C0 GP20/GP21", 0, 20, 21),
    ("I2C1 GP6/GP7", 1, 6, 7),
    ("I2C0 GP4/GP5", 0, 4, 5),
    ("I2C1 GP26/GP27", 1, 26, 27),
]

for name, bus, sda, scl in tests:
    try:
        i2c = I2C(bus, sda=Pin(sda), scl=Pin(scl), freq=100000)
        print(name, "->", i2c.scan())
    except Exception as e:
        print(name, "ERROR", e)
