#!/usr/bin/python3.9
#coding: utf-8


from smbus2 import *
import time

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


bus.write_i2c_block_data(SLAVE_ADDRESS, SECONDS, [0x00,0x30,0x15])

def Set_time():
    heures   = input("Heures : ")
    minutes  = input("Minutes : ")
    secondes = input("Secondes : ")
    return [heures,minutes,secondes]


def Set_time_RTC():
    
    heures,minutes,secondes = Set_time()

    print("L'heure va être synchronisé sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))


Set_time_RTC()

while True: 
	print(bus.read_i2c_block_data(SLAVE_ADDRESS, SECONDS, 3))
	time.sleep(2)