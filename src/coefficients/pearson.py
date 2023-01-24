from src.coefficients.covariance import Covariance
from src.colonne.colonne import Colonne
from src.indicateursStatistiques.ecart_type import Ecart_Type
from src.coefficients.coefficients import Coefficients
from src.table.table import Table

class Pearson(Coefficients):

    def calculer(table, nom_colonne1, nom_colonne2):
        """
        Paramètres:
        
        table : Table
        
        nom_colonne1 : str
        
        nom_colonne2: str
        """
        
        valeurs = Coefficients.valeurs_calcul_possibles( table, nom_colonne1, nom_colonne2)
        
        cov = Covariance.calculer(table, nom_colonne1, nom_colonne2)
        
        data = Table("data",  [Colonne( "colonne1", valeurs[0]), Colonne("colonne2", valeurs[1])])

        sigma_1 = Ecart_Type.calculer(data, "colonne1")
        sigma_2= Ecart_Type.calculer(data, "colonne2")

        print("Coefficient de Pearson : " + str(cov/(sigma_1 * sigma_2)))
        return cov/(sigma_1 * sigma_2)
