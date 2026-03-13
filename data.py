""" Module de chargement de donnees - calculatrice ."""
2
3 import csv
4 import os
5
6
7 def load_csv ( filepath : str) -> list [ dict ]:
8 """
9 Charge un fichier CSV et retourne une liste de dictionnaires .
10
11 Args :
12 filepath : Chemin vers le fichier CSV
13
14 Returns :
15 Liste de dictionnaires (une entree par ligne )
16
17 Raises :
18 FileNotFoundError : si le fichier n’existe pas
19 ValueError : si le fichier est vide
20 """
21 if not os. path . exists ( filepath ):
22 raise FileNotFoundError (f" Fichier introuvable : { filepath }")
23
24 with open ( filepath , "r", encoding ="utf -8") as f:
25 reader = csv . DictReader (f)
26 data = list ( reader )
27
28 if not data :
29 raise ValueError ("Le fichier CSV est vide .")
30
31 return data
32
33
34 def save_csv ( filepath : str , data : list [ dict ]) -> None :
35 """
36 Sauvegarde une liste de dictionnaires dans un fichier CSV .
37
38 Args :
39 filepath : Chemin de destination
40 data : Donnees a ecrire ( liste de dicts avec memes cles )
41 """
42 if not data :
43 raise ValueError (" Aucune donnee a sauvegarder .")
44
45 fieldnames = data [0]. keys ()
46 with open ( filepath , "w", newline ="", encoding ="utf -8") as f:
47 writer = csv . DictWriter (f, fieldnames = fieldnames )
48 writer . writeheader ()
49 writer . writerows ( data )
P