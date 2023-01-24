from src.table.table import Table 
from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne

class Supprimer_ligne(ABC):
    @abstractmethod
    def transformer(table,num):
        if len(table.liste_colonnes[0].liste_valeurs):
            for k in range(len(table.liste_colonnes)):
                del table.liste_colonnes[k].liste_valeurs[num]
        else :
            raise ValueError("Pas le bon numéro de ligne")
        return table
