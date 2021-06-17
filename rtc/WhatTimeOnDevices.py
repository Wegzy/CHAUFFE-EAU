from subprocess import check_output
from smbus2 import read_i2c_block_data,write_i2c_block_data
import time

def timenow_rpi ():
    out = str(check_output("date +%X", shell=True), 'UTF-8')
    heures_rpi = out[0:2]
    minutes_rpi = out[3:5]
    secondes_rpi = out[6:8]
    print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la Raspberry".format(heures_rpi,minutes_rpi,secondes_rpi))
    return heures_rpi, minutes_rpi, secondes_rpi
timenow_rpi()

def timenow_RTC():
    SLAVE_ADDRESS = 0x51
    bus  = SMBus(1)
    CONTROL_1 = 0x00
    TimeOnRTC = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
    #print(val[2:5]) # Récupère uniquement les secondes, min, sec
    secondes_RTC = str(TimeOnRTC[2])
    minutes_RTC = str(TimeOnRTC[3])
    heures_RTC = str(TimeOnRTC[4])
    print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur l'horloge RTC".format(heures_RTC,minutes_RTC,secondes_RTC))

timenow_RTC()