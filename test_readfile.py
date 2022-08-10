file = open("readfile.txt", "r")        # Open primeste doi parametri: numele fisierului (+ extensie) si comanda de executat ("r", "w", "a", "r+")
for cuvant in file.readlines(): # file.readlines() - transforma fiecare rand intr-un element al unei liste.
    print(cuvant)

file.close() # Este un bun-practice sa inchizi fisiere dupa ce le deschizi.


fisier = open("readfile.txt", "a")
fisier.write("\nHavana, havana, sud americanca")
fisier.write("\nNicusor de la braila")
fisier.close()