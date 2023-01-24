from src.coefficients.coefficients import Coefficients
from src.indicateursStatistiques.moyenne import Moyenne
from src.colonne.colonne import Colonne
from src.coefficients.coefficients import Coefficients

class Covariance(Coefficients):

     def calculer(table, nom_colonne1, nom_colonne2):
        """
        Paramètres:
        
        table : Table
        
        nom_colonne1 : str
        
        nom_colonne2: str
        """
        

        valeurs = Coefficients.valeurs_calcul_possibles( table, nom_colonne1, nom_colonne2)
        
        liste_valeurs_1 = valeurs[0]
        liste_valeurs_2 = valeurs[1] 

        N = len(liste_valeurs_1)
        somme = 0
        somme1 = 0
        somme2 = 0
        for valeur in liste_valeurs_1:
            somme1 += valeur
        for valeur in liste_valeurs_2:
            somme2 += valeur

        moy_1 = somme1/N        
        moy_2 = somme2/N

        for k in range(N):
            somme += (liste_valeurs_1[k] - moy_1) * (liste_valeurs_2[k] - moy_2)
        if valeurs[2] != 0:
            print( " Attention, valeurs manquantes. Calcul effectué avec " + str(valeurs[2]) + " valeurs manquantes")
        
        print( "Covariance : " + str(somme/N))
        return somme/N 

        
