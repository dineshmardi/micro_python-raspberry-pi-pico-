# from machine import Pin, I2C

# i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# devices= i2c.scan()
# i2caddr=devices[0]
# # print(hex(i2caddr))# return addres of periferal

# lcd=I2cLcd(i2c, i2caddr, 2, 16)


from machine import Pin, I2C, Timer
from pico_i2c_lcd import I2cLcd
import utime
import random

sda=Pin(0)
scl=Pin(1)

i2c=I2C(0, sda=sda, scl=scl, freq=400000)
devices=i2c.scan()
i2caddr=devices[0]
print(hex(i2caddr))
lcd=I2cLcd(i2c, i2caddr, 2, 16)



# i2cd=I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
# lcd1=I2cLcd(i2cd, i2caddr, 2, 16)

msg="DINESH MARDI......"
i=1
# while i<=12:
#   lcd.putstr(str(i))
#   utime.sleep(1)
#   lcd.clear()
#   i=i+1

#-------------------------------------------
# def numberss(timer):
#   global i
#   lcd.putstr(str(i))
#   utime.sleep(1)
#   lcd.clear()
#   i=i+1

# timer=Timer(freq=1, mode=Timer.PERIODIC, callback=numberss)

# lcd.putstr("GOOD JOB---")

#------------------------------------------------------

#to print random numbers in the screen.....

# def random_numbers(timer):
#   a=random.randint(1,6)
#   # lcd.backlight_on()
#   lcd.putstr(str(a))
#   utime.sleep(1)
#   lcd.clear()

#----------------------------

def fn(timer):
  global msg
  lcd.putstr(msg)
  msg=msg[-1]+msg[:-1]
  
timer=Timer(freq=1, mode=Timer.PERIODIC, callback=fn)


#code in wokwi simulator---https://wokwi.com/projects/421941636858957825

