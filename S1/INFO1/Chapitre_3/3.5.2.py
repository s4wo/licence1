def estDiviseur(i: int,n: int):
    return n % i == 0
         
# print(estDiviseur(4,8))

# 1,3,5,7,11,13

def estPremier(p):
    for elt in range(2,p):
        if estDiviseur(elt,p):   
            return False
    return True

print(estPremier(55598))
