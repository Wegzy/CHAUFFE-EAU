

heures = input()
minutes = input()
secondes = input()

heures = int(heures)
minutes = int(minutes)
secondes = int(secondes)

print("L'heure va être synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))

heures_bin  = bin(heures)
minutes_bin = bin(minutes)
secondes_bin = bin(secondes)

print("L'heure  en binaire : {0} pour l'heure, {1} Minutes, {2} Secondes".format(heures_bin,minutes_bin,secondes_bin))


