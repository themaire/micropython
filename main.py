#### Variables ####

#### Fonctions ####
def readMoove(mode):
    x = adx.xValue
    y = adx.yValue
    z = adx.zValue
    position = (x,y,z)

    if (mode == 'xyz'):
        return position
    elif(mode == 'rp'):
        return adx.RP_calculate(x,y,z)
    else:
        return 'La fonction demande "xyz" ou "rp" (roll pitch) comme parametre.'

#### Programme ####
print("")
print("Pret!!")
print("Reset cause : " + str(reset_cause()) + " (6 = hot reboot)")
