# This file is executed on every boot (including wake-boot from deepsleep)

#import esp
#esp.osdebug(None)

import gc
import webrepl

from machine import I2C,reset_cause

#### Mes modules ####
from utils.m_wifico import *
from utils.m_pinout import pinout
from utils.m_adxl345 import ADXL345

#### Programme ####
webrepl.start()
gc.collect()

i2c = I2C(scl=Pin(0),sda=Pin(2), freq=10000)
adx = ADXL345(i2c)
wifiConnect(20) # Lors d'un soft reboot, ne sera pas executé
