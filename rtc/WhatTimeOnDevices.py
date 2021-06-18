from subprocess import check_output,CalledProcessError
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
def check_sync():

    out = str(check_output("timedatectl | grep clock", shell=True), 'UTF-8')
    out = out[27:30]
    
    statut = None
    

    if out == "yes":
        ip = "1.debian.pool.ntp.org"
        try:
            check_output("ping -c 2 " + ip, shell=True)
            print("\n\n Statut 0 : L'horloge est synchronisé \n\n\n")
            statut = 0
            return statut
    
        except CalledProcessError: 
            print("\n\n Statut 1 : L'horloge n'est plus synchronisé à internet \n\n\n")
            statut = 1
            return statut
            
    else:
        print("\n\n Statut 2 : L'horloge n'est plus du tout synchronisé \n\n\n")
        statut = 2
        return statut

try: 
    secondes_rpi, minutes_rpi, heures_rpi = timenow_rpi()
    secondes_RTC, minutes_RTC, heures_RTC = timenow_RTC()

    if int(heures_RTC)==int(heures_rpi) and int(minutes_RTC)==int(minutes_rpi): 
        print("L'horloge RTC et la Raspberry sont synchronisés ! ")

    else:
        print("Les deux horloges ne sont pas synchronisés ! \n\n\n\n\n ")
        print("Vérification du statut de synchronisation de la Raspberry  :")
        try: 
            statut = check_sync() 
            if statut == 1:
                print("Synchronisation de la RTC en cours ...")