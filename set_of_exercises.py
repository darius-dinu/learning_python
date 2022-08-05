# 1. Write a Python function to find the Max of three numbers.

def f(x):
    max = x[0]
    for numar in x:
        if numar > max:
            max = numar
    return max

lista = f([300, 400, 100])
print(lista)





# 2. Write a Python function to sum all the numbers in a list.

def suma(x):
    sum = 0
    for numar in x:
        sum = sum + numar
    return sum
lista = suma([8, 2, 3, 0, 7])
print(lista)



# 3. Write a Python function to multiply all the numbers in a list.

def multiply(x):
    produs = 1
    for numar in x:
        produs = produs * numar
    return produs
lista = multiply([8, 2, 3, -1, 7])
print(lista)


# 4. Write a Python program to reverse a string

def functie(x):
    return x[::-1]
string = functie("1234abcd")
print(string)


# 5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def functie(x):
    count1 = 0
    count2 = 0
    for numar in x:
        if(numar.isupper()):
            count1 = count1 + 1
        elif(numar.islower()):
            count2 = count2 + 1
        else:
            pass
    return count1, count2

count1, count2 = functie("The quick Brown Fox")
print("The number of upper case letters is: " + str(count1))
print("The number of lower case letters is: " + str(count2))



# 6. Write a Python program to check a list is empty or not.

a = [1]
if len(a) > 0:
    print("The list isn't empty")
else:
    print("The list is empty.")


# 7. Write a Python function that takes two lists and returns True if they have at least one common member.

def functie(x, y):
    intors = False
    for numar in x:
        for numar2 in y:
            if numar == numar2:
                intors = True
                break
    return intors
liste = functie([1, 2, 3, 4], [4, 5, 6, 7])
print(liste) 
            

