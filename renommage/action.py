# -*- coding:utf-8 -*-

#----- module -----
import doctest, unittest, os, glob
from regles import *

#----- methodes -----
class Action():
    """docstring for Action."""
    def __init__(self,namedirectory,rule=''):
        self.nomdurepertoire = namedirectory
        self.regle = rule

    def __str__(self):
        return "Le répertoire {} prendra la règle suivante : {}.".format(self.nomdurepertoire,self.regle)

    #----- setters -----
    def set_nomdurepertoire(self,namedirectory):
        self.nomdurepertoire = namedirectory

    def set_regle(self,rule):
        self.regle = rule

    #----- getters -----
    def get_nomdurepertoire(self):
        return self.nomdurepertoire

    def get_regle(self):
        return self.regle

class Renommage(Action):
    """
    Docstring pour Renommage.

    Renommage est une classe permettant de renommer des fichiers avec certains critères :
    \t- Une amorce
    \t-
    """
    def __init__(self,namedirectory,rule=""):
        Action.__init__(self,namedirectory,rule)

    def renommer(self,motlet="aucun",apartir="",pre="",namefile=(False,""),post="",extension=[]):
        maliste = []
        chemin_complet = []
        files = os.listdir(self.nomdurepertoire)
        chemin = os.path.abspath(self.nomdurepertoire)+"/"
        #print("files : {}".format(files))
        #print("chemin : {}".format(chemin))

        #"texte.txt".rsplit('.')
        #['texte', 'txt']


        for cheminc in files:
            chemin_complet.append(chemin+cheminc)

        #chemin_complet = [item for item in chemin_complet if item not in extension]

        #for item in chemin_complet:
        #    print "Voici le nouveau chemun complet {}".format(item)

        # les extensions
        if extension:
            print(True)
            #ext = ["fichier1.txt","fichier2.txt","fichier3.txt"]
            #files = [item for item in files if item not in ext]
            trie_liste_chemin = []
            for ext in extension:
                #print ext
                for chemin in chemin_complet:
                    #print chemin.rsplit('.')[1]
                    if ext in chemin:
                        trie_liste_chemin.append(chemin)
            chemin_complet = trie_liste_chemin
            #for f in extension:
            #    files_reste.append(chemin+f)
        else:
            print(False)

        print("Voici le chemin complet final")
        for item in chemin_complet:
            print item

        #for item in files:
        #    print("New files : {}".format(item))

        #for item in files_reste:
        #    print("files reste start : {}".format(item))

        # le renommage de fichier
        # Décomposer le nom fichier pour récupérer les extenstions et leur attribuer des numéros (doit être dans amorce)
        if namefile[0]:
            print("namefile True : {}".format(namefile))
            new_word = namefile[1]
            cpt = 0
            for f in files:
                new_path = chemin+str(cpt)+"_"+new_word
                pathabs = chemin+f
                #print("new_path : {}".format(new_path))
                #print("pathabs : {}".format(pathabs))
                cpt = cpt+1
                #os.rename(pathabs,new_path)
                files = new_path
            namefile = (False,namefile[1])
            #print("Dans namefile : {}".format(files))
            #print(namefile)
            new_path = ""
            pathabs = ""
            #files = os.listdir(self.nomdurepertoire)
        #else:
            #print("namefile False : {}".format(namefile))

        #print("Après renommage de files : {}".format(files))

        # le prefixe
        if pre:
            print("Il y a un prefixe")
            for f in files:
                pathabs = chemin+f
                new_path = chemin+pre+f
                maliste.append(new_path)
                #print(maliste)
                #print("new_path : {}".format(new_path))
                #print("pathabs : {}".format(pathabs))
                #os.rename(pathabs,new_path)
                files = new_path
            new_path = ""
            pathabs = ""
            #print("Dans pre : {}".format(files))
            #files = os.listdir(self.nomdurepertoire)
        else:
            print("Il n'y a pas de préfixe")

        # le postfixe
        if post:
            #print("Il y a un postfixe")
            for f in files:
                pathabs = chemin+f
                new_path = chemin+f+post
                files = new_path
                #os.rename(pathabs,new_path)
        else:
            print("Il n'y a pas de postfixe")

        #print("files : {}".format(files))
        #print("files_reste {}".format(files_reste))

        #os.rename(files,files_reste)
