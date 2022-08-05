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







