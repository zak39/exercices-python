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

    # Methode spéciale permettant de d'afficher un objet au format string
    def __str__(self):
        return "{} {} possède une force de {}".format(self.prenom,self.nom,self.force)

    # Setters
    def set_nom(self,lastname):
        self.nom = lastname

    def set_prenom(self,firstname):
        self.prenom = firstname

    def set_force(self,muscle):
        self.force = muscle

    # Getters
    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_force(self):
        return self.force

    # Methode pour savoir si le personnage est un gentil ou un mechant
    def estBonOuMechant(self):
        if self.nom == "Snow" or self.nom == "Stark":
            print("C'est un gentil !")
        elif self.nom == "Lannister" or self.nom == "Tyrel":
            print("C'est un méchant !")

class Heros(Personnage):
    """
    Class qui hérite la class Personnage.
    L'attribut statut peut être soit "Mort" soit "Vivant" soit "Marcheur Blanc"
    """
    # Constructeur de la classe Heros
    def __init__(self,lastname,firstname,stat,muscle=80):
        Personnage.__init__(self,lastname,firstname,muscle)
        self.statut = stat

    # Methode spéciale permettant de d'afficher un objet au format string
    def __str__(self):
        return "{} {} est un héros avec {} de force et faisant partie des {}".format(self.prenom,self.nom,self.force,self.statut)

    # Setters
    def set_statut(self,stat):
        self.statut = stat

    # Getters
    def get_statut(self):
        return self.statut

    # Methode pour remettre la force à 100
    def recouvrirFroce(self):
        self.force = 100
