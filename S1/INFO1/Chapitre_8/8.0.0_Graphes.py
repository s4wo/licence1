from bibgraphes import *

graph = ouvrirGraphe("tgv2005.dot")

def existeGare(graphe, nomGare):
    for s in listeSommets(graphe):
        if nomSommet(s)==nomGare: 
            return True
    return False


print(existeGare(graph,"Paris"))
print(existeGare(graph, "Nice"))
