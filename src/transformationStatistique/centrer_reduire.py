from src.transformationStatistique.centrage import Centrage
from src.transformationStatistique.reduire import Reduire
from src.transformationStatistique.transformation_statistique import TransformationStatistique


class Centrer_Reduire(TransformationStatistique):

    def appliquer(table, nom_colonne):

        """
        Renvoie une instance de table dont la colonne nommée "nom_colonne" a été centrée réduite
        ATTENTION : cette méthode modifie directement la table en argument
        Parameters
        ---------- 
        table : Table
            une instance de Table
        nom_colonne : str
            nom de la colonne à centrer réduire

        Returns
        ----------
        table : Table
            renvoie la table en argument avec la colonne du nom "nom_colonne" centrée réduite
        
        Examples
        ---------
        data = Table("nom",[Colonne("var1",[1,2,3]),Colonne("var2",[4,5,6])])
        >>> Centrer_Reduire.appliquer(data, "var1")
        Table("nom", [Colonne("var1",[-1,0,1]), Colonne("var2", [4,5,6])])
        data2 = Table("nom",[Colonne("var1",["mq","mq","mq"]),Colonne("var2",[4,5,6])])
        >>> Centrer_Reduire.appliquer(data2, "var1")
        ValueError: La liste ne contient que des valeurs manquantes
        """
        table = Centrage.appliquer(table, nom_colonne)
        table = Reduire.appliquer(table, nom_colonne)

        return table
if __name__ == "__main__":
    import doctest
    doctest.testmod()
