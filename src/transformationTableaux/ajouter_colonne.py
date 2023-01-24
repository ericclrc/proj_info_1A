from src.table.table import Table 
from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne

class Ajouter_colonne(ABC) :
    @abstractmethod
    def transformer(table,liste,nom):
        if len(table.liste_colonnes[0].liste_valeurs)==len(liste) :
            table.liste_colonnes.append(Colonne(nom,liste))
        else : 
            raise ValueError("liste pas à la bonne taille")
        return table
