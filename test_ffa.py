def functie(x):  # x = lista cu care definesc functia
    suma = 0
    for numar in range(len(x)):
        suma = suma + x[numar]
    return suma

lista = functie([1, 2, 3, 4, 5])
print(lista)
