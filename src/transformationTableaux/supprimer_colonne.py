from src.table.table import Table 
from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne

class Supprimer_colonne(ABC):
    @abstractmethod
    def transformer(table,nom):
        for k in range(len(table.liste_colonnes)-1):
            if table.liste_colonnes[k].nom_colonne == nom :
                del table.liste_colonnes[k]
        return table
