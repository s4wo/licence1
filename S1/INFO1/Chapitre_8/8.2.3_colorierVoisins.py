from bibgraphes import *

graph = ouvrirGraphe("tgv2005.dot")

def colorierVoisins(graph, v, c):
    for a in listeVoisins(sommetNom(graph, v)):
        colorierSommet(a, c)
        
colorierVoisins(graph, "Bordeaux", "green")
afficherGraphe(graph)
