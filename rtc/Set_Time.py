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
CONTROL_1 = 0x00

def Set_time():
    heures   = input("Heures : ")
    minutes  = input("Minutes : ")
    secondes = input("Secondes : ")
    return [heures,minutes,secondes]


def Set_time_RTC():
    hex_form = str("0x") # Variable à ajouter aux heures pour correspondre au format : 0xY (Y = H/Min/SEC)
    heures,minutes,secondes = Set_time()
    print("L'heure va être synchronisé sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))
    
    #heures = int("0x31",16)
    heures = int(hex_form+str(heures),16)
    minutes= int(hex_form+str(minutes),16) 
    secondes= int(hex_form+str(secondes),16)
    bus.write_i2c_block_data(SLAVE_ADDRESS, SECONDS, [heures,minutes,secondes])

    val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    print(val[2:5]) # Récupère uniquement les secondes, min, sec
    rtc_sec = hex(val[2])
    rtc_min = hex(val[3])
    rtc_hours = hex(val[4])
    print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_sec[2:4],rtc_min[2:4],rtc_hours[2:4]))


Set_time_RTC()

#while True: 
	#print(bus.read_i2c_block_data(SLAVE_ADDRESS, SECONDS, 3))
    #val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    #print(val[2:5]) # Récupère uniquement les secondes, min, sec
    #rtc_sec = hex(val[2])
    #rtc_min = hex(val[3])
    #rtc_hours = hex(val[4])
    #print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_sec[2:4],rtc_min[2:4],rtc_hours[2:4]))
    #time.sleep(1)

