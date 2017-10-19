# -*- coding:utf8 -*-

# Initialisation des variables
texte = "Le chat noir est sur un arbre noir prés d'un tracteur noir".replace("'"," ")
liste = texte.split()
doublon_liste = list(set(liste))
nb = len(doublon_liste)


print(liste)
print(doublon_liste)
print(nb)
