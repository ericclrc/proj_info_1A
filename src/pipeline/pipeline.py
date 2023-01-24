
from src.table.table import Table

from src.indicateursStatistiques.moyenne import Moyenne
from src.indicateursStatistiques.mediane import Mediane
from src.indicateursStatistiques.ecart_type import Ecart_Type
from src.indicateursStatistiques.quartile import Quartile
from src.indicateursStatistiques.variance import Variance
from src.indicateursStatistiques.summary import Summary
from src.indicateursStatistiques.somme import Somme
from src.indicateursStatistiques.maximum import Maximum
from src.indicateursStatistiques.minimium import Minimum


from src.coefficients.pearson import Pearson 
from src.coefficients.covariance import Covariance

from src.graphique.boxplot import Boxplot
from src.graphique.camembert import Camembert
from src.graphique.histogramme import Histogramme
from src.graphique.nuage_de_points import Nuage_de_points

class Pipeline:

    def appliquer(table, instructions, arguments_supplémentaires):
        """ applique les méthodes présentes dans la liste d'instructions à chaque élément de la liste arguments
        Comme les méthodes codées par notre groupe ont au plus 4 arguments, on aura 3 cas dans l'exécution du programme
        => rajouter un cas si on implémente une méthode à 5 arguments ou plus 
        
        ATTENTION : la pipeline modifie la table mise en argument, qui peut ne plus être exploitable par la suite
        => travailler sur une copie 


        Parameters:
        -----
        instructions : list 
            liste de méthodes présentes dans le programme
        arguments_supplémentaires : liste de liste
            liste des listes d'arguments supplémentaires pris par chaque instruction. Si l'instruction ne prend qu'une table en argument, mettre une liste vide

        table : Table
            table à laquelle on applique la pipeline

        Exemples:
        table = Table(" patients", [Colonne( "nom", ["Pierre", "Paul", "Jacques"]), Colonne("taille", [180, 175, 182]), Colonne("poids", [70, 60, 80]) ] )
        >>>pipeline([centrer], [["poids"]], table)
        Table(" patients", [Colonne( "nom", ["Pierre", "Paul", "Jacques"]), Colonne("taille", [180, 175, 182]), Colonne("poids", [0, -10, 10]) ] )

        >>>pipeline([centrer,trier_croissant], [["poids"],["taille"]], table)
        Table(" patients", [Colonne( "nom", ["Paul", "Pierre", "Jacques"]), Colonne("taille", [175, 180, 182]), Colonne("poids", [-10, 0, 10]) ] )
        """
        # si l'instruction ne renvoie pas de table mais par exemple un float ou un graphique 
        liste_exceptions = [Table.exporter, Moyenne.calculer, Mediane.calculer, Ecart_Type.calculer, Variance.calculer, Quartile.calculer, Summary.calculer, Somme.calculer, Maximum.calculer, Minimum.calculer,  Pearson.calculer, Covariance.calculer, Boxplot.afficher, Camembert.afficher, Histogramme.afficher, Nuage_de_points.afficher]
        
        for k in range(len(instructions)):
            nb_arg_sup = len(arguments_supplémentaires[k]) 
            
            if nb_arg_sup == 0:
                if instructions[k] in liste_exceptions:
                    instructions[k](table)
                else:
                    table = instructions[k](table)

            if nb_arg_sup == 1:
                 if instructions[k] in liste_exceptions:
                    instructions[k](table, arguments_supplémentaires[k][0])
                 else:
                    table = instructions[k](table, arguments_supplémentaires[k][0])
            if nb_arg_sup == 2:
                if instructions[k] in liste_exceptions:
                    instructions[k](table, arguments_supplémentaires[k][0], arguments_supplémentaires[k][1])
                else:
                    table = instructions[k](table, arguments_supplémentaires[k][0], arguments_supplémentaires[k][1])
                
            
            if nb_arg_sup == 3:
                if instructions[k] in liste_exceptions:
                    instructions[k](table, arguments_supplémentaires[k][0], arguments_supplémentaires[k][1], arguments_supplémentaires[k][2])
                else:
                    table = instructions[k](table, arguments_supplémentaires[k][0], arguments_supplémentaires[k][1],  arguments_supplémentaires[k][1])
        return table 