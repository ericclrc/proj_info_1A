from math import sqrt
from src.indicateursStatistiques.variance import Variance
from src.colonne.colonne import Colonne
from src.table.table import Table
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Ecart_Type(IndicateursStatistiques):
    

    def calculer(table, nom_colonne):
        """
        Renvoie l'écart-type de la colonne de table ayant le nom "nom_colonne"
        
        Parameters
        ----------
        table : Table
            instance de Table
            
        nom_colonne : str
            nom de la colonne dont on calcule la médiane
        
        Retour:
        ecart_type : float
        """
        colonne = table.selectionner_colonne_par_nom( nom_colonne) 

        sigma = Variance.calculer(table, nom_colonne)

        return(sqrt(sigma))