from bibgraphes import *

graph = ouvrirGraphe("tgv2005.dot")

def toutColorier(graph, c):
    for a in listeSommets(graph):
        colorierSommet(a, c)

toutColorier(graph, "white")
afficherGraphe(graph)
