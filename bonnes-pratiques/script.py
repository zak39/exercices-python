# -*- coding:utf-8 -*-

import doctest, unittest

def Somme(a,b):
    # Les trois guillemets permet de creer un DocString.
    # Un DocString permet de creer une documentation.
    """
    Cette fonction permet de faire la somme de a et de b.
    >>> Somme(2,3)
    5
    """
    res = a+b
    return res

class MyTest(unittest.TestCase):
    def test_is_even(self):
        x = 10
        z = 32
        self.assertTrue(Somme(x,z) == 42)       # Equivalent a 'x+z == True'
        self.assertFalse(Somme(x,z) != 42)      # Equivalent a 'x+z != 42'
        self.assertEqual(Somme(x,z),42)         # Equivalent a 'x+z' == 42


print("Voici le resultat de la fonction : {}".format(Somme(10,32)))
#help(Somme) # Affiche le DocString a la maniere d'un man

if __name__ == '__main__':
    unittest.main() # Execute un programme principal, depuis une class, dont le code contient le module unittest.
		    # Cet appel permet de retourner le résultat du problème concerné depuis la class MyTest.
    doctest.testmod() # Permet de retourner le jeu d'essai de notre DocString s'il y a une erreur.
		      # En effet, le DocTest est capable de faire un test avec la mise en place d'un exemple réel avec ">>>Somme(2,3)" avec le résultat attendu et réel qui est 5. Si nous mettions "res = a+b+2". Le programme va détecter une erreur comme quoi c'est

# Code non exécuté car ne fait pas partie du bloc conditionnel if __name__ == '__main__':
print("coucou")
