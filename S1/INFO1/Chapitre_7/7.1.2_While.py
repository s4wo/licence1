def mystere ( n : int ):
    s = 0
    while n > 0 :
        s = s + ( n % 10)  # Reste de la division par 10
        n = n // 10 # n devient l'entier de la division euclidienne par 10 
    return s

def nombreDeChiffres(n: int):
    s = 0 
    while n > 0:
        s = s + 1
        n = n // 10
    return s

def plusGrandChiffre(n: int):
    s = 0
    while n > 0: 
        d = n % 10
        if d > s:
            s = d
        n = n // 10
    return s
        
