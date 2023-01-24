from src.indicateursStatistiques.ecart_type import Ecart_Type
from src.colonne.colonne import Colonne
from src.transformationStatistique.transformation_statistique import TransformationStatistique
from src.table.table import Table

class Reduire(TransformationStatistique):
    
    
    def appliquer(table, nom_colonne):

        """
        Renvoie une instance de table dont la colonne nommée "nom_colonne" a été réduite
        ATTENTION : cette méthode modifie directement la table en argument
        Parameters
        ---------- 
        table : Table
            une instance de Table
        nom_colonne : str
            nom de la colonne à réduire

        Returns
        ----------
        table : Table
            renvoie la table en argument avec la colonne du nom "nom_colonne" réduite
        
        Examples
        ----------
        data = Table("nom",[Colonne("var1",[0,2,4]),Colonne("var2",[4,5,6])])
        >>> Reduire.appliquer(data, "var1")
        Table("nom", [Colonne("var1",[1,2,3]), Colonne("var2", [4,5,6])])
        data2 = Table("nom",[Colonne("var1",["mq","mq","mq"]),Colonne("var2",[4,5,6])])
        >>> Reduire.appliquer(data2, "var1")
        ValueError: La liste ne contient que des valeurs manquantes
        """
        colonne = table.selectionner_colonne_par_nom( nom_colonne)

        
        if colonne.liste_valeurs == []:
            raise ValueError ("La liste est vide")
        
        else:
            Liste_reduite = [] 
            sigma = Ecart_Type.calculer(table, nom_colonne)
            
            for val in colonne.liste_valeurs:
                if val != 'mq':
                    val1 = val/sigma
                Liste_reduite.append(val1)
            if Liste_reduite == []:
                raise ValueError ("La liste ne contient que des valeurs manquantes")  
            else:
                
                indice_colonne = 0
                for k in range(len(table.liste_colonnes)):
                    if table.liste_colonnes[k].nom_colonne == nom_colonne:
                        indice_colonne = k
                        table.liste_colonnes[indice_colonne].liste_valeurs = Liste_reduite
                return table 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
