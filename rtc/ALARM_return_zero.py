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
SECONDS   = 0x03
MINUTES   = 0x04
HOURS     = 0x05

SECOND_ALARM  = 0x0A
MINUTE_ALARM  = 0x0B
HOUR_ALARM    = 0x0C
DAY_ALARM     = 0x0D
WEEKDAY_ALARM = 0x0E

"""
    Paramètres du bus
"""

bus  = SMBus(1)

data = [0x00, 0x02, 0xE0, 0x00, 0x00, 0x00]
######## R1 ,  R2 ,  R3 , sec ,  h  , min ####

bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, data)
bus.write_i2c_block_data(SLAVE_ADDRESS, SECOND_ALARM, [0x01])
bus.write_i2c_block_data(SLAVE_ADDRESS, MINUTE_ALARM, [0x00])
bus.write_i2c_block_data(SLAVE_ADDRESS, HOUR_ALARM, [0x00])
bus.write_i2c_block_data(SLAVE_ADDRESS, DAY_ALARM, [0x80])
bus.write_i2c_block_data(SLAVE_ADDRESS, WEEKDAY_ALARM, [0x80])

time.sleep(2)
bus.write_i2c_block_data(SLAVE_ADDRESS, CONTROL_2, [0x00])


#while True: 
#	print(bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9))
#	time.sleep(2)

