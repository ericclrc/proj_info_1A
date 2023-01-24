import gzip
import json 
import csv
import numpy as np

from src.colonne.colonne import Colonne

class Table:

    """ Modélise une table de données

    Attributes
    -------
    nom_table : str
        nom de la table

    liste_colonnes : list
        liste d'instances de la classe Colonne
    """

    def __init__(self, nom_table, liste_colonnes):
        self.nom_table = nom_table
        self.liste_colonnes = liste_colonnes
    
    def selectionner_colonne_par_nom(self, nom_colonne):
        """ renvoie une colonne de la table
        On fait ici l'hypothèse que le nom d'une colonne est unique dans la table
        Paramètres:
        ----
        nom_colonne : str
            nom de la colonne que l'on souyhaite retouner

        Renvoi:

        colonne : Colonne 
            instance de la classe Colonne, avec le nom spécifié en paramètre
        """
        for colonne in self.liste_colonnes:
            if colonne.nom_colonne == nom_colonne:
                return colonne


    def exporter(self, chemin, nom_fichier):
        """
        exporte une instance de la classe Table dans un fichier csv placé dans le dossier output 
        
        Parameters:
        -----
        Table : Table
            L'instance de table à exporter
        chemin : str
            chemin vers l'endroit où l'on veut enregister la table
            
        nom_fichier : str
            nom du fichier de l'export
        
        """
        table_copie = [[]]

        for colonne in self.liste_colonnes:
            table_copie[0].append(colonne.nom_colonne)


        for i in range(len(self.liste_colonnes[0].liste_valeurs)): #on parcourt une colonne ' de haut en bas'
            ligne = []
            for j in range(len(self.liste_colonnes)): # on parcourt les colonnes
                ligne.append(str(self.liste_colonnes[j].liste_valeurs[i])) #on crée la ligne 
            table_copie.append(ligne)
        table_export = np.asarray(table_copie)

        np.savetxt( chemin + nom_fichier + '.csv' , table_export, fmt='%s', delimiter = ";")
        
       
    
    def importer_table(extension, chemin, nom_fichier, nom_tableau):
        """
        Paramètres :
        ----
        extension : str
            extension du fichier contenant la table à ouvrir 
            seules les extensions "csv", "csv.gz" et "json.gz" ont supportées

        chemin : str
            chemin vers l'endroit d'où l'on veut importer la table
            
        nom_fichier : str
            nom de la table à importer ( les fichiers doivent être compressés et se finir par "extension.gz")
            
         nom_table : str
            nom à donner à la table 

        Retourne:
        ----
        Une instance de la classe Table
        """

        if extension == "json.gz":

            with gzip.open( chemin + nom_fichier, mode='rt') as gzfile :
                liste_dict = json.load(gzfile)
            data = []
            
            liste_variables = []
            for dico in liste_dict: #on parcourt les dictionnaire pour avoir toutes les variables du tableau
                variables_test = dict.keys(dico['fields'])
                if len(variables_test) > len(liste_variables): #dico a plus de clés, donc plus de colonnes
                    liste_variables = variables_test # on a toutes les colonnes du tableau
            
            for variable in liste_variables: #on parcourt les colonnes
                liste_valeurs = [] # valeurs de la colonne
                for dico in liste_dict: #on parcourt les dicos
                    if variable in dico['fields']: # si la colonne est bien dans le dico, on a bien une valeur
                        liste_valeurs.append(dico['fields'][variable])
                    else: # sinon valeur manquante
                        liste_valeurs.append('mq')
                data.append(Colonne(variable, liste_valeurs))
            
            return Table(nom_tableau, data )

        if extension == "csv.gz":
            data = []
            with gzip.open(chemin + nom_fichier, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';') 
                for row in synopreader :
                    data.append(row)

            liste_colonnes = []

            for j in range(len(data[0])): #pour chaque colonne
                liste_valeurs = []
                for i in range(1,len(data)): #pour chaque ligne sauf la première qui contient les noms des colonnes 
                    liste_valeurs.append(data[i][j]) #on créee la j-e colonne 
                liste_colonnes.append(Colonne(data[0][j], liste_valeurs))#on crée une instance de Colonne  
            return Table(nom_tableau, liste_colonnes)
        
        if extension == "csv":
            data = []
            with open(chemin + nom_fichier, mode='rt') as csvfile :
                reader_variable = csv.reader(csvfile, delimiter=';') 
                for row in reader_variable :
                    data.append(row)

            liste_colonnes = []

            for j in range(len(data[0])): #pour chaque colonne
                liste_valeurs = []
                for i in range(1,len(data)): #pour chaque ligne sauf la première qui contient les noms des colonnes 
                    liste_valeurs.append(data[i][j]) #on créee la j-e colonne 
                liste_colonnes.append(Colonne(data[0][j], liste_valeurs))#on crée une instance de Colonne  
            return Table(nom_tableau, liste_colonnes)


        if extension not in ["csv", "csv.gz", "json.gz"]:
            raise ValueError("Extension du fichier non supportée")

