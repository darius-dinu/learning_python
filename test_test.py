# O functie care sa primeasca ca argumente doua numere, returneaza pe primul daca mai mare decat al doilea, pe al doilea mai mare ca primul sau media geometrica, daca sunt egale.

import math


def functie(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return math.sqrt(a * b)
    
# nebunie = functie(4, 3)
# print(nebunie)



def f(a, b):
    if a > b:
        return a* b
    else:
        return functie(a, b)

nebunie = f(7, 7)
print(nebunie)





# O functie care primeste doi parametrii
# Cat timp parametrul 1 e mai mare decat al doilea
# afisam valoarea primului parametru
# decrementam valoarea parametrului 1 pana cele doua ajung egale
# cand ajungem in acest punct iesim din bucla cu break

def g(a, b):
    while a > b:
        print(a)
        a = a - 1
        if a == b:
            break
    
g(9, 7)


#First itteration: a = 9, a > b, afiseaza 9, decrementeaza cu 1, a = 8, continue
#Second itteration: a = 8, a > b, afiseaza 8, decrementeaza cu 1, a = 7, a = b, stop.