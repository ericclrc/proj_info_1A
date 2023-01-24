class Colonne:
    """
    Modélise les colonnes d'une table

    Attributes
    -----
    liste_valeurs : list
        liste contenant les entrées de la colonne
    
    nom_colonne : str
        nom de la colonne

    """

    def __init__(self, nom_colonne = "sans nom", liste_valeurs = []):
        self.nom_colonne = nom_colonne
        liste_valeurs_num = []
        for k in range(len(liste_valeurs)):
            try:
                float( liste_valeurs[k])
                liste_valeurs_num.append(float(liste_valeurs[k]))
            except:
                liste_valeurs_num.append(liste_valeurs[k])
        self.liste_valeurs = liste_valeurs_num
            

    def nb_valeurs_manquantes(self):

        """" renvoie le nombre de valeurs manquantes dans la colonne
        
        renvoi : un entier 
        
        """
        compteur = 0
        for valeur in self.liste_valeurs :
            if valeur == 'mq':
                compteur += 1
        return compteur 