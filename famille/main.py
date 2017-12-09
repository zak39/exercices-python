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

# Cersei Lannister
cersei = Personnage("Lannister","Cersei",10)
print("Voici {} {} et il a une force de {}".format(cersei.get_prenom(),cersei.get_nom(),cersei.get_force()))
cersei.estBonOuMechant()


# Famille Stark
stark = Famille(jon.get_nom(),[], (jon.get_nom(), jon.get_prenom()))
stark.set_nom("Stark")
print("{} est membre des {} est il est {}".format(jon.get_prenom(),stark.get_nom(),stark.get_chef()))

# Famille Lannister
lannister = Famille(tiwyn.get_nom(),[],(tiwyn.get_nom(),tiwyn.get_prenom()))
print("{} est membre des {} est il est {}".format(tiwyn.get_prenom(),lannister.get_nom(),lannister.get_chef()))

# Ajout des memnbres chez Stark
stark.ajouteMembre(jon.get_prenom(),jon.get_nom(),jon.get_force())
stark.ajouteMembre(brandon.get_prenom(),brandon.get_nom(),brandon.get_force())
stark.ajouteMembre(arya.get_prenom(),arya.get_nom(),arya.get_force())
#Affiche des membres chez stark
stark.afficheMembres()

# Ajout des membres chez Lannister
lannister.ajouteMembre(tiwyn.get_prenom(),tiwyn.get_nom(),tiwyn.get_force())
lannister.ajouteMembre(tyrion.get_prenom(),tyrion.get_nom(),tyrion.get_force())
lannister.ajouteMembre(cersei.get_prenom(),cersei.get_nom(),cersei.get_force())

# Affiche des membres chez Lannister
lannister.afficheMembres()

# On change de chef chez les lannister
lannister.set_chef((cersei.get_prenom(),cersei.get_nom()))

# On affiche les chefs
print("{} est membre des {} et leur chef est {}".format(cersei.get_prenom(),lannister.get_nom(),lannister.get_chef()))
print("{} est membre des {} et leur chef est {}".format(tiwyn.get_prenom(),lannister.get_nom(),lannister.get_chef()))

# On crée les héros Stark
benjen = Heros("Stark","Benjamin","Marcheur Blanc")
print("{} est un Héros dont la force est de {} est il est {}".format(benjen.get_prenom(),benjen.get_force(),benjen.get_statut()))

# On crée des Héros Marcheurs Blanc
night_king = Heros("King","Night","Marcheur Blanc")

# Famille White Walkers
marcheur_blanc = Famille(night_king.get_nom(),[],(night_king.get_prenom(),night_king.get_nom()))
# On modifie le nom de la Famille
marcheur_blanc.set_nom("White Walkers")

# On affiche les chefs
print("{} est membre des {} et leur chef est {}".format(night_king.get_prenom(),marcheur_blanc.get_nom(),marcheur_blanc.get_chef()))

# On ajoute des membres chez marcheur_blanc
marcheur_blanc.ajouteMembre(night_king.get_prenom(),night_king.get_nom(),night_king.get_force(),night_king.get_statut())

# On crée des Héros Lannister
jaime = Heros("Lannister","Jaime","Vivant")

# Ajout des Héros Stark
stark.ajouteMembre(benjen.get_prenom(),benjen.get_nom(),benjen.get_force(),benjen.get_statut())

# Ajout des Héros Lannister
lannister.ajouteMembre(jaime.get_prenom(),jaime.get_nom(),jaime.get_force(),jaime.get_statut())

# Affiche des membres chez les Stark
stark.afficheMembres()

# Benjen a recourt à la force !
benjen.recouvrirFroce()
print("{} est un Héros dont la force est de {} est il est {}".format(benjen.get_prenom(),benjen.get_force(),benjen.get_statut()))

# Affiche des membres chez marcheur_blanc
marcheur_blanc.afficheMembres()

# Affiche des membres chez Lannister
lannister.afficheMembres()

# On saucegarde dans des fichiers
stark.sauvegarder()
marcheur_blanc.sauvegarder()
lannister.sauvegarder()

# On charge les fichiers
#print("\n\n\n\n")
#stark.charger()
#print("\n\n\n\n")
#marcheur_blanc.charger()
#print("\n\n\n\n")
#lannister.charger()

print("\n\n\n\n")
print("Le personnage {} est : {}".format(jaime.get_prenom(),jaime))
print("{} est de type : {} ".format(jaime.get_prenom(),type(jaime)))
print("Est ce que {} est une instance de la classe Heros ? Réponse : {}".format(jaime.get_prenom(),isinstance(jaime,Heros)))

# sauvegarder la famille stark dans un fichier
stark.sauvegarder()
print("\n\n\n")
# charger la famille stark
stark.charger()

# Ned Stark
ned = Personnage("Stark","Ned",120)
print("Voici {} {} et il a une force de {}".format(ned.get_prenom(),ned.get_nom(),ned.get_force()))
ned.estBonOuMechant()

# Catelyn Stark
catelyn = Personnage("Stark","Catelyn",20)
print("Voici {} {} et il a une force de {}".format(catelyn.get_prenom(),catelyn.get_nom(),catelyn.get_force()))
catelyn.estBonOuMechant()

# Famille Stark2
stark2 = Famille(ned.get_nom(),[], (ned.get_nom(), ned.get_prenom()))

stark2.charger()

# Ajout des memnbres chez Stark
stark2.ajouteMembre(ned.get_prenom(),ned.get_nom(),ned.get_force())
stark2.ajouteMembre(catelyn.get_prenom(),catelyn.get_nom(),catelyn.get_force())
# Affiche membres stark2
stark2.afficheMembres()
print(stark2)

# Rob Stark
rob = Personnage("Stark","rob",110)
print("Voici {} {} et il a une force de {}".format(rob.get_prenom(),rob.get_nom(),rob.get_force()))
rob.estBonOuMechant()


stark3 = Famille(rob.get_nom(),[], (rob.get_nom(), rob.get_prenom()))
stark2.sauvegarder()
stark3.charger()
# Ajout des memnbres chez Stark
stark3.ajouteMembre(rob.get_prenom(),rob.get_nom(),rob.get_force())
stark3.afficheMembres()
stark2.afficheMembres()

#stark.afficheFichier("Stark.txt")
print(jon)
print(benjen)
print(cersei)
print(tiwyn)
print(night_king)
print(stark)
print(lannister)
print(marcheur_blanc)
lannister.afficheMembres()
