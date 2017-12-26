# -*- coding:utf-8 -*-

#----- module -----

import doctest, unittest, os

#----- class -----
class Regle():
    """
    docstring for Regle.
    """

    # Constructeur
    def __init__(self,motlet="aucun",apartir="",pre="",namefile=(False,""),post="",extension=[]):
        self.amorce = motlet
        self.apartirde = apartir
        self.prefixe = pre
        self.nomfichier = namefile
        self.postfixe = post
        self.extensions = extension

    def __str__(self):
        return "Voici les caractéristiques des régles :\n\tAmorce : {} \n\tA partir de : {} \n\tPrefixe : {} \n\tPostfix : {} \n\tNom de fichier : {} \n\tExtensions : {}".format(self.amorce,self.apartirde,self.prefixe,self.postfixe,self.nomfichier,self.extensions)

    #---------- setters ----------
    def set_amorce(self,motlet):
        self.amorce = motlet

    def set_apartirde(self,apartir):
        self.apartirde = apartir

    def set_prefixe(self,pre):
        self.prefixe = pre

    def set_nomfichier(self,namefile):
        self.nomfichier = namefile

    def set_postfixe(self,post):
        self.postfixe = post

    def set_extensions(self,extension):
        self.extensions = extension

    #---------- getters ----------
    def get_amorce(self):
        return self.amorce

    def get_apartirde(self):
        return self.apartirde

    def get_prefixe(self):
        return self.prefixe

    def get_nomfichier(self):
        return self.nomfichier

    def get_postfixe(self):
        return self.postfixe

    def get_extensions(self):
        return self.extensions
