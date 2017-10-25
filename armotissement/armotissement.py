#-*- coding: utf-8 -*-

#------------- Fonctions / Methodes -------------

# Fonction: Calculer l'amortissement
def CalculAmortissementConstant(emprunt,annee,taux):
    liste = [["Annees","Emprunt restant du","interet","Armotissement","Annuite","Valeur nette"]]       # Créer la premiere liste de la matrice. Cette liste représente l'en-tête
    emprunt_restant = emprunt                                   # On met de coté l'emprunt pour mettre dans la variable emprunt_restant. Cette dernière varie en fonction de l'année
    for i in range(0,annee):
        interet = emprunt_restant * (float(taux)/float(100))    # On calcul les intérêts. C'est un coût qui correspond à une utilisation anticipé
        amortissement = emprunt/annee                           # On calcul le coût de remboursement pour l'année en cours sur le projet
        annuite = amortissement+interet                         # On calcul l'annuité. C'est le coût que l'on verse annuellement par un emprunteur pour rembourser une dette
        val_nette = emprunt_restant - amortissement             # C'est la valeur nette du coût du projet dans l'année

        liste = liste+[["Annee {}".format(i+2),emprunt_restant,interet,amortissement,annuite,val_nette]]    # Concaténation d'une liste dans une liste pour former une matrice (liste dans une liste)

        emprunt_restant=val_nette                               # On met à jour l'emprunt restant
    return liste

# Méthode: Affiche liste par liste notre matrice
def Affichage(liste):
    for item in liste:
        print(item)

#----------- main -----------

annee = input("Durée de l'emprunt : ")
emprunt = input("Le montant de l'emprunt : ")
taux = input("Taux d'intérêt : ")

print("\nVous avez choisi un emprunt d'un montant de {}€ avec un taux d'intérêt de {}% sur {} an(s)\n".format(emprunt,taux,annee))

liste = CalculAmortissementConstant(emprunt,annee,taux)
Affichage(liste)
