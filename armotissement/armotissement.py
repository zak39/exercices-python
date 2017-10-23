# -*- coding:utf8 -*-
# Armotissement = emprunt / nbannuite
def Armotissement(emprunt,duree):
    armotissement = emprunt/duree
    return armotissement
    pass

# interets = emprunt_restant_armortir * taux_interet
def Interet(armotissement,taux):
    interet = armotissement * (float(taux)/float(100))
    return interet
    pass

# annuite = armotissement + interet
def Annuite(armotissement,interet):
    annuite = armotissement+interet
    return annuite
    pass

# valeur_net = emprunt_restant_debut_periode - armotissement_de_annee
def ValeurNette(emprunt,armotissement_annee):
    val_nette = emprunt - armotissement_annee
    return val_nette
    pass

def CalculArmotissementConstant(interet,armotissement,annuite,val_nette,emprunt_restant,liste):
    for i in range(0,annee):
        interet = Interet(emprunt_restant,taux)
        armotissement = Armotissement(emprunt,annee)
        annuite = Annuite(armotissement,interet)
        val_nette = ValeurNette(emprunt_restant,armotissement)

        liste = liste+[["Année {}".format(i+2),emprunt_restant,interet,armotissement,annuite,val_nette]]

        emprunt_restant=val_nette

    return liste
    pass

def Affichage(liste):
    for item in liste:
        print(item)

# ce qui est donne :
#   - emprunt
#   - duree
#   - taux

# Utiliser module numpy puis un print pour l'afficher correctement

#----------- main -----------

annee = input("Durée de l'emprunt : ")
emprunt = input("Le montant de l'emprunt : ")
taux = input("Taux d'intérêt : ")

print("\nVous avez choisi un emprunt d'un montant de {}€ avec un taux d'intérêt de {}% sur {} an(s)\n".format(emprunt,taux,annee))

interet = emprunt*(float(taux)/float(100))
armotissement = emprunt/annee
annuite = armotissement+interet
val_nette = emprunt-armotissement
emprunt_restant = emprunt
liste = [["Années","Emprunt restant dû","intérêt","Armotissement","Annuité","Valeur nette"]]

liste = CalculArmotissementConstant(interet,armotissement,annuite,val_nette,emprunt_restant,liste)

Affichage(liste)
