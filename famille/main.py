# -*- coding:utf-8 -*-

#----- module -----
from personnage import *    # On cherche le fichier personnage.py qui est dans le même dossier que main.py
from famille import *

#----- main -----

# Jon Snow
jon = Personnage("Snow","Jon")
print("Voici {} {} et il a une force de {}".format(jon.get_prenom(),jon.get_nom(),jon.get_force()))
jon.estBonOuMechant()

# Brandon Stark
brandon = Personnage("Stark","Brandon",50)
print("Voici {} {} et il a une force de {}".format(brandon.get_prenom(),brandon.get_nom(),brandon.get_force()))
brandon.estBonOuMechant()

# Arya Stark
arya = Personnage("Stark","Arya",250)
print("Voici {} {} et il a une force de {}".format(arya.get_prenom(),arya.get_nom(),arya.get_force()))
arya.estBonOuMechant()


# Tiwyn Lannister
tiwyn = Personnage("Lannister","Tiwyn",150)
print("Voici {} {} et il a une force de {}".format(tiwyn.get_prenom(),tiwyn.get_nom(),tiwyn.get_force()))
tiwyn.estBonOuMechant()

# Tyrion Lannister
tyrion = Personnage("Lannister","Tyrion",50)
print("Voici {} {} et il a une force de {}".format(tyrion.get_prenom(),tyrion.get_nom(),tyrion.get_force()))
tyrion.estBonOuMechant()

# Jaime Lannister
jaime = Personnage("Lannister","Jaime",200)
print("Voici {} {} et il a une force de {}".format(jaime.get_prenom(),jaime.get_nom(),jaime.get_force()))
jaime.estBonOuMechant()


# Famille Stark
stark = Famille(jon.get_nom(),[], (jon.get_nom(), jon.get_prenom()))
stark.set_nom("Stark")
print("{} est membre des {} est il est {}".format(jon.get_prenom(),stark.get_nom(),stark.get_chef()))

# Famille Lannister
lannister = Famille(tiwyn.get_nom(),[],(tiwyn.get_nom(),tiwyn.get_prenom()))
print("{} est membre des {} est il est {}".format(tiwyn.get_prenom(),lannister.get_nom(),lannister.get_chef()))

# Ajout des memnbres chez Stark
stark.ajouteMembre(jon.get_prenom())
stark.ajouteMembre(brandon.get_prenom())
stark.ajouteMembre(arya.get_prenom())
#Affiche des membres chez stark
stark.afficheMembres()

# Ajout des membres chez Lannister
lannister.ajouteMembre(tiwyn.get_prenom())
lannister.ajouteMembre(tyrion.get_prenom())
lannister.ajouteMembre(jaime.get_prenom())

# Affiche des membres chez Lannister
lannister.afficheMembres()

# On change de chef chez les lannister
lannister.set_chef((jaime.get_prenom(),jaime.get_nom()))

# On affiche les chefs
print("{} est membre des {} et leur chef est {}".format(jaime.get_prenom(),lannister.get_nom(),lannister.get_chef()))
print("{} est membre des {} et leur chef est {}".format(tiwyn.get_prenom(),lannister.get_nom(),lannister.get_chef()))
