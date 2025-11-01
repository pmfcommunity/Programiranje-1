# Napisati program koji nakon unosa prirodnog broja pretvara broj u binarni. 

n = int(input("Unesite prirodni broj: "))

if n > 0:
    lista_binarnih_brojeva = []
    kopija = n
    while n > 0:
        if n % 2 == 0: lista_binarnih_brojeva.append(0)
        if n % 2 != 0: lista_binarnih_brojeva.append(1)
        n //= 2
    lista_binarnih_brojeva.reverse()
    binarni_brojevi = "".join(str(broj) for broj in lista_binarnih_brojeva)
    print(f"Dekadni broj {kopija} u binarnom zapisu: {binarni_brojevi}")
else: print(f"Broj {n} nije prirodan!")