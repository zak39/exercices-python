# -*- coding:utf-8 -*-

#----- module -----

import doctest, unittest, pickle

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
    def __init__(self,lastname="",membre=[],leader=("","")):
        self.nom = lastname
        #self.prenom = firstname
        self.chef = leader
        self.membres = membre

    # Setters
    def set_nom(self,lastname):
        self.nom = lastname

    def set_membres(self,membre):
        self.membres = membre

    def set_chef(self,leader):
        self.chef = leader

    # Getters
    def get_nom(self):
        return self.nom

    def get_membres(self):
        return self.membres

    def get_chef(self):
        return self.chef

    # Methode pour afficher les membres ligne par ligne
    def afficheMembres(self):
        print("Voici les membres de la famille {}".format(self.nom))
        for item in self.membres:
            print(item)

    # Methode pour ajouter des membres
    def ajouteMembre(self,prenom,nom,force,statut=""):
        # pickley.load() # pour enregistrer tout dans une ligne
        self.membres.append(prenom)
        self.membres.append(nom)
        self.membres.append(force)
        self.membres.append(statut)

    # Methode pour charger un fichier qui contient des objets
    def charger(self):
        with open("{}.txt".format(self.nom),"rb") as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            self.membres = mon_depickler.load()
            self.membres.append("")
    # Methode pour sauvegarder des objets dans un fichier binaire
    def sauvegarder(self):
        with open("{}.txt".format(self.nom),"wb") as fichier:
            pickle.dump(self.membres,fichier)
