# Outils pour la conexion WIFI
# Mon tout premier module pour Micropyton

from time import sleep

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

from machine import Pin
led = Pin(2, Pin.OUT)
led.on()

import ujson

def lireF(file):
    f =open(file,'r')
    string =  f.read()
    f.close()
    return str(string)

def checkSSID(dict):
#voir pour se connecter au wifi instencier la carte wlan.
    scanWifi = []
    for i in wlan.scan():
        scanWifi.append(i[0].decode('utf8').strip())

    for ap in dict:
        for i in scanWifi:
            if (ap == i):
                return(i)

def wifiConnect(tryCo):
    countr=0

    mySSIDs = lireF('/utils/ssid_password.txt') # json en str()
    myNetworks = ujson.loads(mySSIDs) # dictionnaire de tout ce qu'on connais comme AP!


    ssidFound = checkSSID(myNetworks) # ssid correspondant au lieu

    wlan = network.WLAN(network.STA_IF)

    if wlan.isconnected() == True: # Nous avons une ip connecte
        if (len(wlan.ifconfig()[0]) > 11):
            print("Deja connecté. " + wlan.ifconfig()[0])
            led.off() # OFF c'est allumé
            return 0
        else: # Cas d'une ip incorrecte
            led.on() # Led est eteinte
            return 1
    else:
        led.on()

    wlan.active(True)
    wlan.connect(ssidFound, myNetworks[ssidFound])
#     wlan.connect('iPomme', 'manonelie')

    while (wlan.isconnected() == False): # Tant que pas connecté
        sleep(1)
        countr+=1

        if (countr > tryCo): # Abandonne si on dépasse le nombre d'essais
            print("N'est pas connecté au Wifi apres " + str(tryCo) + "  tentatives.")
     	    return 1
        else:
            pass # Fait recommencer la boucle
            # Continue ci-dessous si enfin connecté au wifi

    # A partir d'ici, le Wifi est forcement connecté
    print("")
    print("Tentative(s) de connexion : " + str(countr))
    print("IP :" + wlan.ifconfig()[0])
    led.off() # Allume la led :-)

    return 0

if __name__ == '__main__':
    from time import sleep

    wifiConnect()
