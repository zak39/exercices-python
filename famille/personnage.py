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
            print("C'est un gentil !")
        elif self.nom == "Lannister" or self.nom == "Tyrel":
            print("C'est un méchant !")
