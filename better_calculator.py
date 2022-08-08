a = float(input("Introdu primul numar: "))
operator = input("Introdu operatorul: ")
b = float(input("Introdu al doilea numar: "))
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Operatorul pe care l-ai introdus este invalid")
