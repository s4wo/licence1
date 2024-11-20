#!/usr/bin/env python3
from bibimages import * 

img1 = ouvrirImage("ocean.png")
img2 = ouvrirImage("road2.jpg")

L1 = largeurImage(img1)
H1 = hauteurImage(img1)
L2 = largeurImage(img2)
H2 = hauteurImage(img2)

img3 = nouvelleImage(L1, H1)

def moyenneCouleurPixel(p1, p2): 
    (r1,g1,b1) = p1
    (r2,g2,b2) = p2
    return (r1+r2//2),(g1+g2//2),(b1+b2//2)

def fusion(img1, img2, img3): 
    for x in range(largeurImage(img1)):
        for y in range(hauteurImage(img1)):
            p1 = couleurPixel(img1, x, y)
            p2 = couleurPixel(img2, x, y)
            colorierPixel(img3, x, y, moyenneCouleurPixel(p1,p2))
    return img3
            
fusion(img1, img2, img3)
afficherImage(img3)
