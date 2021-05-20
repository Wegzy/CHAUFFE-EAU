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
    
    secondes = hex(int(secondes,16))
    minutes  = hex(int(minutes,16))
    heures   = hex(int(heures,16))

    

    print("L'heure va être reellement synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))


    

Set_time_RTC()

