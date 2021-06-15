#!/usr/bin/python3.9
#coding: utf-8

"""
    Librairie
"""

from smbus2 import *
import time

"""
    Adresse de l'esclave   
"""

SLAVE_ADDRESS = 0x51

"""
    Adresse des registres
"""
CONTROL_1 = 0x00
CONTROL_2 = 0x01
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
TIMESTAMP_REGISTER      = 0x12

"""
    Paramètres du bus
"""

bus  = SMBus(1)

data = [0x00, 0x02, 0xE0, 0x00, 0x30, 0x11]
######## R1 , R2 , R3    , sec , h , min ####

""" CLOCK SPEED """
clkout32 =  0b11000000
clkout1 = 0b11000110
clkout1024 = 0b11000101
""" ########### """

bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, data)
bus.write_i2c_block_data(SLAVE_ADDRESS, SECOND_ALARM, [0x02])
bus.write_i2c_block_data(SLAVE_ADDRESS, MINUTE_ALARM, [0x30])
bus.write_i2c_block_data(SLAVE_ADDRESS, HOUR_ALARM, [0x11])
bus.write_i2c_block_data(SLAVE_ADDRESS, DAY_ALARM, [0x80])
bus.write_i2c_block_data(SLAVE_ADDRESS, WEEKDAY_ALARM, [0x80])

while True: 
	print(bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9))
	time.sleep(2)










