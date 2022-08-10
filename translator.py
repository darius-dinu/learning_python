def translate(a):
    final = ""
    for litera in a:
        if litera in "AEIOUaeiou":
            final = final + "p"
        else:
            final = final + litera
    return final


print(translate(input("Introdu un cuvant sau o propozitie: ")))