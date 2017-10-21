# -*- coding:utf8 -*-

#--------- fonctions / méthodes ---------

# Compter le nombre de mot
def comptage(nb):
    compter = 0
    for i in range(0,nb):
        compter = compter + liste.count(doublon_liste[i])
    return compter

# Afficher le mot et le nombre d'occurence
def affiche_occurrence(nb,doublon_liste):
    for i in range(0,nb):
        print(str(doublon_liste[i])+" "+str(liste.count(doublon_liste[i])))

# Affiche le taux d'occurence dans un texte
def pourcentage(doublon_liste,nb,compter):
    for i in range(0,nb):
        calcul = round((float(liste.count(doublon_liste[i]))/float(compter))*100,2)
        print("Le mot '{}' apparait {} sur les {} soit {}% de fois.".format(str(doublon_liste[i]),str(liste.count(doublon_liste[i])),str(nb),str(calcul)))

def deleteElement(liste_parse):
    rep = True
    while rep:
        char = raw_input("\nEst-ce que vous voulez ignorer des mots ? [O]ui [N]on ")
        if char == "O":
            liste_ignore = raw_input("\nEcrire votre liste de mot à ignorer en mettant comme séparateur des espaces : ")
            liste_ignore = liste_ignore.split()
            liste_parse = [item for item in liste_parse if item not in liste_ignore]
            rep = False
        elif char != "N":
            print("\nProblème dans la saissie.\n")
        else:
            rep = False
    return liste_parse

#--------- main ---------

# Initialisation des variables
texte = "\nLe chat noir est sur un arbre noir prés d'un tracteur noir\n".replace("'"," ")
liste = texte.split()

print("Voici le texte à analyser : \n"+texte)

liste = deleteElement(liste)
doublon_liste = list(set(liste))
nombre = len(doublon_liste)

# Appel(le)s fonctions / méthodes
compt = comptage(nombre)
affiche_occurrence(nombre,doublon_liste)
pourcentage(doublon_liste,nombre,compt)
