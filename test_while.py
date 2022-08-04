i = 10   
while i > 0:   # Expresie echivalenta cu "Cat timp i > 0,
    print(i) # atunci afiseaza i"
    i = i - 1   # Decrementez valoarea unui numar, astfel incat sa pot parcurge toate valorile pe care le poate lua i-ul.



a = [1, 2, 3] # Pornesc de la o lista
sum = 0 # Daca sum = 0, atunci nu se va interveni
numar = 0 # Variabila ce ma ajuta sa trec prin toata lista folosind while
while numar < len(a):  # len(a) este folosit pentru a ma asigura ca nu depasesc elementele listei.
    sum = sum + a[numar] #Adaug rand pe rand termenii la suma
    numar = numar + 1 #Incrementez valoarea unui numar, astfel incat sa pot parcurge toata lista pana la len(a)
print(sum)



a = [12, 23, 3, 4, 5, 6, 7]  # Pornesc de la o lista
sum = 0   # Daca sum = 0, atunci nu se va interveni
numar = 0 # Variabila ce ma ajuta sa trec prin toata lista folosind while
while numar < len(a): # len(a) este folosit pentru a ma asigura ca nu depasesc elementele listei.
    if numar % 3 == 0: # Conditia care imi pune termenii in suma, in acest caz, cei care au indexii divizibili cu 3(si anume: 0, 3, 6)
        sum = sum + a[numar] #Adaug rand pe rand termenii la suma
    numar = numar + 1   # Incrementez valoarea unui numar, astfel incat sa pot parcurge toata lista pana la len(a)
    
print(sum)




a = [1, 2, 3, 4, 5]
produs = 1
numar = 0
while numar < len(a):
    produs = produs * a[numar]
    numar = numar + 1
print(produs)