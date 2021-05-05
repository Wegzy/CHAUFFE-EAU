import subprocess

# Récupère le retour de timedatectl 
out = subprocess.check_output("timedatectl | grep clock", shell=True)
# Convertion 'bytes' en 'str'
out = str(out, 'UTF-8') 


print(out[27:31])
#print(type(out))



