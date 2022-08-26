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
            

# 8. Write a program to find how many times substring “Emma” appears in the given string.

# 8.A. Varianta relativa CPP:
str_x = "Emmaa is a goEmmaod developer. Emma is a writer."
a = str_x.split(" ")
b = 0
for nume in a:
    if "Emma" in nume:
        b = b + 1
print(b)



# 8.B. The Pythonic way:
str_x = "Emmaa is a goEmmaod developer. Emma is a writer."
a = str_x.count("Emma")
print(a)





# 9. Given two lists of numbers, write a program to create a new list. The new list should contain odd numbers from the first list and even numbers from the second list.

# 9.A. Varianta clasica (doua for-uri):
a = [10, 20, 25, 30, 35]
b = [40, 45, 60, 75, 90]
lista = []
for numar in a:
    if numar % 2 == 1:
        lista.append(numar)
for numar2 in b:
    if numar2 % 2 == 0:
        lista.append(numar2)

print(lista)





# 9.B. Varianta simpla:
a = [10, 20, 25, 30, 35]
b = [40, 45, 60, 75, 90]
lista = []
for numar in range(len(a)):
    if a[numar] % 2 == 1:
        lista.append(a[numar])
    if b[numar] % 2 == 0:
        lista.append(b[numar])

print(lista)



# 10. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# a = [10, 20, 30, 40, 10] - prima lista cu care apelez functia
# b = [75, 65, 35, 75, 30] - a doua lista cu care apelez functia
def functie(a):
    if a[0] == a[-1]:
        return True
    else:
        return False

lista = functie([10, 20, 30, 40, 10])
print(lista)





# 11. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def functie(x):
    lista1 = []
    for numar in x:
        if numar not in lista1:
            lista1.append(numar)
    return lista1

lista2 = functie([1, 2, 3, 3, 3, 3, 4, 5])
print(lista2)



# 12. Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#     Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    if exp > 0:   
        a = base ** exp
        return int(a)
    else:
        return "Your result isn't a whole number"

print(exponent(2, 3))


# 13. Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

def functie(a, b):
    lista = []
    for numar in a:
        if numar in b:
                lista.append(numar)
    return lista

f = functie([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(f)



# 14. Write a program that displays the even numbers between 1-10:
count = 0
for numar in range(1, 10):
    if numar % 2 == 0:
        print(numar)
        count = count + 1
print ("We've got " + str(count) + " even numbers")
                


# 15. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#     We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if weekday == False and vacation == True:
        return True
    elif weekday == True and vacation == False:
        return False
    else:
        return True



# 16. Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    times = 0
    final = ""
    while times < n:
        final = final + str
        times = times + 1
    return final

print(string_times("Hi", 4))



# 17. Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
    Greeting = "Hello " + name + "!"
    return Greeting 

print(hello_name("Darius"))




# 18. Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
    for numar in nums:
        if nums[0] == 6 or nums[-1] == 6:
            return True
    else:
        return False

print(first_last6([1, 2, 6, 4, 5]))


# 19. Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    intors = ""
    for litera in str:
        intors = intors + litera * 2
    return intors

print(double_char("Salut"))

# 20. Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
    count = 0
    for numar in nums:
        if numar % 2 == 0:
            count = count + 1
    return count

print(count_evens([1, 2, 3, 4, 5]))




# 21. Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
    if len(nums) > 0:
        if nums[0] == nums [-1]:
            return True
        else:
            return False
    else:
        return False

print(same_first_last([1, 2, 1]))




# 22. Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
#     Both arrays will be length 1 or more.

def common(a, b):
    if len(a) > 0 and len(b) > 0:   
        if a[0] == b[0]:
            return True
        elif a[-1] == b[-1]:
            return True
        else:
            return False
    else:
        return False

print(common([1, 2, 3], [7, 3]))




# 23. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
    copy3 = 0
    intors = ""
    if len(str) > 1:
        while copy3 < 3:
            intors = intors + str[-2] + str[-1]
            copy3 = copy3 + 1
        return intors
    else:
        return False

print(extra_end("Candy"))



# 24. Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
    if len(str) < 2:
        return False
    else:
        str = str[1 : -1]
    return str

print(without_end("java"))


# 25. Given 2 strings, a and b, return a string of the form short+long+short
#     with the shorter string on the outside and the longer string on the inside. 
#     The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
    if len(a) != len(b):
        if len (a) > len (b):
            return b + a + b
        else:
            return a + b + a

print(combo_string("aaa", "1234"))





# 26. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
    intors = ""
    if len(a) > 0 and len(b) > 0:
        intors = a[1:] + b[1:]
    return intors

print(non_start("Hello", "There"))



# 27. Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
    intors = ""
    if len(str) > 1:
        intors = str[2:] + str[0] + str[1]
    return intors

print(left2("Hello"))



# 28. Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
    intors = a + b + b + a
    return intors

print(make_abba("Hi", "Bye"))


# 29. Given a string, return a new string where "not " has been added to the front.
#     However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    intors = "not " + str
    if str[:3] == "not":
        return str
    else:
        return intors

print(not_string("not bad"))



# 30. Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) > 1:
        uc = str[-1]
        pc = str[0]
        str = uc + str[1:-1] + pc
        return str
    else:
        return str

print(front_back("Hello"))



# 31. Write a Python program to concatenate elements of a list.

def concatenate(lista):
    intors = ""
    for i in range(len(lista)):
        intors = intors + lista[i]
    return intors
a = ["Dragos", "E", "Barosan"]
print(concatenate(a))


# 32. Write a Python program to count the number 4 in a given list.

lista = [3, 4, 5, 6, 4, 8, 7, 4]
count = 0
for i in lista:
    if i == 4:
        count = count + 1
print(count)



# 33. Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#     Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(a):
    lista = []
    for i in range(len(a)):
        if a[i].isupper ():
            lista.append(i)
    return lista
print(capital_indexes("HeLlO"))



# 34. Write a function named mid that takes a string as its parameter. 
#     Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

def mid(a):
    if len(a) % 2 == 1:
            return a[int(len(a) / 2)]
    else:
        return ""

print(mid("abc"))



# 35. Write a function named online_count that takes one parameter. 
#     The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

def online_count(a):
    count = 0
    for i in a.values():    # .values - accesez parametrul "y" din dictionar
        if i == "online":
            count += 1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))






# 36. Write a function named only_ints that takes two parameters. 
#     Your function should return True if both parameters are integers, and False otherwise.
#     For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(a, b):
    if type(a) == int and type(b) == int:    #type - functie ce imi permite sa verific tipul variabilei date
        return True
    else:
        return False

print(only_ints(1, 2))  # Aici intoarce "True"
print (only_ints(1, "a"))   # Aici intoarce "False"






# 37. Define a function named double_letters that takes a single parameter. 
#     The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(a):
    for i in range(len(a)):
        if i != len(a) - 1:
            if a[i] == a[i + 1]:
                return True
    
    return False

print(double_letters("Hello"))  # Aici intoarce "True"
print(double_letters("nono"))   # Aici intoarce "False"



# 38. Define a function named count that takes a single parameter. The parameter is a string. 
#     The string will contain a single word divided into syllables by hyphens, such as these: "ho-tel", "cat", "met-a-phor", etc.

def count(a):
    lista = a.split("-")
    return len(lista)

print(count("ho-tel"))      # Aici intoarce 2
print(count("cat"))         # Aici intoarce 1
print(count("met-a-phor"))  # Aici intoarce 3




# 39. Define a function named largest_difference that takes a list of numbers as its only parameter.
#     Your function should compute and return the difference between the largest and smallest number in the list.

def largest_difference(a):
    max = a[0]
    for numar in a:
        if numar > max:
            max = numar
    min = a[0]
    for numar2 in a:    
        if numar2 < min:
            min = numar2
    return max - min

print(largest_difference([1, 2, 3]))   # Aici intoarce 2
print(largest_difference([3, 6, 9]))   # Aici intoarce 6
print(largest_difference([4, 8, 12]))  # Aici intoarce 8





# 40. Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(a, b, c):
    if a == True and b == True and c == True:
        return True
    else:
        return False

print(triple_and(True, True, True))        # Aici intoarce True
print(triple_and(True, False, True))       # Aici intoarce False
print(triple_and(False, True, False))      # Aici intoarce False
print(triple_and(False, False, False))     # Aici intoarce False





# 41. Write a Python program that removes empty strings from a list of strings.

def empty_remove(a):
    for i in a:
        if i == "":
            a.remove(i)
    return a

print(empty_remove(["Mike", "", "Emma", "Kelly", "", "Brad"]))
