from src.table.table import Table 
from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne

class Ajouter_ligne(ABC):
    @abstractmethod
    def transformer(table,liste):
        if len(table.liste_colonnes) == len(liste):
            for k in range(len(table.liste_colonnes)) :
                table.liste_colonnes[k].liste_valeurs.append(liste[k])
        else :
            raise ValueError("Pas la bonne taille")
        return table
