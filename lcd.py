import time
from machine import I2C, Pin
from I2C_LCD import I2cLcd

takki = Pin(15, Pin.IN, Pin.PULL_UP)
i2c = I2C(scl=Pin(13), sda=Pin(14), freq=400000)
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    for device in devices:
        print("I2C addr: "+hex(device))
        lcd = I2cLcd(i2c, device, 2, 16)
try:
    lcd.move_to(0, 0)
    lcd.putstr("___") # breyta
    count = 0
    while True:
        lcd.move_to(0, 1)
        lcd.putstr("Score:%d" %(count))
        if not takki.value():
            count += 10
            time.sleep_ms(300)
except:
    pass
