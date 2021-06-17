#!/usr/bin/python3.9
#coding: utf-8

from subprocess import check_output,CalledProcessError

def check_sync():

    out = str(check_output("timedatectl | grep clock", shell=True), 'UTF-8')
    out = out[27:30]
    
    statut = None
    print(statut)

    if out == "yes":
        ip = "1.debian.pool.ntp.org"
        try:
            check_output("ping -c 2 " + ip, shell=True)
            print("\n\n Statut 0 : L'horloge est synchronisé \n\n\n")
            statut = 0
            print(statut)
        except CalledProcessError: 
            print("\n\n Statut 1 : L'horloge n'est plus synchronisé à internet \n\n\n")
            statut = 1
            print(statut)
    else:
        print("\n\n Statut 2 : L'horloge n'est plus du tout synchronisé \n\n\n")
        statut = 2
        print(statut)
check_sync()    
