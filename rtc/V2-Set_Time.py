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

def Set_time_RTC():
    try:
        heures = int(input("Heures : "))
        if ((heures<0) or (heures>24)):
            print("Merci de rentrer une heure entre 0 et 24")
            heures=int('erreur')
              

        minutes = int(input("Minutes : "))
        if (minutes<0) or (minutes>60) :
            print("Merci de rentrer une minute entre 0 et 60")
            minutes=int('erreur')

        secondes = int(00)
            
        print("L'heure va être synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))

        heures = bin(heures)
        minutes = bin(minutes)
        secondes = bin(secondes)
        
        bus.write_byte_data(SLAVE_ADDRESS, SECONDS, [secondes,minutes,heures])
        #val = bus.read_byte_data(SLAVE_ADDRESS, SECONDS)
        print(val)
    except:
        print("Test")
Set_time_RTC()