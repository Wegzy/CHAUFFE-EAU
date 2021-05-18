from subprocess import check_output


def check_sync():
    """
     La fonction récupère la valeur obtenu par "timedatectl", c'est une commande "linux"
     Cette valeur est convertis au format string (puisqu'elle est au départ en bytes). 
     Et enfin on récupère l'information : Yes / No pour pouvoir l'utiliser dans une condition.
    """
    out = str(check_output("timedatectl | grep clock", shell=True), 'UTF-8')
    out = out[27:30]
    if out == "yes" :
        check_network()

    elif out == "no" : 
        print("L'horloge n'est pas synchronisé")

def check_network():
    """ 
     Fonction "ping" 
     Si la valeur retourné = 0, la connexion est fonctionnel, l'horloge sync
    """

    ip = "8.8.8.8"
    rep = check_output("ping -c 2 " + ip + " > /dev/null", shell=True)
    if rep == 0:
        print("No Network")
        
    else: 
        print("Network OK")
    
check_sync() 






