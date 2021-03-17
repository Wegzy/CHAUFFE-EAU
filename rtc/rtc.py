#!/usr/bin/python3
#coding: utf-8

"""
    Librairie
"""

import smbus
import time

"""
    Adresse de l'esclave   
"""

SLAVE_ADDRESS = 0x51

"""
    Adresse des registres
"""

# CONTROL_1 permet de configurer des paramètres tel que : "External Clock test mode"
#                                                         "RC source Clock runs"
#                                                         "12/24 hours mode"
# DOC Page 10
# ===============
# CONTROL_3 permet de configurer des paramètres concernant la batterie
#
# DOC Page 11
# ===============
# CLKOUT_CONTROL_REGISTER : HZ
# 
# 
# Doc Page 14
# 
# 
# 
# 



CONTROL_1 = 0x00
#CONTROL_2 = 0x01
CONTROL_3 = 0x02
SECONDS   = 0x03
MINUTES   = 0x04
HOURS     = 0x05
DAYS      = 0x06
WEEKDAYS  = 0x07
MONTHS    = 0x08
YEARS     = 0x09

SECOND_ALARM  = 0x0A
MINUTE_ALARM  = 0x0B
HOUR_ALARM    = 0x0C
DAY_ALARM     = 0x0D
WEEKDAY_ALARM = 0x0E

CLKOUT_CONTROL_REGISTER = 0x0F
WATCHDOG_TIME_CONTROL   = 0x10
WATCHDOG_TIME_VAL       = 0x11
TIMESTAMP REGISTER      = 0x12