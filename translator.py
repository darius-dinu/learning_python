def translate(a):
    final = ""
    for litera in a:
        if litera.lower() in "aeiou":
            if litera.isupper():
                final = final + "P"
            else:
                final = final + "p"
            
        else:
            final = final + litera
    return final


print(translate(input("Introdu un cuvant sau o propozitie: ")))