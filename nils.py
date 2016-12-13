import os
import csv

csv_chemin = "Q:\Espace d'échange\Mini projets ISN\mp1-2-access"
os.chdir(csv_chemin)
csv_nom = "nils.csv"
with open(csv_nom, mode='r', newline='') as csv_file :
   csv_reader = csv.reader(csv_file,delimiter=';')
   for line in csv_reader :
       print(line)

def lit_horodatage():
    #Lit le fichier d'horodatage et renvoie une liste de liste
    horodatage = []
    with open("nils.csv", mode='r', newline='') as csv_file :
       csv_reader = csv.reader(csv_file,delimiter=';')
       for ligne in csv_reader :
           horodatage.append(ligne)
    horodatage.pop(0)
    return horodatage


def ajoute_horodatage(horodatage, code, nom, prenom):
    import time
    temps=time.strftime('%d/%m/%y %H:%M',time.localtime())
    horodatage.append([code,nom,prenom,temps])



