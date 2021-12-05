import random

def capture(t,b,pv,pvmax,s):
    """Déclaration des variables"""
    t=float(t) #Taux de capture (entre 3 et 255). +elevé = +facile
    b=float(b) #Pokéball
    pv=float(pv) #Pv restant (plus affaibli, plus facile)
    pv_max=float(pvmax) #Pv max
    s=float(s) #1=Aucun; 1,5=Paralysé,Empoisonné ;2=Endormi -> +elevé = +facile

    """Calcule de a"""
    a=float((1-(2/3)*(pv/pv_max))*t*b*s)

    """Conditions"""
    if a>=255:
        print("Attrapé avec a")
    else:
        #Calcul de b
        b=float(65535*((a/255)**0.25))

        #Tire au hasard
        n1=random.randint(0,65535)
        n2=random.randint(0,65535)
        n3=random.randint(0,65535)
        n4=random.randint(0,65535)

        #Verif
        if n1 <= b and n2 <= b and n3 <= b and n4 <= b:
            print("Attrapé avec b")
        else :
            print("Perdu")

#Chenipan
capture(255,1.5,75,100,2) #75% correspond à 75 pv restant sur 100 en tout

#Pikachu
capture(190,1,50,100,1.5) #50% (la moitié) correspond à 50 pv restant sur 100 en tout