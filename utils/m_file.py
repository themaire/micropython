
# Outils pour exploiter des fichiers

def lireF(file):
    f =open(file,'r')
    string =  f.read()
    f.close()
    return str(string)

if __name__ == '__main__':

    lireF('utils/ssis_password.txt')




