# import des packages 

from src.table.table import Table
from src.colonne.colonne import Colonne

from src.transformationTableaux.jointure import Jointure
from src.transformationTableaux.trier_croissant import Triercroiss

from src.pipeline.pipeline import Pipeline

from src.transformationStatistique.centrage import Centrage
from src.transformationStatistique.reduire import Reduire
from src.transformationStatistique.centrer_reduire import Centrer_Reduire


from src.indicateursStatistiques.moyenne import Moyenne
from src.indicateursStatistiques.mediane import Mediane
from src.indicateursStatistiques.ecart_type import Ecart_Type
from src.indicateursStatistiques.quartile import Quartile
from src.indicateursStatistiques.variance import Variance
from src.indicateursStatistiques.summary import Summary

from src.coefficients.pearson import Pearson 
from src.coefficients.covariance import Covariance

from src.graphique.boxplot import Boxplot
from src.graphique.camembert import Camembert
from src.graphique.histogramme import Histogramme
from src.graphique.nuage_de_points import Nuage_de_points

#création d'un exemple de table
#Colonne.liste_valeurs peut avoir des variables numériques au texte, cf concstructeur de Colonne
table_exemple_fus1 = Table( "Exemple fusion 1", [Colonne( "id", [1, 2, 3, 4, 5, 6]) , Colonne( "Nom" , ["Pierre", "Paul", "Jacques", "Jean", "Fabienne", "Camille"]), Colonne("Note", ["10","18","8", "15","16", "13"])])
table_exemple_fus2 = Table( "Exemple fusion 2", [Colonne( "id", [3, 5, 7, 8]), Colonne("Classe", [ "a", "b", "a", "c"]) ])

table_exemple = Table ("Exemple bivarié", [Colonne( "id", [1,2,3,4,5,6,7,8,9,10]), Colonne("Taille", [ 180, 170, 175, 163, 159, 187, 192, 180, 168, 179]) , Colonne("poids", [80, 65, 70, 59,  62, 89, 101, 83, 65, 90]) ] )


Pipeline.appliquer( table_exemple_fus1, [Jointure.transformer, Table.exporter], [[table_exemple_fus2, "id"], ["data/output/", "exemple fusion"]])

#Pipeline.appliquer( table_exemple, [Jointure.transformer, Table.exporter], [[table_exemple, "id"], ["data/données/", "exemple fusion"]])

