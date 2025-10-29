# Napisati program koji od korisnika trazi unos prirodnog broja n. Zatim, program od korisnika trazi unos dva 
# cijela brojaa i b, te generise n slucajnih cijelih brojeva vecid od min(a, b) i manjih od max(a, b), te ispisuje
# zbir pretposljednjih cifara svh generisanih brojeva. Ukoliko korisnik unese broj 5, te racunar generise brojeve:
# 9310, 341212, 32, 2920 i 238, program ispisuje 10 (jer je 1 + 1 + 3 + 2 + 3 = 10)

import random

n = int(input("Unesite prirodni broj n: "))

if n > 0:
    a = int(input("Unesite cijeli broj a: "))
    b = int(input("Unesite cijeli broj b: "))
    minimum = min(a,b)
    maximum = max(a,b)
    suma_pretposljednjih_cifara = 0
    i = 0
    lista_generisanih_cifara = []
    while i < n:
        random_broj = random.randint(minimum + 1, maximum - 1) # Zato sto brojevi moraju biti strogo veci od min,
        if random_broj > minimum and random_broj < maximum:    # i strogo manji od max.
            lista_generisanih_cifara.append(random_broj)
            i += 1
    for broj in lista_generisanih_cifara:
        if broj >= 10: 
            broj_u_string = str(broj)
            pretposljednja_cifra = int(broj_u_string[-2])
            suma_pretposljednjih_cifara += pretposljednja_cifra
        else: pass 
    print(f"Generisane cifre: {lista_generisanih_cifara}")
    print(f"Suma pretposljednjih cifara iznosi: {suma_pretposljednjih_cifara}")
else: print(f"Broj {n} nije prirodan!")