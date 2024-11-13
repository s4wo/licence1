from bibimages import *

fond = ouvrirImage("road.jpg")
avantPlan = ouvrirImage("personnage.png")

def copieCoinImage(avantPlan, fond):
    L = largeurImage(fond)
    H = hauteurImage(fond)
    l = largeurImage(avantPlan)
    h = hauteurImage(avantPlan)
    for y in range(h):
        for x in range(l):
            (r, g, b) = couleurPixel(avantPlan, x, y)
            if (r, g, b) != (0, 255, 0):
                colorierPixel(fond, x, y, (r, g, b))
                
copieCoinImage(avantPlan, fond)
afficherImage(fond)
