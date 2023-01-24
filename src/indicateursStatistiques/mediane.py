from unittest.util import sorted_list_difference
from src.colonne.colonne import Colonne
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Mediane(IndicateursStatistiques):


    def calculer(table, nom_colonne):
        """
        Renvoie la médiane de la colonne de table ayant le nom "nom_colonne"
        
        Parameters
        ----------
        table : Table
            instance de Table
            
        nom_colonne : str
            nom de la colonne dont on calcule la médiane
        Retour:
        mediane : float
        """
        colonne = table.selectionner_colonne_par_nom( nom_colonne)

        copy_list = []

        if colonne.liste_valeurs == []:
            raise ValueError ("La liste est vide")

        
        for val in colonne.liste_valeurs:
            if val != 'mq':
                copy_list.append(val)
        
        if copy_list == []:
            raise ValueError ("La liste ne contient que des valeurs manquantes")       
        
        copy_list.sort
        
        if len(copy_list)%2 == 1: # la liste est de cardinal impair 
            indice_mediane = (len(copy_list)//2)
            valeur_mediane = copy_list[indice_mediane]
        
        else: # la liste est de cardinal pair 
            indice_mediane1 = int(len(copy_list) / 2) - 1
            indice_mediane2 = int(len(copy_list) / 2)
            valeur_mediane = (copy_list[indice_mediane1] + copy_list[indice_mediane2]) /2

        return valeur_mediane