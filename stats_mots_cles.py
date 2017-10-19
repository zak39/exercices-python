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

print(liste)
print(doublon_liste)
print(nb)
print(compter)
