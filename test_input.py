a = input("Adauga numele tau: ") #Asta este un input. Input-urile sunt datele de intrare care trebuiesc introduse din terminal. 
b = input("Adauga prenumele tau: ") #Asta este al doilea input.

print("Numele tau este: " + a + " " + b ) #Asta este afisarea prin print. Atentie! Space trebuie introdus printr-un string separat intre paranteze


a = input("Adauga primul numar: ")
b = input("Adauga al doilea numar: ")
if int(a) > int(b):   #If = Daca. Dupa If trebuie o CONDITIE. Int = Numar intreg ce apartine intervalului [-32768; 32768]
    print(a)
    b = 100
else:   #else = Daca nu se respecta conditia IF, atunci codul va rula din else.
    print(b)
print (b)