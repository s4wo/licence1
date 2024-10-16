L = [-5,2,9,-5,9,-7]


def maximumListe(L: list):
    s = L[1]
    for elt in L: 
        if elt > s:
            s = elt
    return s

print(f"La valeur maximum de la liste est {maximumListe(L)}.")
