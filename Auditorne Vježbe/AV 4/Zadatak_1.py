# Napisati program koji od korisnika trazi unos broja n. Program ispisuje prvih n kvadrata prirodnih brojeva.

n = int(input("Unesite broj n: "))

if n > 0:
    i = 1
    while i <= n:
        print(f"Kvadrat prirodnog broja {i}: {i ** 2}")
        i += 1
else: print(f"Broj {n} nije prirodan broj!")