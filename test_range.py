a = [6, 9]

for numar in range(len(a)):  # len a = 2 => numar poate lua doua valori: [0, 1]
    if a[numar] % 2 == 0:
        print("intru pe 2 " + str(a[numar]))
    if a[numar] % 3 == 0:
        print("intru pe 3 " + str(a[numar]))