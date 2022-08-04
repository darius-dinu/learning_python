def functie(x, y):
    lista = []
    for number in x:
        if number % y == 0:
            lista.append(number + y)    # Comanda ".append" adauga ce se afla intre "()"
        else:
            lista.append(number - y)
    return lista

lista = functie([1, 2, 3, 7], 2)
print(lista)



def functie(x):
    sum = 0
    for numar in x:
        sum = numar + sum
    return sum    

lista = functie([1, 2, 3])
print(lista)