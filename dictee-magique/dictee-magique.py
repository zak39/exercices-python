# -*- coding:utf8 -*-

#--------- Imports ---------

import wave, pyaudio, os, random

#--------- fonctions / méthodes ---------

# Compter le nombre de mot
def comptage(nb):
    compter = 0
    for i in range(0,nb):
        compter = compter + liste.count(doublon_liste[i])
    return compter

# Afficher le mot et le nombre d'occurence
def affiche_occurrence(nb,doublon_liste):
    for i in range(0,nb):
        print(str(doublon_liste[i])+" "+str(liste.count(doublon_liste[i])))

# Affiche le taux d'occurence dans un texte
def pourcentage(doublon_liste,nb,compter):
    for i in range(0,nb):
        calcul = round((float(liste.count(doublon_liste[i]))/float(compter))*100,2)
        print("Le mot '{}' apparait {} sur les {} soit {}% de fois.".format(str(doublon_liste[i]),str(liste.count(doublon_liste[i])),str(nb),str(calcul)))

# Supprime des mots dans la var texte
def deleteElement(liste_parse):
    rep = True
    while rep:
        char = raw_input("\nEst-ce que vous voulez ignorer des mots ? [O]ui [N]on ")
        if char == "O":
            liste_ignore = raw_input("\nEcrire votre liste de mot à ignorer en mettant comme séparateur des espaces : ")
            liste_ignore = liste_ignore.split()
            liste_parse = [item for item in liste_parse if item not in liste_ignore]
            rep = False
        elif char != "N":
            print("\nProblème dans la saissie.\n")
        else:
            rep = False
    return liste_parse

# Supprime certaine ponctuation dans le texte
def deleteCaractere(texte_parse):
    texte_parse = texte_parse.replace("."," ")
    texte_parse = texte_parse.replace("'"," ")
    texte_parse = texte_parse.replace(","," ")
    texte_parse = texte_parse.replace('"',' ')
    texte_parse = texte_parse.replace(':',' ')
    texte_parse = texte_parse.replace(';',' ')
    texte_parse = texte_parse.replace('(',' ')
    texte_parse = texte_parse.replace(')',' ')

    liste_parse = texte_parse.split()
    liste_caractere = ["?","!"]
    liste_parse = [item for item in liste_parse if item not in liste_caractere]

    return liste_parse

# Ouvrir, lire et fermer un fichier
def OpenFic(fic):
    # ouverture du fichier
    ouvrir_fic=open(fic)
    # lecture du fichier
    contenu=ouvrir_fic.read()
    return contenu
    CloseFile(contenu)

#--

# Ouverture du son au format wave
def OpenWave(mus):
    open_mus = wave.open(mus,"rb")
    return open_mus

# Récupération de certainnes propriétés du son
def Stream(initAudio,open_mus):
    stream = initAudio.open(
                format=initAudio.get_format_from_width(open_mus.getsampwidth()),
                channels=open_mus.getnchannels(),
                rate=open_mus.getframerate(),
                output=True)
    return stream

# Lire des données d'un son en 1024 octets
def ReadData(open_mus):
    data = open_mus.readframes(1024)
    return data

# Jouer le son en ligne de commande
def PlaySound(stream,data,open_mus):
    while len(data) > 0:
        stream.write(data)
        data = open_mus.readframes(1024)

# Fermeture des fichiers
def CloseSound(stream,initAudio):
    stream.stop_stream()
    stream.close()
    initAudio.terminate()

# Fonction qui répète les traitements pour jouer un son en ligne de commande
def TraitementAudio(fichierWave):
    musique = OpenWave(fichierWave)

    initialisation_audio = pyaudio.PyAudio()
    prepa_lecture = Stream(initialisation_audio,musique)

    donnees = ReadData(musique)

    PlaySound(prepa_lecture,donnees,musique)
    pass

#--

def ListenWordSound(nb,doublon_liste,chemin_mus):
    print("Attention ! Écoutez le son associé au mot")
    for i in range(0,nb):
        print("Le mot '{}' est associé au son '{}'".format(doublon_liste[i],chemin_mus[i]))
        TraitementAudio(chemin_mus[i])
    pass

#--------- main ---------

# Initialisation des variables

chemin = raw_input("Merci de saisir le chemin absolu de votre fichier\n\tExemple : /home/Documents/fichier.txt.\n\nSaisir chemin absolu : ")

try:
    texte = OpenFic(chemin)

    liste = deleteCaractere(texte)

    print("\nVoici le texte à analyser : \n\n"+texte)

    liste = deleteElement(liste)
    doublon_liste = list(set(liste))
    nombre = len(doublon_liste)

    # Appel(le)s fonctions / méthodes
    compt = comptage(nombre)
    affiche_occurrence(nombre,doublon_liste)
    pourcentage(doublon_liste,nombre,compt)
except:
    print("Le fichier n'a pas pu être ouvert")

#--------- main2 ---------
#CloseSound(prepa_lecture,initialisation_audio)
path="sons/naturals/"
ListeMusique=os.listdir(path)
path_list_music = []

# Ajout dans une liste le chemin absolu des sons
for item in ListeMusique:
    path_list_music.append(path+item)

# Joue les sons en parcourant la liste des différents sons
#for item in path_list_music:
#    print("Le son utilisé est le {}".format(item))
#    TraitementAudio(item)

print("---------------------------")
print("Il y a en tout {} mot(s) dans le fichier".format(nombre))
nombre_sons = len(path_list_music)
print("Il y a {} son(s) en tout".format(nombre_sons))

if nombre > nombre_sons:
    print("Il y a trop de mot ! Merci d'en retirer dans votre fichier.\n\n\tRemarque : Vous pouvez avoir des doublons dans votre fichier")
else:
    #print("On joue les sons")
    difference = nombre_sons - nombre
    #print("La différence est de {}".format(difference))

    for nb in range(0,difference):
        path_list_music.pop()

    #print("Maintenant il y a {} son(s)".format(len(path_list_music)))

    #print("\nVoici les doublons : {}".format(doublon_liste)+"\n")
    #print("==============================================")

    ListenWordSound(nombre,doublon_liste,path_list_music)

    point=0

    saisieUser = ""
    fini = False
    while fini == False:
        print(path_list_music)
        random.shuffle(path_list_music)
        print(path_list_music)
        saisieUser = raw_input("Saisir le texte : ")
        fini=True
        pass
