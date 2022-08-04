def functie(x):  # x = lista care ma ajuta sa definesc functia. Atentie! x = Orice alta "()" definita mai tarziu in cod.
    suma = 0  # In calcularea sumei, 0 nu va interveni cu absolut nimic.
    for numar in range(len(x)): # Daca len(x) = 5, atunci range(len(x)) poate lua 5 valori, si anume: [0, 1, 2, 3, 4]
        suma = suma + x[numar]
    return suma # Return - intoarce suma (daca se afla in afara for-ului, cum este si aici).

suma_intoarsa = functie([1, 2, 3])
print(suma_intoarsa)

# f(x) = x + 3 => intoarce valoarea lui x + 3
# rezultat = f(1) = 4

# def functie2(x):
    # return x + 3

# print(functie2(2))

# print(sum([1, 2, 3, 4, 5]))