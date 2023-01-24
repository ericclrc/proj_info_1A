from src.indicateursStatistiques.mediane import Mediane
from src.colonne.colonne import Colonne
from src.table.table import Table
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques

class Quartile(IndicateursStatistiques):


    def calculer(table, nom_colonne):
        """
        Renvoie les quartiles de la colonne de table ayant le nom "nom_colonne"
        
        Parameters
        ----------
        table : Table
            instance de Table
            
        nom_colonne : str
            nom de la colonne dont on calcule la médiane
        Retour :
        quartiles : list
            liste des quartiles de la colonne
        """   
        colonne = table.selectionner_colonne_par_nom(nom_colonne)

        if colonne.liste_valeurs == []:
            raise ValueError ("La liste est vide")

        copy_list = []

        for valeur in colonne.liste_valeurs:
            if type(valeur)!= str:
                copy_list.append(valeur)

        copy_list.sort()

        if len(copy_list)%2 == 1: # la liste est de cardinal impair 

            table1 = Table("table1", [Colonne("nom_colonne1", copy_list[0:(len(copy_list)//2 )+1])])
            table2 = Table("table2", [Colonne("nom_colonne2", copy_list[ (len(copy_list)//2 ) : ] )])
            return [ Mediane.calculer(table1, "nom_colonne1"), Mediane.calculer(table,nom_colonne), Mediane.calculer(table2, "nom_colonne2")]
        
        else: # la liste est de cardinal pair
            table1 = Table("table1", [Colonne("nom_colonne1", copy_list[0:(len(copy_list)//2)])])
            table2 = Table("table2", [Colonne("nom_colonne2", copy_list[ (len(copy_list)//2): ] )])
            return [ Mediane.calculer(table1, "nom_colonne1"), Mediane.calculer(table,nom_colonne), Mediane.calculer(table2, "nom_colonne2")]
        

            









