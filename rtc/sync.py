from subprocess import check_output,CalledProcessError

def check_sync():
    """
     La fonction récupère la valeur obtenu par "timedatectl", c'est une commande "linux"
     Cette valeur est convertis au format string (puisqu'elle est au départ en bytes). 
     Et enfin on récupère l'information : Yes / No pour pouvoir l'utiliser dans une condition.
    """
    out = str(check_output("timedatectl | grep clock", shell=True), 'UTF-8')
    print(out)
    out = out[27:30]
    print(out)
    if out == "yes" :
        check_network()
 
    elif out == "no " : 
        print("\n\n\n Statut 3 : L'horloge n'est plus du tout synchronisé\n\n\n")

def check_network():
    """ 
     Fonction "ping" 
     Si la valeur retourné = 0, la connexion est fonctionnel, l'horloge sync
    """

    ip = "8.8.8.8"

    try:
        check_output("ping -c 1 " + ip, shell=True)
        return True
    except CalledProcessError: 
        return False
    
res_ping = check_network() 

if res_ping == True: 
    print("\n\n\n Statut 1 : L'horloge est synchronisé \n\n\n")
elif res_ping == False:
    print("\n\n\n Statut 2 : L'horloge n'est plus synchronisé à internet \n\n\n")

