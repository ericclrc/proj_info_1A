import matplotlib.pyplot as plt
from src.graphique.graphique import Graphique
from src.table.table import Table
from src.colonne.colonne import Colonne

class Boxplot(Graphique):

    '''
    Trace le boxplot des données
    '''

    def afficher(table, nom_colonne):

        '''
        Renvoie le boxplot des données

        Parameters
        ----------
        table : Table
            instance de Table
        nom_colonne : str
            nom de la colonne dont on souhaite afficher un graphique 
        
        Examples
        --------
        table = Table("nom_table",Colonne("nom_colonne", ["1","mq","1","2","mq","3","1","mq","3","3","mq","2","3"]))
        >>> afficher(table, "nom_colonne")
        4
        table = Table("nom_table",Colonne("nom_colonne", ["A","mq","B","C","mq","B","A","mq","A","B","mq","A","A"]))
        >>> afficher(table, "nom_colonne")
        TypeError
        '''
        colonne = table.selectionner_colonne_par_nom( nom_colonne)
        liste = colonne.liste_valeurs
        
        if liste == []:
            raise ValueError('Liste vide')
        
        else:
            l = []
            valeurs_manquantes = 0
            for i in range(len(liste)):
                if liste[i] != "mq":
                    l.append(liste[i])
                else:
                    valeurs_manquantes += 1

            if l == []:
                raise ValueError('La liste ne contient que des valeurs manquantes')
                
            else:  
                ax1 = plt.subplots()
                plt.boxplot(l)
                a = max(l) - min(l)
                plt.ylim(min(l) - 0.1*a, max(l) + 0.1*a)
                plt.title("Boxplot de "+ nom_colonne)
                plt.show()
                print ( "La colonne " + str(nom_colonne) + " comporte "  + str(valeurs_manquantes) + " valeurs manquantes")
