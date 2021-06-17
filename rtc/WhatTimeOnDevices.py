from subprocess import check_output
from smbus2 import *
import time

def timenow_rpi():    
    try:

        out = str(check_output("date +%X", shell=True), 'UTF-8')
        heures_rpi = out[0:2]
        minutes_rpi = out[3:5]
        secondes_rpi = out[6:8]
        print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la Raspberry".format(heures_rpi,minutes_rpi,secondes_rpi))
        
        return secondes_rpi, minutes_rpi, heures_rpi
        
    except: 
        print(" Impossible de récupérer l'heure de la Raspberry ! ")
        
def timenow_RTC():
    SLAVE_ADDRESS = 0x51
    bus  = SMBus(1)
    CONTROL_1 = 0x00
    try:        
        TimeOnRTC = bus.read_i2c_block_data(SLAVE_ADDRESS, CONTROL_1, 9)
        #print(val[2:5]) # Récupère uniquement les secondes, min, sec
        #print(type(TimeOnRTC))
        #print(TimeOnRTC)

        secondes_RTC = str(TimeOnRTC[2])
        minutes_RTC  = str(TimeOnRTC[3])
        heures_RTC   = str(TimeOnRTC[4])    

        secondes_RTC = int(secondes_RTC)
        minutes_RTC  = int(minutes_RTC)
        heures_RTC   = int(heures_RTC)    

        print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la RTC \n".format(heures_RTC,minutes_RTC,secondes_RTC))
        
        return secondes_RTC,minutes_RTC,heures_RTC
        
    except: 
        print("\n ----> Impossible de communiquer avec la RTC ! \n Vérifier son branchement !  \n ")
        
try: 
    secondes_rpi, minutes_rpi, heures_rpi = timenow_rpi()
    secondes_RTC, minutes_RTC, heures_RTC = timenow_RTC()

    print(minutes_RTC, minutes_rpi, heures_RTC, heures_rpi)


    if heures_rpi==heures_RTC and minutes_rpi==minutes_RTC: 
        print("L'horloge RTC et la Raspberry sont synchronisés ! ")
    else:
        print("Les deux horloges ne sont pas synchronisés ! ")

except:

    print("L'heure n'a pas pu être comparé ")
