from abc import ABC, abstractmethod
from src.table.table import Table
from src.colonne.colonne import Colonne
class Coefficients(ABC):

    @abstractmethod
    def calculer(table, nom_colonne1, nom_colonne2):
        pass


    
    def valeurs_calcul_possibles(table, nom_colonne1, nom_colonne2):
        
        colonne1 = Table.selectionner_colonne_par_nom(table, nom_colonne1)
        colonne2 = Table.selectionner_colonne_par_nom(table, nom_colonne2) 

        liste_valeurs_possibles_1 = []
        
        liste_valeurs_possibles_2 = []
        compteur = 0

        for k in range(len(colonne1.liste_valeurs)):
            if colonne1.liste_valeurs[k] == 'mq':
                compteur += 1
            else:
                if colonne2.liste_valeurs[k] == 'mq':
                    compteur += 1
                else:
                    liste_valeurs_possibles_1.append( colonne1.liste_valeurs[k])
                    liste_valeurs_possibles_2.append( colonne2.liste_valeurs[k])
        return ( [liste_valeurs_possibles_1 , liste_valeurs_possibles_2, compteur])                     

