# Créé par lefort, le 28/11/2016 en Python 3.2
import os
import csv
from PIL import Image
csv_chemin = "Q:/Espace d'échange/Mini projets ISN/mp1-2-access"
compteur = 0
bibli=[]
acces = 0
os.chdir(csv_chemin)
rfid = input("Passez votre badge RFID :")
csv_nom = "bibli.csv"
with open(csv_nom, mode='r', newline='') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=';')
    for line in csv_reader :
        bibli.append(line)
bibli.pop(0)

present = 0

for ligne in bibli:
    if ligne[0] == rfid:
        present = 1
        lien = "Q:/Espace d'échange/Mini projets ISN/mp1-2-access/" + rfid + ".jpg"
        affichage = Image.open(lien)
        affichage.show()
        if ligne[3] == '1':
            print("Tu peux rentrer")
        else:
            print("Tu ne peux pas rentrer")
if present == 0:
    print("Vous n'existez pas dans la base de données.")



























