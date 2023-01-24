
from src.transformationTableaux.transposition import Transposer
from src.table.table import Table 
from abc import ABC, abstractmethod 
from src.colonne.colonne import Colonne

class Triercroiss(ABC) :
    @abstractmethod
    def transformer(table,var):
        """tri le tableau selon une colonne
        Parameters 
        ------------
        table : objet table
        instance de table à trier 
        var : str
        nom de la colonne à trier
        Returns
        ----------
        table : table
        instance de table triée
           
        Exemples
        -----------
        tablexemple = Table("exemple",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
        >>> tranformer(tablexemple,"taille")
        Table("exemple",[Colonne([12,56,23],"age"),Colonne(["mq",181,192],"taille")])

        tablexemple2 = Table("exemple2",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
        >>> tranformer(tablexemple2,"age")
        Table("exemple2",[Colonne([12,23,56],"age"),Colonne(["mq",192,181],"taille")])"""
        L = []
        liste_nom = []
        for k in range(len(table.liste_colonnes)):
            L.append(table.liste_colonnes[k].liste_valeurs)
            liste_nom.append(table.liste_colonnes[k].nom_colonne)
        compteur = 0
        for k in range(len(L)) :
            if var == table.liste_colonnes[k].nom_colonne :
                copytable=Transposer.transformer(table)
                for a in range(len(L[k])):
                    if L[k][a] == "mq":
                        L[k][a],L[k][compteur] = L[k][compteur],L[k][a]
                        copytable.liste_colonnes[a].liste_valeurs,copytable.liste_colonnes[compteur].liste_valeurs = copytable.liste_colonnes[compteur].liste_valeurs,copytable.liste_colonnes[a].liste_valeurs
                        compteur += 1
                n = len(L[k])
                for i in range(compteur+1,n):
                    j = i
                    while j > compteur and L[k][j-1] > L[k][j]:
                        L[k][j-1],L[k][j]=L[k][j],L[k][j-1]
                        copytable.liste_colonnes[j].liste_valeurs,copytable.liste_colonnes[j-1].liste_valeurs = copytable.liste_colonnes[j-1].liste_valeurs,copytable.liste_colonnes[j].liste_valeurs
                        j -= 1
        tabfinal = Transposer.transformer(copytable)
        LFINAL=[]
        for k in range(len(tabfinal.liste_colonnes)):
            LFINAL.append(tabfinal.liste_colonnes[k].liste_valeurs)
        taille=len(tabfinal.liste_colonnes)
        table.liste_colonnes.clear()
        for k in range(taille):
            table.liste_colonnes.append(Colonne(liste_nom[k],LFINAL[k]))
        return table
