from PIL import Image

# Charger l'image
image = Image.open("logo0.png").convert("RGBA")  # Utilisation du mode RGBA pour les images avec transparence
pixels = image.load()

# Couleur à modifier (ancienne) et couleur de remplacement (nouvelle)
ancienne_couleur = (0, 0, 0, 255)  # Rouge pur avec opacité complète (RGBA)
nouvelle_couleur = (0, 71, 71, 255)  # Vert pur avec opacité complète (RGBA)

# Parcourir tous les pixels et modifier la couleur
largeur, hauteur = image.size
for x in range(largeur):
    for y in range(hauteur):
        if pixels[x, y] == ancienne_couleur:  # Vérifie si le pixel correspond à l'ancienne couleur
            pixels[x, y] = nouvelle_couleur  # Remplace par la nouvelle couleur

# Sauvegarder l'image modifiée
image.save("logo1.png")
print("Image modifiée et sauvegardée!")


