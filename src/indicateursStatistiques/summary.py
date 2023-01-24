from src.colonne.colonne import Colonne
from src.table.table import Table
from src.indicateursStatistiques.indicateur_statistique import IndicateursStatistiques
from src.indicateursStatistiques.ecart_type import Ecart_Type
from src.indicateursStatistiques.maximum import Maximum
from src.indicateursStatistiques.minimium import Minimum
from src.indicateursStatistiques.moyenne import Moyenne
from src.indicateursStatistiques.quartile import Quartile
from src.indicateursStatistiques.somme import Somme
from src.indicateursStatistiques.variance import Variance


class Summary(IndicateursStatistiques):


    def calculer(table, nom_colonne):
        ''' 
        Renvoie le résummé de la colonne de table ayant le nom "nom_colonne"

        Parameters
        ---------- 
        table : Table
            une instance de table
        nom_colonne : str
            nom de la colonne dont on souhaite calculer le résumé statistique

        '''

        print("moyenne = " + str( Moyenne.calculer(table, nom_colonne) ) )
        print("max = " + str( Maximum.calculer(table, nom_colonne) ) )
        print("min = " + str( Minimum.calculer(table, nom_colonne) ) )
        print("Q1 = " + str( Quartile.calculer(table, nom_colonne)[0] ) )
        print("Q2 = " + str( Quartile.calculer(table, nom_colonne)[1] ) )
        print("Q3 = " + str( Quartile.calculer(table, nom_colonne)[2] ) )
        print("variance = " + str( Variance.calculer(table, nom_colonne) ) )
        print("écart-type = " + str( Ecart_Type.calculer(table, nom_colonne) ) )
        