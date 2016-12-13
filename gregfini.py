from PIL import Image
code = input("Entrez votre code")
lien = "Q:/Espace d'échange/Mini projets ISN/mp1-2-access/" + code + ".jpg"
affichage = Image.open(lien)
affichage.show()