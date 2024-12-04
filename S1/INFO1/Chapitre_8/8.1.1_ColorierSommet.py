from bibgraphes import *

graph = ouvrirGraphe("tgv2005.dot")

def colorierGraphe(graph, p, c):
    p = sommetNom(graph, p)
    colorierSommet(p, c)

colorierGraphe(graph, "Paris", "green")
colorierGraphe(graph, "Bordeaux", "blue")
afficherGraphe(graph)
