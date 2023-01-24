import matplotlib.pyplot as plt
from src.graphique.graphique import Graphique
from src.table.table import Table
from src.colonne.colonne import Colonne

class Histogramme(Graphique):

    '''
    Trace un histogramme des données
    '''
    
    def afficher(table, nom_colonne):

        '''
        Affiche l'histogramme des données et le nombre de valeurs manquantes
        
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
        4          #et un graphique

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
                l.sort()
                L = [l[0]]
                
                a = 1
                b = 1

                for i in range(1,len(l)):
                    if l[i] != l[i-1]:
                        L.append(l[i])
                        if a > b:
                            b = a
                            a = 1
                    else:
                        a+=1
                ax1 = plt.subplot()
                ax1.set_title( nom_colonne)
                plt.hist(l)
                plt.xticks(L)
                plt.ylim(0, b + 0.1*max(L))
                plt.show()

                
                print ( "La colonne " + str(nom_colonne) + " comporte "  + str(valeurs_manquantes) + " valeurs manquantes")
