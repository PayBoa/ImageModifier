from PIL import Image

image = Image.open("logo0.png").convert("RGBA")
pixels = image.load()

ancienne_couleur = (0, 0, 0, 255)  # REMPLIR
nouvelle_couleur = (255, 255, 255, 255)  # REMPLIR

largeur, hauteur = image.size
for x in range(largeur):
    for y in range(hauteur):
        if pixels[x, y] == ancienne_couleur: 
            pixels[x, y] = nouvelle_couleur 

image.save("logo1.png")
print("Image modifiée et sauvegardée!")


