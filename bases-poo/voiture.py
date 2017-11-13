# -*- coding:utf-8 -*-

#----- module -----

import doctest, unittest

#----- Class -----
class Voiture:
    """
    C'est une classe qui permet de creer des voitures avec les attributs suivant :
    \t- immatricule
    \t- date
    \t- marque
    >>> Voiture("XYZ",2017,"Porsche")
    """

    # Constructeur qui initialise les attributs (un attribut est une caractéristique)
    def __init__(self,immat,date,marque):
        self.immatricule = immat    # attribut qui est immatricule de la voiture
        self.date = date
        self.marque = marque

    # Setter (modifier) la plaque d'immatriculation
    def set_Immat(self,immat):
        self.immatricule = immat

    # Setter (modifier) modifier la date
    def set_Date(self,date):
        self.date = date

    # Setter (modifier) la marque
    def set_Marque(self,nom_marque):
        self.marque = nom_marque

    # Guetteur qui sert uniquement a afficher le nom
    def get_immat(self):
        return self.immatricule

    def get_date(self):
        return self.date

    def get_marque(self):
        return self.marque

    # Methode qui permet d'afficher les caracteristiques de la voiture
    def affiche(self):
        return self.immatricule,self.date,self.marque

    # Methode pour savoir si c'est
    def estDeCollection(self):
        if self.date < 1997:
            return True
        else:
            return False

    # Methode qui permet déterminer si la voiture est de luxe ou pas
    def estDeLuxe(self):
        if self.marque == "Porsche":
            return True
        else:
            return False

#----- main -----

# v1 est un objet (ou instance) de la classe Voiture
v1 = Voiture("XYZ",2007,"Porsche")
print(v1)

# v2 est un objet (ou instance) de la classe Voiture
v2 = Voiture("ABC",1993,"Clio")
print(v2.affiche())

# Modification la marque de v1
v1.set_Marque("Renault")

# Affiche les attributs de v1
print(v1.affiche())

# Condition pour savoir si v2 est une voiture de collection
if v2.estDeCollection():
    print("C'est une voiture de collection")
else:
    print("Ce n'est pas une voiture de collection")

# Condition pour savoir si v2 est une voiture de luxe
if v2.estDeLuxe():
    print("C'est une voiture de luxe")
else:
    print("Ce n'est pas une voiture de luxe")
