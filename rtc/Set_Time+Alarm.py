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
    
    secondes = hex(secondes,16)
    minutes  = hex(minutes ,16)
    heures   = hex(heures  ,16)

    secondes_alarm = int(secondes)+2

    print("L'heure va être reellement synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))

    bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_2, [0x02])
    bus.write_i2c_block_data(SLAVE_ADDRESS, SECONDS, [secondes,minutes,heures])
    val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    print(val[2:5]) # Récupère uniquement les secondes, min, sec
    rtc_sec = hex(val[2]) # Passage en hexa de la valeur
    rtc_min = hex(val[3])
    rtc_hours = hex(val[4])
    print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_hours[2:4],rtc_min[2:4],rtc_sec[2:4]))
    print(secondes_alarm) # Vérifier l'incrémentation de l'heure
    bus.write_i2c_block_data(SLAVE_ADDRESS, SECOND_ALARM, [secondes_alarm, minutes, heures, 0x80, 0x80])
    
    time.sleep(4)
    bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_2, [0x00])


Set_time_RTC()

