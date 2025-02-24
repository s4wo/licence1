#Ex1.0

a = 2+(1/2)
b = 2+(1/a)
c = 2+(1/b)
s2 = 1+(1/c)

print(s2) 

#Ex1.1

x = 1-2j ; y = 1+2j
a = x.real 
b = x.imag
c = y.real 
d = y.imag


print(x/y)

print(a,b,c,d)

z = ((a*c + b*d)+(b*c - a*d)*1j)/(c**2 + d**2)

print(z)

# Ex1.3
a = 101
L1 = []
print(L1)

def sumN(a):
    z = 0
    for x in range(a):
        z  = z + x
    return z
        
print(sumN(a))
print(sum(range(a)))

def produit(a):
    z = 1
    for x in range(1,a):
        z  = z * x
    return z

print(produit(a))




