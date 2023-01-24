from src.transformationTableaux.trier_croissant import Triercroiss
from src.table.table import Table 
from abc import ABC, abstractmethod

class Trierdecroiss(ABC):
   @abstractmethod
   def transformer(table,var):
      """tri le tableau selon une colonne de manière décroissante
      Parameters 
      ------------
      table : table
      instance de table à modifier
      var : str
      nom de la colonne à trier
      Returns
      -----------
      table : table
      instance de table modifiée
      Exemples
      -----------
      tablexemple = Table("exemple",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
      >>> tranformer(tablexemple,"taille")
      Table("exemple",[Colonne([23,56,12],"age"),Colonne([192,181,"mq"],"taille")])

      tablexemple2 = Table("exemple2",[Colonne([23,12,56],"age"),Colonne([192,"mq",181],"taille")])
      >>> tranformer(tablexemple2,"age")
      Table("exemple2",[Colonne([56,23,12],"age"),Colonne([181,192,"mq"],"taille")])"""
      RES=[]
      tablainver = Triercroiss.transformer(table,var)
      for i in range(len(tablainver.liste_colonnes)):
         RES.append(tablainver.liste_colonnes[i].liste_valeurs[::-1])
      for k in range(len(table.liste_colonnes)):
         table.liste_colonnes[k].liste_valeurs = RES[k]
      return table
         
