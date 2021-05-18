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
