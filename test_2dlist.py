a = [      # O lista poate fi compusa din mai multe liste. Acest fenomen este numit: 2D list. El are ca puncte de referinta doua "coordonate": rand si coloana
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Daca dau print(a [0] [2]), 0 = primul rand, iar 2 = a treia coloana => trebuie sa imi afiseze 3.


for rand in a:
    for coloana in rand:
        print(coloana)