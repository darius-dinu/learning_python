# # 1. Write a Python function to find the Max of three numbers.

# def f(x):
#     max = x[0]
#     for numar in x:
#         if numar > max:
#             max = numar
#     return max

# lista = f([300, 400, 100])
# print(lista)





# # 2. Write a Python function to sum all the numbers in a list.

# def suma(x):
#     sum = 0
#     for numar in x:
#         sum = sum + numar
#     return sum
# lista = suma([8, 2, 3, 0, 7])
# print(lista)



# # 3. Write a Python function to multiply all the numbers in a list.

# def multiply(x):
#     produs = 1
#     for numar in x:
#         produs = produs * numar
#     return produs
# lista = multiply([8, 2, 3, -1, 7])
# print(lista)


# # 4. Write a Python program to reverse a string

# def functie(x):
#     return x[::-1]
# string = functie("1234abcd")
# print(string)


# # 5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# def functie(x):
#     count1 = 0
#     count2 = 0
#     for numar in x:
#         if(numar.isupper()):
#             count1 = count1 + 1
#         elif(numar.islower()):
#             count2 = count2 + 1
#         else:
#             pass
#     return count1, count2

# count1, count2 = functie("The quick Brown Fox")
# print("The number of upper case letters is: " + str(count1))
# print("The number of lower case letters is: " + str(count2))



# # 6. Write a Python program to check a list is empty or not.

# a = [1]
# if len(a) > 0:
#     print("The list isn't empty")
# else:
#     print("The list is empty.")


# # 7. Write a Python function that takes two lists and returns True if they have at least one common member.

# def functie(x, y):
#     intors = False
#     for numar in x:
#         for numar2 in y:
#             if numar == numar2:
#                 intors = True
#                 break
#     return intors

# liste = functie([1, 2, 3, 4], [4, 5, 6, 7])
# print(liste) 
            

# # 8. Write a program to find how many times substring “Emma” appears in the given string.

# # 8.A. Varianta relativa CPP:
# str_x = "Emmaa is a goEmmaod developer. Emma is a writer."
# a = str_x.split(" ")
# b = 0
# for nume in a:
#     if "Emma" in nume:
#         b = b + 1
# print(b)



# # 8.B. The Pythonic way:
# str_x = "Emmaa is a goEmmaod developer. Emma is a writer."
# a = str_x.count("Emma")
# print(a)





# # 9. Given two lists of numbers, write a program to create a new list. The new list should contain odd numbers from the first list and even numbers from the second list.

# # 9.A. Varianta clasica (doua for-uri):
# a = [10, 20, 25, 30, 35]
# b = [40, 45, 60, 75, 90]
# lista = []
# for numar in a:
#     if numar % 2 == 1:
#         lista.append(numar)
# for numar2 in b:
#     if numar2 % 2 == 0:
#         lista.append(numar2)

# print(lista)





# # 9.B. Varianta simpla:
# a = [10, 20, 25, 30, 35]
# b = [40, 45, 60, 75, 90]
# lista = []
# for numar in range(len(a)):
#     if a[numar] % 2 == 1:
#         lista.append(a[numar])
#     if b[numar] % 2 == 0:
#         lista.append(b[numar])

# print(lista)



# # 10. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# # a = [10, 20, 30, 40, 10] - prima lista cu care apelez functia
# # b = [75, 65, 35, 75, 30] - a doua lista cu care apelez functia
# def functie(a):
#     if a[0] == a[-1]:
#         return True
#     else:
#         return False

# lista = functie([10, 20, 30, 40, 10])
# print(lista)





# # 11. Write a Python function that takes a list and returns a new list with unique elements of the first list.

# def functie(x):
#     lista1 = []
#     for numar in x:
#         if numar not in lista1:
#             lista1.append(numar)
#     return lista1

# lista2 = functie([1, 2, 3, 3, 3, 3, 4, 5])
# print(lista2)



# 12. Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
    # Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    if exp > 0:   
        a = base ** exp
        return int(a)
    else:
        return "Your result isn't a whole number"

print(exponent(2, 3))