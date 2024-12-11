def contientDuBlanc(img: image, c):
    resultat = True
    for x in range(largeurImage(img)):
        for y in range(hauteurImage(img)):
            if couleurPixel(img, x, y) != c:
                resultat = False
    return resultat

print(contientDuBlanc(img, c))
