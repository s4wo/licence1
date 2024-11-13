from bibimages import *

img = ouvrirImage("teapot.png")

def Monochrome(img):
    L = largeurImage(img)
    H = hauteurImage(img)
    for y in range(H):
        for x in range(L):
            (r, g, b) = couleurPixel(img, x, y)
            lum = int(r*0.3+g*0.59+b*0.11)
            colorierPixel(img, x, y, (lum,lum,lum))
            
Monochrome(img)
afficherImage(img)
