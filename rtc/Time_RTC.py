#!/usr/bin/python3.9
#coding: utf-8

from smbus2 import *
import time
from smbus2 import read_i2c_block_data

SLAVE_ADDRESS = 0x51
bus  = SMBus(1)

"""
    Adresse des registres
"""

SECONDS   = 0x03
MINUTES   = 0x04
HOURS     = 0x05
DAYS      = 0x06
WEEKDAYS  = 0x07
MONTHS    = 0x08
YEARS     = 0x09
CONTROL_1 = 0x00

val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    #print(val[2:5]) # Récupère uniquement les secondes, min, sec
rtc_sec = str(val[2])
rtc_min = str(val[3])
rtc_hours = str(val[4])
print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_hours,rtc_min,rtc_sec))

