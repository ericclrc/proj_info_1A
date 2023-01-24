from src.indicateursStatistiques.moyenne import Moyenne
from src.colonne.colonne import Colonne
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Variance(IndicateursStatistiques):    

    def calculer(table, nom_colonne):
        """
        Renvoie la variance de la colonne de table ayant le nom "nom_colonne"
        
        Parameters
        ----------
        table : Table
            instance de Table
            
        nom_colonne : str
            nom de la colonne dont on calcule la médiane
        
        Retour:
        variance : float
        """
        colonne = table.selectionner_colonne_par_nom( nom_colonne) 

        somme = 0
        compteur = 0

        if colonne.liste_valeurs == []:
            raise ValueError ("La liste est vide")
        
        else:
            M = Moyenne.calculer(table, nom_colonne)
            for val in colonne.liste_valeurs:
                if val != 'mq':
                    somme += ((val-M)**2)
                    compteur += 1
            if compteur == 0:
                raise ValueError ("La liste ne contient que des valeurs manquantes")
                  
            else :
                return somme/compteur