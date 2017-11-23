# -*- coding:utf-8 -*-

#----- module -----

import doctest, unittest

#----- class -----

class Famille:
    """
    La classe Famille permet de créer des Familles de l'univers de Game Of Throne
    dont on va définir :\n
    \t- nom
    \t- chef : Qui prendra la valeur nom et prenom
    \t- membres : qui est une liste
    """

    # Constructeur pour les Familles
    def __init__(self,lastname,membre=[],leader=("","")):
        self.nom = lastname
        #self.prenom = firstname
        self.chef = leader
        self.membres = membre

    def set_nom(self,lastname):
        self.nom = lastname

    def set_membres(self,membre):
        self.membres = membre

    def set_chef(self,leader):
        self.chef = leader

    def get_nom(self):
        return self.nom

    def get_membres(self):
        return self.membres

    def get_chef(self):
        return self.chef

    def afficheMembres(self):
        print("Voici les membres de la famille {}".format(self.nom))
        for item in self.membres:
            print(item)

    def ajouteMembre(self,prenom):
        self.membres.append(prenom)

    def charger(self):
        fic = open("{}.txt".format(self.nom),"r")
        print(fic.read())
        fic.close()

    def sauvegarder(self):
        fic = open("{}.txt".format(self.nom),"w")
        for item in self.membres:
            fic.writelines(item)
            fic.writelines("\n")
        fic.close()
