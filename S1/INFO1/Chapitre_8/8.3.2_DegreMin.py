from bibgraphes import *

G = ouvrirGraphe("tgv2005.dot")

def degreMin(G):
    ville = ""
    nbMin = degre(listeSommets(G)[0])
    for a in listeSommets(G):
        if degre(a) < nbMin:
            nbMin = degre(a)
            ville = nomSommet(a)
    return ville, nbMin
 
print(degreMin(G))
