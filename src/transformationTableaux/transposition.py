from src.table.table import Table
from src.colonne.colonne import Colonne 
from abc import ABC, abstractmethod
class Transposer(ABC) :
    @abstractmethod
    def transformer(table):
        """Transforme le tableau de ligne en tableau de colonne
        Parameters 
        -----------
        table : list
    
        Returns
        -----------
        TABTRANSPO : list
    
        Exemples 
        -----------
        >>> transposer([[1,2,3],[1,2,3]])
        [[1,1],[2,2],[3,3]]
        """
        TABTRANSPO = []
        for i in range(len(table.liste_colonnes[0].liste_valeurs)):
            COLi = []
            for j in range(len(table.liste_colonnes)):
                COLi.append(table.liste_colonnes[j].liste_valeurs[i])
            TABTRANSPO.append(COLi)
        n=len(table.liste_colonnes[0].liste_valeurs)
        table.liste_colonnes.clear()
        for k in range(n):
            table.liste_colonnes.append(Colonne("ligne",TABTRANSPO[k]))
        return table

