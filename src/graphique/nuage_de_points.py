from multiprocessing.sharedctypes import Value
import matplotlib.pyplot as plt
from src.graphique.graphique import Graphique
from src.table.table import Table
from src.colonne.colonne import Colonne
from src.coefficients.coefficients import Coefficients

class Nuage_de_points(Graphique):

    '''
    Trace le nuage de points
    '''
    
    def afficher(table, nom_colonne1, nom_colonne2):
      
        '''
        Affiche le nuage de points et le nombre de valeurs manquantes
        
        Parameters
        ----------
        colonne1 : Colonne
            colonne de données en abscisses
        colonne2 : Colonne
            colonne de données en ordonnées

        Returns
        -------
        int
            nombre de valeurs manquantes

        Examples
        --------
        >>> afficher([2,1,"mq",4,8],["mq",10,"mq",7,5])
        2
        '''
        
        colonne1 = table.selectionner_colonne_par_nom( nom_colonne1)
        colonne2 = table.selectionner_colonne_par_nom( nom_colonne2)

        liste1 = colonne1.liste_valeurs
        liste2 = colonne2.liste_valeurs

        if liste1 == [] or liste2 == []:
            raise ValueError('Les listes sont vides')
       
        else:  
            l1 = []
            l2 = []
            valeurs_manquantes = 0
            for i in range(len(liste1)):
                if liste1[i] != "mq" and liste2[i] != "mq":
                    l1.append(liste1[i])
                    l2.append(liste2[i])
                else:
                    valeurs_manquantes += 1

            if l1 == []:
                raise ValueError ('Les listes ne contiennent que des valeurs manquantes')

                
            else:
                plt.scatter(l1,l2)
                plt.title(nom_colonne1 + " en fonction de " + nom_colonne2)
                plt.xlabel(nom_colonne1)
                plt.ylabel(nom_colonne2)
                plt.show()

                
                print ( "Il y a " + str(nom_colonne) + " comporte "  + str(valeurs_manquantes) + " entrées manquantes")
