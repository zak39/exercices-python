# Description

Programme permettant de jouer à la `dictée magique`.

Régles du jeu :

1. Écoute attentivement les sons et observe les mots associés. Puis, ce sera à toi de jouer.
2. Quand tu joueras, écoute bien les sons puis on te demandera de saisir le nom de l'animal que tu auras entendu-e.  

**Remarque** : À chaque fois que tu auras validé-e ta réponse, on t'informera si tu as **Juste** ou **Faux** :0)  Un score sera affiché à la fin du jeu ;0)

# Prérequis avant compilation #

La version de **python** utilisé est la **2.7.12** et il a été utilisé pour un système **GNU/Linux** car des chemins de fichier absolu et/ou relatif on étaient inscrit en dur dans des variables.

## Module wave ##

Il est nécessaire d'installer le module wave pour récupérer les caractéristiques des fichiers au format wave, en faisant `pip install wave`.

**Remarque** : Il est peut-être nécessaire de mettre à jour `pip` en faisant `pip install --upgrade` avant l'installation du module.

## Module pyaudio ##

Il est nécessaire d'installer le module pyaudio pour l'utilisation du script afin d'écouter les sons.

Pour cela, il faut installer le paquet adapté en faisant `apt-get install python-pyaudio` puis, faire `python -m pip install pyaudio`.

**Remarque** : Il est peut-être nécessaire de mettre à jour `pip` en faisant `pip install --upgrade` avant l'installation du module.

# Compiler le script

Pour utiliser le script `dictee-magique.py`, il faudra être dans le dossier `./dictee-magique/` puis de saisir la commande suivante :

```
python dictee-magique.py
```
