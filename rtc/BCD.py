"""def bcdToDEC_test():
    a = int(input("Insérer une valeur en Décimal :"))
    print(a)
    print(type(a))
    
    a = bin(a)
    print(a)
    print(type(a))


#bcdToDEC_test()
"""
"""
def bcdToDEC():

    try: 
        heures = int(input("Heures : "))
        if ((heures<0) or (heures>24)):
            print("Merci de rentrer une heure entre 0 et 24")
            heures=int('erreur')
        
        heures = bin(heures)
        print(heures)
        
        minutes = int(input("Minutes : "))
        if (minutes<0) or (minutes>60) :
            print("Merci de rentrer une minute entre 0 et 60")
            minutes=int('erreur')
        
        minutes = bin(minutes)
        print(minutes)
        
        secondes = int(00)
        secondes = bin(secondes)
        print(secondes)
    except:
        print("Problème")
        bcdToDEC()

bcdToDEC()"""

def convert_reception():

    try: 
        heures = bin(0b1010)
        minutes = bin(0b00100000)
        secondes = bin(0b0110101)

        print(heures, minutes, secondes)
        
        heures = int(heures,2)
        minutes = int(minutes,2)
        secondes = int(secondes,2)

        print(heures, minutes, secondes)

        
        
        
    except:
        print("test")



convert_reception()


