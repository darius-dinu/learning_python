a = 20
b = 3
c = 50
if a > b: #Daca se verifica aceasta conditie;
    if a > c: #Dar aceasta nu, atunci, in aceasta circumstanta, codul nu va rula.
        print("Cel mai mare numar este A")
elif b > a and b > c:
    print("Cel mai mare numar este B")
else:
    print("Cel mai mare numar este C")

# b > a and b > c: True and False: False
# b > a or b > c: True or False: True


# And
# 0 0 False
# 0 1 False
# 1 0 False
# 1 1 True

# Or
# 0 0 False
# 0 1 True
# 1 0 True
# 1 1 True