 from bibgraphes import *

graph = ouvrirGraphe("tgv2005.dot")

def colorSummit(graph, v, c):
    v = sommetNom(graph, v)
    colorierSommet(v, c)

colorSummit(graph, "Paris", "red")

def nbSommetsCouleur(graph, c):
    x = 0
    for a in listeSommets(graph): 
        if couleurSommet(a) == c:
            x = x + 1
    return x

print(nbSommetsCouleur(graph, "white"))

def nbSommetsColores(graph):
    x = 0
    for a in listeSommets(graph): 
        if couleurSommet(a) != "white":
            x = x + 1
    return x

print(nbSommetsColores(graph))

afficherGraphe(graph)
