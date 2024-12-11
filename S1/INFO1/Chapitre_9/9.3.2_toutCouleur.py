def toutCouleur(G: graphe, c: str):
    resultat = True
    for x in listeSommets(G):
        if couleurSommet(x) != c:
            resultat = False
    return resultat

print(toutCouleur(G,c))
