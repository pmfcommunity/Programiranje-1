# Napisati program koji od korisnika trazi unos broja n.
# Program ispisuje sumu prvih n neparnih brojeva (1, 3, 5, ...)

n = int(input("Unesite broj n: "))

suma = 0
i = 1 
while i <= n: 
    if i % 2 != 0: suma += i
    i += 1
    
print(f"Suma ne parnih brojeva {n} je: {suma}")