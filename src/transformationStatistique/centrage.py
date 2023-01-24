from src.indicateursStatistiques.moyenne import Moyenne 
from src.colonne.colonne import Colonne
from src.transformationStatistique.transformation_statistique import TransformationStatistique
from src.table.table import Table

class Centrage(TransformationStatistique):


    def appliquer(table, nom_colonne):

        """
        Renvoie une instance de table dont la colonne nommée "nom_colonne" a été centrée
        ATTENTION : cette méthode modifie directement la table en argument
        
        Parameters
        ---------- 
        table : Table
            une instance de Table
        nom_colonne : str
            nom de la colonne à centrer

        Returns
        ----------
        table : Table
            renvoie la table en argument avec la colonne du nom "nom_colonne" centrée

        Examples
        ----------
        data = Table("nom",[Colonne("var1",[1,2,3]),Colonne("var2",[4,5,6])])
        >>> Centrage.appliquer(data, "var1")
        Table("nom", [Colonne("var1",[-1,0,1]), Colonne("var2", [4,5,6])])
        data2 = Table("nom",[Colonne("var1",["mq","mq","mq"]),Colonne("var2",[4,5,6])])
        >>> Centrage.appliquer(data2, "var1")
        ValueError: La liste ne contient que des valeurs manquantes
        """
        colonne = table.selectionner_colonne_par_nom(nom_colonne)

        valeurs_centrees = []
        if colonne.liste_valeurs == []:
            raise ValueError ("La liste est vide") 
 
        else: 
            M = Moyenne.calculer(table, nom_colonne)
            for val in colonne.liste_valeurs:
                if val != 'mq':
                    val1 = val - M
                valeurs_centrees.append(val1)
            if valeurs_centrees == []:
                raise ValueError ("La liste ne contient que des valeurs manquantes")  
            
            indice_colonne = 0
            for k in range(len(table.liste_colonnes)):
                if table.liste_colonnes[k].nom_colonne == nom_colonne:
                    indice_colonne = k
                    table.liste_colonnes[indice_colonne].liste_valeurs = valeurs_centrees
            return table

if __name__ == "__main__":
    import doctest
    doctest.testmod()
