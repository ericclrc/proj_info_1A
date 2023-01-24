from src.colonne.colonne import Colonne
from abc import ABC, abstractmethod

class Graphique(ABC):

    '''
    Classe abstraite graphique
    '''
    @abstractmethod
    def afficher(): 
        pass
