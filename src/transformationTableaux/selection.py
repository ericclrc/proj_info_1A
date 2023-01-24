from src.transformationTableaux.transposition import Transposer
from src.table.table import Table 
from abc import ABC, abstractmethod
from src.colonne.colonne import Colonne
class Selection(ABC) : 
     @abstractmethod
     def transformer(table,var,condition,option):
        """Sélectionne lignes selon une valeurs d'une variable
        Parameters
        ----------
        table : table 
        instance de la classe table
        var : str
        nom de la variable à analyser
        conditionc : list
        liste des conditions (un ou deux éléments)
        option : str
        défini la séléction 
        Returns
        ----------
        tabfinal : table
        instance de la classe table
        
        Exemples 
        ----------
        tablexemple = Table("exemple",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
        >>> tranformer(tablexemple,"taille",[185],"inf")
        Table("exemple",[Colonne([56],"age"),Colonne([181],"taille")])

        tablexemple2 = Table("exemple2",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
        >>> tranformer(tablexemple2,"taille",[170,200],"inter")
        Table("exemple2",[Colonne([23,56],"age"),Colonne([192,181],"taille")])"""
        N=len(table.liste_colonnes) 
        n=len(table.liste_colonnes[0].liste_valeurs)
        L=[]
        Ltranspo=[]
        liste_nom=[]
        for k in range(len(table.liste_colonnes)):
            L.append(table.liste_colonnes[k].liste_valeurs)
            liste_nom.append(table.liste_colonnes[k].nom_colonne)
        tabselect = []
        for i in range(N):
            if var == liste_nom[i] :
                tabligne = Transposer.transformer(table)
                for j in range(len(L[i])) :
                    if option == "equal":
                        if L[i][j] == condition[0] :
                            tabselect.append(tabligne.liste_colonnes[j].liste_valeurs)
                    if option == "sup" :
                        if L[i][j] != "mq" and L[i][j] > condition[0] :
                            tabselect.append(tabligne.liste_colonnes[j].liste_valeurs)
                    if option == "inf" :
                        if L[i][j] != "mq" and L[i][j] < condition[0] :
                            tabselect.append(tabligne.liste_colonnes[j].liste_valeurs)
                    if option == "inter" :
                        if L[i][j] != "mq" and condition [0] < L[i][j] < condition[1] :
                            tabselect.append(tabligne.liste_colonnes[j].liste_valeurs)
        for i in range(n):
            COLi = []
            for j in range(len(tabselect)):
                COLi.append(tabselect[j][i])
            Ltranspo.append(COLi)
        table.liste_colonnes.clear()
        for k in range(N):
            table.liste_colonnes.append(Colonne(liste_nom[k],Ltranspo[k]))
        return table

         
