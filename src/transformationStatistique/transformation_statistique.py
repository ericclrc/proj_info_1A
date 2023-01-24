from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne

class TransformationStatistique(ABC):

    @abstractmethod
    def appliquer(table, nom_colonne):
        pass
    
