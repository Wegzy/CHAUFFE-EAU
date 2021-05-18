from subprocess import check_output
import time

def timenow_rpi ():
    out = str(check_output("date +%X", shell=True), 'UTF-8')
    heures = out[0:2]
    minutes = out[3:5]
    secondes = out[6:8]
    print("\nIl est {0} heures, {1} minutes et {2} secondes".format(heures,minutes,secondes))


def datenow_rpi (): 
    out = str(check_output("date +%x", shell=True), 'UTF-8')
    Jour = out[0:2]
    Mois = out[3:5]
    Année = out[6:8]

    print("\nJour : {0}\nMois : {1} \nAnnée :{2}\n\n".format(Jour,Mois,Année))
    
timenow_rpi()
datenow_rpi()
