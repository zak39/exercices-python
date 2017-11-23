# -*- coding:utf-8 -*-

#----- module -----

import doctest, unittest

#----- class -----

class Personnage:
    """
    La classe personnage permet de créer des personnages de l'univers de Game Of Throne
    dont on va définir :\n
    \t- Le nom
    \t- Le prenom
    \t- La force (par défaut c'est 100)
    """

    # Constructeur pour les personnages
    def __init__(self,lastname,firstname,muscle=100):
        self.nom = lastname
        self.prenom = firstname
        self.force = muscle

    def set_nom(self,lastname):
        self.nom = lastname

    def set_prenom(self,firstname):
        self.prenom = firstname

    def set_force(self,muscle):
        self.force = muscle

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_force(self):
        return self.force

    def estBonOuMechant(self):
        if self.nom == "Snow" or self.nom == "Stark":
            return True
        elif self.nom == "Lannister" or self.nom == "Tyrel":
            return False

jon = Personnage("Snow","Jon")
print("Voici {} {} et il a une force de {}".format(jon.get_prenom(),jon.get_nom(),jon.get_force()))

if jon.estBonOuMechant():
    print("C'est un gentil !")
else:
    print("C'est un méchant !")

tiwyn = Personnage("Tiwyn","Lannister",150)
print("Voici {} {} et il a une force de {}".format(tiwyn.get_prenom(),tiwyn.get_nom(),tiwyn.get_force()))

if tiwyn.estBonOuMechant():
    print("C'est un gentil !")
else:
    print("C'est un méchant !")
