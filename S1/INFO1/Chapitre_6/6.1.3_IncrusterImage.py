from bibimages import *

fond = ouvrirImage("road.jpg")
avantPlan = ouvrirImage("personnage.png")
dx = 150
dy = 150

def IncrusterImage(avantPlan, fond, dx: int, dy: int):
    L = largeurImage(fond)
    H = hauteurImage(fond)
    l = largeurImage(avantPlan)
    h = hauteurImage(avantPlan)
    for y in range(h):
        for x in range(l):
            (r, g, b) = couleurPixel(avantPlan, x, y)
            if (r, g, b) != (0, 255, 0):
                if 0 < x+dx < L and 0 < y+dy < H:
                    colorierPixel(fond, x+dx, y+dy, (r, g, b))
                
IncrusterImage(avantPlan, fond, dx, dy)
afficherImage(fond)
