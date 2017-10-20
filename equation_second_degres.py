# -*- coding: utf-8 -*-

import math  # Permet d'importer la fonction racine carré "sqrt(nombre)"

def CalculDelta(a,b,c):
    resultat= pow(b,2)-4*a*c                                        # On calcule delta
    return resultat

def Solution(resultat):
    if resultat < 0:
        print("Le delta est égal à "+str(resultat))
        print("L'équation possede deux solutions complexe")
        rc_resultat=resultat*-1
        x1R="({} - i RacineCarre({}))/{}".format(-b,rc_resultat,2*a)                            # Partie réelle du calcul
        x2R="({} + i RacineCarre({}))/{}".format(-b,rc_resultat,2*a)                            # Partie réelle du calcul
                                                           # Partie dividende

        print(x1R) # On affiche la première solution
        print(x2R) # On affiche la deuxième solution

    elif resultat == 0:
        print("Delta est egal à "+str(resultat))
        print ("L'équation possede une solution reelle")
        x=(-b)/(2*a)                                                      # Calcul de X
        print ("X="+str(x))                                               # On affiche la solution
    else:
        print("Delta est egal à "+str(resultat))
        print ("L'équation possede deux solutions reelles")
        rc_resultat=math.sqrt(resultat)                                   # On calcul la racine carré de delta
        y=-b-rc_resultat                                                  # Variable qui va intervenir dans le calcul de X1
        z=-b+rc_resultat                                                  # Variable qui va intervenir dans le calcul de x2
        pr=2*a                                                            # Variable qui va intervenir dans le calcul de X1 et X2
        x1=y/pr                                                           # Calcul de X1
        x2=z/pr                                                           # Calcul de X2
        print ("X1="+str(x1))                                             # On affiche la première solution
        print ("X2="+str(x2))                                             # On affiche la deuxième solution



#------------------ Programme principal ------------------

# Donne les objectifs du programme
print ("Programme qui calcule les racines d'un polynome du second degré .\n Pour rappel, l'équation est la suivante : a*x² + b*x + c = 0")

# Initialisation des variables
test=True
a=int(input('Lire a : '))                                                # On rentre la valeur de a
if(a == 0):
    while test:
        a=int(input('Resaisir a : '))
        if(a!=0):
            test=False

b=int(input('Lire b : '))                                               # On rentre la valeur de b
c=int(input('Lire c : '))                                               # On rentre la valeur de c

# Appel aux fonctions
res = CalculDelta(a,b,c)
Solution(res)
