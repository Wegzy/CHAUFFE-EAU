from subprocess import check_output
from smbus2 import *
import time

def timenow_rpi():
    out = str(check_output("date +%X", shell=True), 'UTF-8')
    heures_rpi = out[0:2]
    minutes_rpi = out[3:5]
    secondes_rpi = out[6:8]
    print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la Raspberry".format(heures_rpi,minutes_rpi,secondes_rpi))
    return heures_rpi, minutes_rpi, secondes_rpi
def timenow_RTC():
    SLAVE_ADDRESS = 0x51
    bus  = SMBus(1)
    SECONDS   = 0x03
    TimeOnRTC = bus.read_i2c_block_data(SLAVE_ADDRESS, SECONDS, 3)
    #print(val[2:5]) # Récupère uniquement les secondes, min, sec
    print(type(TimeOnRTC))
    print(TimeOnRTC)

    secondes_RTC = str(TimeOnRTC[0])
    minutes_RTC  = str(TimeOnRTC[1])
    heures_RTC   = str(TimeOnRTC[2])    
    
    #secondes_RTC = TimeOnRTC[6]



    print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la RTC \n".format(heures_RTC,minutes_RTC,secondes_RTC))

timenow_rpi()
timenow_RTC()