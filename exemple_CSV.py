# utiliser csv
import os
import csv

# on travaillera dans un dossier qu'on choisira
base_chemin = "W:/essai"
os.chdir(base_chemin)
# avec un fichier du nom suivant
csv_chemin = "test.csv"

# écrire un fichier csv
with open(csv_chemin, mode='w', newline='') as csv_file :
    csv_writer = csv.writer(csv_file,delimiter=';')

    csv_writer.writerow(['Truc', 'Machin'])
    csv_writer.writerow(['Bidule','MachinChose'])

# lire un fichier csv
with open(csv_chemin, mode='r', newline='') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=';')

    for ligne in csv_reader :
        print(ligne)

# commentaire ajouté inutile
