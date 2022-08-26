# Acest fisier deserveste ca un module cu trei functii definite: calcularea sumei elementelor unei liste, calcularea produsului elementelor unei liste
# si un generator de numere care functioneaza pana in parametrul setat la apelarea functiei.

import random       # random este si el un module built-in


def suma(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

def produs(a):
    factor = 1
    for i in a:
        factor = factor * i
    return factor

def num_generator(a):
    return random.randint(1, a)
