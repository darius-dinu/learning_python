#How to determine the max nummber out of a set of numbers
a = [1, 2, 3]
max = a[0]
for numar in a:
    if numar > max:
        max = numar
print(max)
    


#How to determine the min number out of a set of numbers
b = [1, 2, 3]
min = b[0]
for numar in b:
    if numar < min:
        min = numar 
print(min)




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


#5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

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
