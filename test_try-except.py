# In PYTHON exista un block numit TRY/EXCEPT. Acest block este folosit pentru a proteja codul de erori.
# In exemplul de mai jos se regasesc doua erori: 
# 1. impartirea la zero (ZeroDivisionError)
# 2. nerespectarea conditiei "int" (ValueError)
# Chiar daca acest cod contine erori, in terminal vor fi afisate doar string-urile care se afla in blockul de except.
# REMINDER: Daca doresti "sa prinzi" diverse erori, in blockul de expect trebuie specificata eroarea exacta!
try: 
    value = 10 / 0
    numar = int(input("Introdu un numar: "))
    print(numar)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input")
