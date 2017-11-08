# -*- coding:utf8 -*-

# Script dont les sons sont associes a des mots.
# Mais ces mots n'ont aucun rapport avec les sons.
# Par exemple : Le son "poule" est associe au mot "cool"
# Donc aucun rapport 

#--------- Imports ---------

import os, random, collections, time

try:
    import wave
except:
    print("Il faut installer le module wave avec pip : pip install wave")

try:
    import pyaudio
except:
    print("Il faut installer le module pyaudio en téléchargeant le packet suivant sous linux : python-pyaudio")


#--------- fonctions / méthodes ---------

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

# Méthode qui supprime les éléments dans la liste de musique en fonction du nombre de mot
def DeleteDiff(nbson,nb,path_list_music):
    difference = nbson - nb
    for nb in range(0,difference):
        path_list_music.pop()
    pass

# Fonction qui assemble les listes de mot et de musique en dictionnaire
def ConvertToDic(liste,liste2):
    nb = len(liste)
    dictionnaire = {}
    for i in range(0,nb):
        dictionnaire[liste[i]] = liste2[i]
    return dictionnaire

# Méthode pour écouter le son associé au mot avant de jouer
def ListenWordSound(dico):
    print("\nAttention ! Écoutez le son associé au mot\n")
    time.sleep(10)
    for key,value in dico.iteritems():
        print("Le mot '{}'".format(key))
        TraitementAudio(value)
        time.sleep(3)
    pass

# Fonction qui tri aléatoirement le dictionnaire pour le jeu
def RandomDico(dico):
    listeDeDico = dico.items()
    random.shuffle(listeDeDico)
    dico = collections.OrderedDict(listeDeDico)
    return dico

# Fonction qui calcul le score et indique si l'utilisateur a saisi le bon mot
def PointAndIdication(point,value,saissie_user):
    if saissie_user == value:
        point=point+1
        rep = "Vous avez juste"
    else:
        rep = "Vous avez faux"
    return point,rep
    pass

def Score(point):
    moyenne = round(float(point)/float(2))
    if point >= moyenne:
        print("Cool ! Vous êtes supérieures à la moyenne ! ;)")
    elif point == moyenne:
        print("Pas mal ! Vous avez pile la moyenne :)")
    elif point <= moyenne:
        print("Vous n'étiez pas loin des attentes. Faite vous une réfléxion de vos erreurs et ré-éssayez ;)")
    pass

# Méthode pour débuter le jeu
def StartTheGame(dico):
    point=0
    saisieUser = ""
    fini = False

    while fini == False:
        print("\nGo à vous !\n")
        for key,value in dico.iteritems():
            TraitementAudio(value)
            saisieUser = raw_input("Saisir le texte : ")
            point,reponse = PointAndIdication(point,key,saisieUser)
            print(reponse)
        fini=True
        pass
        print("Vous avez {} point(s) sur les {} mot(s)".format(point,nombre))
        Score(point)
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

    #--------- main2 ---------

    path="sons/naturals/"
    ListeMusique=os.listdir(path)
    path_list_music = []

    # Ajout dans une liste le chemin absolu des sons
    for item in ListeMusique:
        path_list_music.append(path+item)

    nombre_sons = len(path_list_music)
    print("Il y a {} son(s) en tout".format(nombre_sons))

    if nombre > nombre_sons:
        print("Il y a en tout {} mot(s) dans le fichier".format(nombre))
        print("Il y a trop de mot ! Merci d'en retirer dans votre fichier.\n\n\tRemarque : Vous pouvez avoir des doublons dans votre fichier")
    else:
        print("Il y a en tout {} mot(s) dans le fichier".format(nombre))

        DeleteDiff(nombre_sons,nombre,path_list_music)
        MonDictionnaire = ConvertToDic(doublon_liste,path_list_music)
        #MonDictionnaire = RandomDico(MonDictionnaire)
        ListenWordSound(MonDictionnaire)
        MonDictionnaire = RandomDico(MonDictionnaire)
        StartTheGame(MonDictionnaire)
except:
    print("Le fichier n'a pas pu être ouvert")
