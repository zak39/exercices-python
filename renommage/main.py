# -*- coding:utf-8 -*-

#----- module -----
from regles import *
#from listeregle import *
from action import *

#----- main -----

regle = Regle("aucun","","aos_",(True,"depose"),"_devops",[".txt",".png"])
print(regle.get_prefixe())
print(type(regle.get_prefixe()))


appli_regle = Renommage("dossier","")

appli_regle.renommer(regle.get_amorce(),regle.get_apartirde(),regle.get_prefixe(),regle.get_nomfichier(),regle.get_postfixe(),regle.get_extensions())
#appli_regle.prefixe(regle.get_prefixe(),regle.get_nomfichier())
#appli_regle.postfixe(regle.get_postfixe(),regle.get_nomfichier())
#appli_regle.extension(regle.get_extensions())
#appli_regle.nomfichier(regle.get_nomfichier())
