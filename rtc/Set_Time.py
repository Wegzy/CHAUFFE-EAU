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

        secondes = int(input("Secondes : "))
        if (secondes<0) or (secondes>60):
            print("Merci de rentrer une seconde entre 0 et 60")
            secondes=int('erreur')
            
        print("L'heure va être synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))
        bus.write_i2c_block_data(SLAVE_ADDRESS, SECONDS, [secondes,minutes,heures])
        val = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
        #print(val[2:5]) # Récupère uniquement les secondes, min, sec
        rtc_sec   = str(val[2])
        rtc_min   = str(val[3])
        rtc_hours = str(val[4])
        print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_hours,rtc_min,rtc_sec))
    except:
        print("Saisie Incorrecte, il faut entrer des nombres ! ")
        Set_time_RTC()

    

Set_time_RTC()