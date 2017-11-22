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

    # Constructeur qui initialise les attributs (un attribut est une caractéristique lié à l'objet)
    def __init__(self,immat,date,marque):
        self.immatricule = immat    # attribut qui est immatricule de la voiture
        self.date = date            # attribut qui est la date de création de la voiture
        self.marque = marque        # attribut qui est la marque de la voiture

    # Setter (modifier) la plaque d'immatriculation
    def set_Immat(self,immat):
        """
        C'est une "setter" qui permet de modifier l'attribut immatricule.
        Exemple :\n\n
        >>> v1.set_Immat("GHJ")
        >>> print(v1.affiche())
        ('GHJ', 2007, 'Porsche')
        """
        self.immatricule = immat

    # Setter (modifier) modifier la date
    def set_Date(self,date):
        """
        C'est une "setter" qui permet de modifier l'attribut date.
        Exemple :\n\n
        >>> v1.set_Date(1991)
        >>> print(v1.affiche())
        ('XYZ', 1991, 'Porsche')
        """
        self.date = date

    # Setter (modifier) la marque
    def set_Marque(self,nom_marque):
        """
        C'est une "setter" qui permet de modifier l'attribut marque.
        Exemple :\n\n
        >>> v1.set_Marque("Renault")
        >>> print(v1.affiche())
        ('XYZ', 2007, 'Renault')
        """
        self.marque = nom_marque

    # Guetteur qui sert uniquement a afficher l'attribut immatricule
    def get_immat(self):
        """
        C'est une "getter" qui permet de retourner l'attribut immatricule.
        Exemple :\n\n
        >>> v2.get_immat()
        ABC
        """
        return self.immatricule

    # Guetteur qui sert uniquement a afficher l'attribut date
    def get_date(self):
        """
        C'est une "getter" qui permet de retourner l'attribut date.
        Exemple :\n\n
        >>> v2.get_date()
        1993
        """
        return self.date

    # Guetteur qui sert uniquement a afficher l'attribut marque
    def get_marque(self):
        """
        C'est une "getter" qui permet de retourner l'attribut marque.
        Exemple :\n\n
        >>> v2.get_marque()
        Clio
        """
        return self.marque

    # Methode qui permet d'afficher tous les attributs (caractéristiques) de la voiture
    def affiche(self):
        """
        C'est une méthode qui permet de retourner les attributs des objets.
        Exemple :\n\n
        >>> print(v2.affiche())
        ('ABC', 1993, 'Clio')
        """
        return self.immatricule,self.date,self.marque

    # Methode pour savoir si c'est une voiture de collection
    def estDeCollection(self):
        """
        C'est une méthode qui permet de retourner un booléen afin de déterminer si\n
        une voiture est de collection (avant 1997) ou non (plus de 1997).
        Exemple :\n\n
        >>> if v2.estDeCollection():
        >>>     print("C'est une voiture de collection")
        >>> else:
        >>>     print("Ce n'est pas une voiture de collection")
        C'est une voiture de collection
        """
        if self.date < 1997:
            return True
        else:
            return False

    # Methode qui permet déterminer si la voiture est de luxe
    def estDeLuxe(self):
        """
        C'est une méthode qui permet de retourner un booléen afin de déterminer si\n
        une voiture est de luxe ("Porsche") ou non (qui ne soit pas "Porsche").
        Exemple:\n\n
        >>> if v2.estDeLuxe():
        >>>     print("C'est une voiture de luxe")
        >>> else:
        >>>     print("Ce n'est pas une voiture de luxe")
        Ce n'est pas une voiture de luxe
        """
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

# Afficher l'attribut immatricule de l'objet (ou instance) v2
print("Voici l'attribut immatricule de v2 : {}".format(v2.get_immat()))

# Afficher l'attribut date de l'objet (ou instance) v2
print("Voici l'attribut date de v2 : {}".format(v2.get_date()))

# Afficher l'attribut marque de l'objet (ou instance) v2
print("Voici l'attribut marque de v2 : {}".format(v2.get_marque()))
