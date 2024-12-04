from bibgraphes import *

G = ouvrirGraphe("tgv2005.dot")

def degreeMax(G):
    ville = ""
    nbMax = 0
    for a in listeSommets(G):
        if degre(a) > nbMax:
            nbMax = degre(a)
            ville = nomSommet(a)
    return ville, nbMax

print(degreeMax(G))

degre


