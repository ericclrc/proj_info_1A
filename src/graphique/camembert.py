import matplotlib.pyplot as plt
from src.graphique.graphique import Graphique
from src.table.table import Table
from src.colonne.colonne import Colonne

class Camembert(Graphique):

    '''
    Trace un graphique circulaire
    '''

    def afficher(table, nom_colonne):
      
        '''
        Renvoie le graphique circulaire des données et le nombre de valeurs manquantes
        Les variables de type str non convertibles en float ne sont pas supportées
        
        Parameters
        ----------
        table : Table
            instance de Table
        nom_colonne : str
            nom de la colonne dont on souhaite afficher un graphique 

        Returns
        -------
        int
            nombre de valeurs manquantes

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
                M = []
                a = 1

                for i in range(1,len(l)):
                    if l[i] != l[i-1]:
                        L.append(l[i])
                        M.append(a)
                        a = 1
                    else:
                        a+=1
                
                M.append(a)
                M.append(valeurs_manquantes)
                labels = L +["Valeurs manquantes"] 
                sizes = M
                ax1 = plt.subplot()
                ax1.set_title( nom_colonne)
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
                plt.axis('equal')
                plt.show()

                return valeurs_manquantes
