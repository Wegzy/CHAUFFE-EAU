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
CONTROL_2 = 0x01

SECOND_ALARM  = 0x0A
MINUTE_ALARM  = 0x0B
HOUR_ALARM    = 0x0C
DAY_ALARM     = 0x0D
WEEKDAY_ALARM = 0x0E

def Set_time_RTC():

    heures   = input("Heures : ")
    minutes  = input("Minutes : ")
    secondes = input("Secondes : ")    

    print("L'heure va être synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))
             
    secondes = int(secondes) 
    minutes  = int(minutes)
    heures   = int(heures)
    secondes_alarm = secondes+2
       
    bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_2, [0x02])
    bus.write_i2c_block_data(SLAVE_ADDRESS, SECONDS, [secondes,minutes,heures])
    
    val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    print(val[2:5]) # Récupère uniquement les secondes, min, sec
    rtc_sec = str(val[2])
    rtc_min = str(val[3])
    rtc_hours = str(val[4])
    print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_hours,rtc_min,rtc_sec))

    bus.write_i2c_block_data(SLAVE_ADDRESS, SECOND_ALARM, [secondes_alarm, minutes, heures, 0x80, 0x80])
    
    time.sleep(4)
    bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_2, [0x00])


Set_time_RTC()

