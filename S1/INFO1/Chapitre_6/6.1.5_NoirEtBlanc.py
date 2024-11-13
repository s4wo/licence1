from bibimages import *

img = ouvrirImage("teapot.png")

def NoirEtBlanc(img):
    L = largeurImage(img)
    H = hauteurImage(img)
    for y in range(H):
        for x in range(L):
            (r, g, b) = couleurPixel(img, x, y)
            lum = int(r*0.3+g*0.59+b*0.11)
            if lum > 123:
                colorierPixel(img, x, y, (255,255,255))
            else:
                colorierPixel(img, x, y, (0,0,0))
            
            
NoirEtBlanc(img)
afficherImage(img)
