# Napisati program koji za uneseni prirodan broj provjerava da li je prost ili slozen.

n = int(input("Unesite prirodan broj n: "))

if n == 1: print("1 nije ni prost ni slozen broj.")
elif n > 1:
    lista_djelioca = []
    for i in range(1, n + 1):
        if n % i == 0: lista_djelioca.append(i)
    if len(lista_djelioca) == 2: print(f"Broj {n} je prost broj.")
    else: print(f"Broj {n} je slozen broj.")
else: print("Broj nije prirodan!")