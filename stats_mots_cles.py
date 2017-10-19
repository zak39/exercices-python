# -*- coding:utf8 -*-

# Initialisation des variables
texte = "Le chat noir est sur un arbre noir prés d'un tracteur noir".replace("'"," ")
liste = texte.split()
doublon_liste = list(set(liste))
nb = len(doublon_liste)
compter = 0

for i in range(0,nb):
    compter = compter + liste.count(doublon_liste[i])

for i in range(0,nb):
    print(str(doublon_liste[i])+" "+str(liste.count(doublon_liste[i])))

for i in range(0,nb):
    calcul = round((float(liste.count(doublon_liste[i]))/float(compter))*100,2)
    print("Le mot '{}' apparait {} sur les {} soit {}% de fois.".format(str(doublon_liste[i]),str(liste.count(doublon_liste[i])),str(nb),str(calcul)))


print(liste)
print(doublon_liste)
print(nb)
print(compter)
