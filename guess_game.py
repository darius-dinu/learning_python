cuvant = "Bec"
print("Pare ca este o para, dar nu o poti manca.")
a = ""
a_count = 0
a_limit = 3
out_of_guesses = False
while a != cuvant and not(out_of_guesses):
    if a_count < a_limit:
        a = input("Despre ce e vorba? : ")
        a_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Nu mai ai incercari, ai pierdut!")
else:
    print("Ai castigat!")