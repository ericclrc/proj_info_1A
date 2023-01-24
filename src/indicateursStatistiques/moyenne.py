from src.colonne.colonne import Colonne
from src.table.table import Table
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Moyenne(IndicateursStatistiques):


    def calculer(table, nom_colonne):
        ''' 
        Renvoie la moyenne de la colonne de table ayant le nom "nom_colonne"

        Parameters
        ---------- 
        table : Table
            une instance de table
        nom_colonne : str
            nom de la colonne dont on souhaite calculer la moyenne

        '''
        somme = 0
        compteur = 0
        colonne = table.selectionner_colonne_par_nom(nom_colonne)
        
        if colonne.liste_valeurs == []:
            raise ValueError("La liste est vide") 

        for valeur in colonne.liste_valeurs:
            if valeur != 'mq':
                somme += valeur
                compteur += 1
        if compteur == 0:
            raise ValueError( " La liste ne comporte que des valeurs manquantes")
        else:
            return somme/compteur