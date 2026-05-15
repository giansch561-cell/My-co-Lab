from machine import I2C, Pin
from time import sleep_ms

LCD_ADDRESS = 0x3e

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)

def lcd_command(cmd):
    i2c.writeto(LCD_ADDRESS, bytes([0x80, cmd]))
    sleep_ms(5)

def lcd_write(data):
    i2c.writeto(LCD_ADDRESS, bytes([0x40, data]))
    sleep_ms(1)

def clear():
    lcd_command(0x01)
    sleep_ms(5)

def init():
    sleep_ms(100)
    lcd_command(0x38)
    sleep_ms(5)
    lcd_command(0x39)
    sleep_ms(5)
    lcd_command(0x14)
    lcd_command(0x70)
    lcd_command(0x56)
    lcd_command(0x6C)
    sleep_ms(200)
    lcd_command(0x38)
    lcd_command(0x0C)
    clear()

def setText(text):
    init()
    for char in text:
        if char == "\n":
            lcd_command(0xC0)
        else:
            lcd_write(ord(char))
