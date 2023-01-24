from src.colonne.colonne import Colonne
from src.table.table import Table
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Minimum(IndicateursStatistiques):


    def calculer(table, nom_colonne):
        ''' 
        Renvoie le minimum de la colonne de table ayant le nom "nom_colonne"

        Parameters
        ---------- 
        table : Table
            une instance de table
        nom_colonne : str
            nom de la colonne dont on souhaite calculer le minimum

        '''
        
        compteur = 0
        colonne = table.selectionner_colonne_par_nom(nom_colonne)
        mini = colonne.liste_valeurs[0]
        if colonne.liste_valeurs == []:
            raise ValueError("La liste est vide") 

        for valeur in colonne.liste_valeurs:
            if type(valeur) != str:
                if valeur < mini:
                    mini = valeur                
                compteur += 1
        if compteur == 0:
            raise ValueError( " La liste ne comporte que des valeurs manquantes ou non numériques")
        else:
            return mini