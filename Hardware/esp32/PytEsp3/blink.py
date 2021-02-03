from machine import I2C, Pin 
reset = Pin(16, Pin.OUT, value=1)
scl_pin = Pin(15, Pin.IN, Pin.PULL_UP)
sda_pin = Pin(4, Pin.IN, Pin.PULL_UP)
i2c = I2C(scl=scl_pin, sda=sda_pin, freq=400000)
i2c.scan()
import ssd1306
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.text("     NOT      ", 0, 0)
oled.text("    A VERY    ", 0, 16)
oled.text("   EXCITING   ", 0, 32)
oled.text("    SCREEN    ", 0, 48) 
oled.show()