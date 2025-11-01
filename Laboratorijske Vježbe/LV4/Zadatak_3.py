# Napisati program koji od korisnika trazi unos prirodnog broja n. Program racuna i ispisuje najvecu cifru
# unesenog broja. 

n = int(input("Unesite prirodni broj: "))

if n > 0: 
    lista_cifra = []
    kopija = n 
    while n > 0:
        cifra = n % 10 
        lista_cifra.append(cifra)
        n //= 10 
    najveca_cifra = max(lista_cifra)
    print(f"Najveca cifra broja {kopija} je: {najveca_cifra}")
else: print(f"Broj {n} nije prirodan!")