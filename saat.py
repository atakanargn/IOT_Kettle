import ntptime
from machine import RTC
import utime

utc_timezone = 3

ntptime.settime()

def gettime():
    try:
        saat = utime.localtime(utime.mktime(utime.localtime()) + utc_shift*3600)
        saat = saat[0:3] + (0,) + saat[3:6] + (0,)
        return saat
    except:
        return -1