a = [1, 2, 3, 4, 5]
print(len(a)) #len = functie ce imi afiseaza lungimea unei liste/string

a = [1, 2, 3, 4, 5]
for i in range(len(a)):     
    print(i)


a = [1, 2, 3, 4, 5]
suma = 0
for i in range(len(a)):
    suma = suma + a[i]
print(suma)
