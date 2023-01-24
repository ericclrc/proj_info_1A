from abc import ABC, abstractmethod

class IndicateursStatistiques(ABC):
    
    @abstractmethod
    def calculer(table, nom_colonne):
        pass
