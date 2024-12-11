def pasDeCouleur(img: image):
    resultat = True 
    for x in range(largeurImage(img)):
        for y in range(hauteurImage(img)):
            (r,g,b) = couleurPixel(img, x, y)
            if r!=g or r!=b :
                resultat = False
    return resultat
