# Napisati program koji od korisnika trazi unos brojeva, sve dok se ne unese negativan broj.
# Program ispisuje ukupnu sumu i proizvod unesenih brojeva.

suma = 0
proizvod = 1

while True:
    k = int(input("Unesite broj: "))
    if k < 0:
        break 
    suma += k 
    proizvod *= k 

print(f"Suma unesenih brojeva iznosi: {suma}\nProizvod unesenih brojeva iznosi: {proizvod}")  