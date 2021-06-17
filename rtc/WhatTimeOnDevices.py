from subprocess import check_output
from smbus2 import *
import time

global Heure_Recuperee_RPI = None 
global Heure_Recuperee_RTC = None
def timenow_rpi():    
    try:
        out = str(check_output("date +%X", shell=True), 'UTF-8')
        heures_rpi = out[0:2]
        minutes_rpi = out[3:5]
        secondes_rpi = out[6:8]
        print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la Raspberry".format(heures_rpi,minutes_rpi,secondes_rpi))
        Heure_Recuperee_RPI = 0
        return heures_rpi, minutes_rpi, secondes_rpi, Heure_Recuperee_RPI
        
    except: 
        print(" Impossible de récupérer l'heure de la Raspberry ! ")
        Heure_Recuperee_RPI = 1
        return Heure_Recuperee_RPI

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

        secondes_RTC = hex(secondes_RTC)
        secondes_RTC = secondes_RTC[2:4]
        
        print("\n ----> Il est {0} heures, {1} minutes et {2} secondes sur la RTC \n".format(heures_RTC,minutes_RTC,secondes_RTC))
        Heure_Recuperee_RTC = 0
        return secondes_RTC,minutes_RTC,heures_RTC,Heure_Recuperee_RTC
        
    except: 
        print("\n ----> L'horloge semble disfonctionner ! \n Vérifier le branchement de l'horloge ! \n ")
        Heure_Recuperee_RTC = 1 
        return Heure_Recuperee_RTC



timenow_rpi()
timenow_RTC()

try: 
    secondes_rpi, minutes_rpi, heures_rpi, Heure_Recuperee_RPI = timenow_rpi()
    secondes_RTC, minutes_RTC, heures_RTC, Heure_Recuperee_RTC = timenow_RTC()

except:

    print("Doesn't Work ! ")
