
from src.colonne.colonne import Colonne
from src.transformationTableaux.trier_croissant import Triercroiss
from src.table.table import Table
from numpy import sort


class Jointure:

    def transformer( table1, table2, nom_clé_primaire):
        """ Fusion entre deux instances de Table selon une clé primaire
        On fait ici l'hypothèse que la clé primaire est constituée d'une seule colonne dont le nom est nom_clé_primaire
        l'équivalent de jointure(table1, table2, nom_clé_primaire) en SQL serait table1 FULL JOIN table2 ON clé
        
        Parameters:
        ---
        table1 : Table
            instance de la classe Table 
        
        table2 : Table
            instance de la classe Table
        
        nom_clé_primaire : str
            nom de la colonne servant de clé primaire à la fusion 
        """



        table1 = Triercroiss.transformer(table1, nom_clé_primaire)
        table2 =Triercroiss.transformer(table2, nom_clé_primaire)

        
        compteur_id_table_1 = 0
        compteur_id_table_2 = 0

        liste_nom_colonnes = []
        
        for colonne in table1.liste_colonnes:
            liste_nom_colonnes.append(colonne.nom_colonne)
            
        
        for colonne in table2.liste_colonnes:
            flag = 0 # le nom de colonne n'est pas dans la liste par défaut
            for nom in liste_nom_colonnes:

                if colonne.nom_colonne == nom : #  le nom est déjà  dans la liste
                    flag = 1
            if flag == 0:
                liste_nom_colonnes.append(colonne.nom_colonne)
        

        # on a une liste des noms des colonnes de table1 et de table2 sans doublons
    
        for colonne1 in table1.liste_colonnes: #on repère la colonne de la clé primaire dans table1
            if colonne1.nom_colonne == nom_clé_primaire :
                clé_primaire_1 = colonne1
        liste_id1 = clé_primaire_1.liste_valeurs

        liste_id = liste_id1.copy()
        
        for colonne2 in table2.liste_colonnes: # pareil dans table 2
            if colonne2.nom_colonne == nom_clé_primaire :
                clé_primaire_2 = colonne2
        
        liste_id2 = clé_primaire_2.liste_valeurs

        for id2 in liste_id2: #on retire les doublons 
            flag = 0 #id2 n'est pas déjà dans la liste
            for id1 in liste_id:
                if id2 == id1: # doublon
                    flag = 1
            if flag == 0: 
                liste_id.append(id2)
        
        data_fusion = []
        for nom in liste_nom_colonnes: #on crée une table avec seulement des valeurs manquantes
            colonne = []
            for k in range(len(liste_id)):
                colonne.append('mq')
            data_fusion.append(Colonne( nom, colonne))
        

        Table_fusion = Table( " table_fusion", data_fusion) #table de seulement des colonnes de valeurs manquantes 
        longueur_table1 = len(table1.liste_colonnes)
        
        #liste_id contient toutes les lignes des clés primaires pour table1 et table2
        
        sort(liste_id) # on trie les id 
        
        for id_tot in liste_id : # on parcourt tout les id 
            
            if id_tot == liste_id1[compteur_id_table_1]:
                place_id_tot = 0
                for k in range(len(liste_id)):
                    if liste_id[k] == id_tot:
                        place_id_tot = k 

                for k in range(longueur_table1): #on parcourt les colonnes de Table_fusion qui sont dans table1 par construction
                    Table_fusion.liste_colonnes[k].liste_valeurs[place_id_tot] = table1.liste_colonnes[k].liste_valeurs[compteur_id_table_1] 
                if compteur_id_table_1 < len( liste_id1) - 1:        
                    compteur_id_table_1 += 1 #on a traité la ligne 1 du tableau 1

            if id_tot == liste_id2[compteur_id_table_2]:
                place_id_tot = 0
                for k in range(len(liste_id)):
                    if liste_id[k] == id_tot:
                        place_id_tot = k 

                for colonne in Table_fusion.liste_colonnes: # partie droite du tableau correspondant à table2 sans doublons
                    for colonne2 in table2.liste_colonnes:
                        if colonne.nom_colonne == colonne2.nom_colonne: # on repère la bonne colonne dans table2
                            colonne.liste_valeurs[place_id_tot] = colonne2.liste_valeurs[compteur_id_table_2]
                if compteur_id_table_2 < len ( liste_id2) - 1 :
                    compteur_id_table_2 += 1
                    
        
        return Table_fusion
