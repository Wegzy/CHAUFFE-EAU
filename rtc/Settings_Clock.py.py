#!/usr/bin/python3.9
#coding: utf-8

def Set_time():
    heures   = input("Heures : ")
    minutes  = input("Minutes : ")
    secondes = input("Secondes : ")
    return [heures,minutes,secondes]

heures,minutes,secondes = Set_time()

print("L'heure va être synchronisé sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))

