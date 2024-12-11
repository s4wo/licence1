def existeCouleur(G: graphe, c: str):
    resultat = False
    for x in listeSommets(G):
        if couleurSommet(x) == c:
            return True
    return resultat
        
print(existeCouleur(G, c))
