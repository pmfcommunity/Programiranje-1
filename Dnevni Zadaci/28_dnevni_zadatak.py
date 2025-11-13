# Napisati program koji od korisnika trazi unos broja n. Korisnik nakon toga unosi n prirodnih brojeva. Program ispisuje zbir prvih cifara
# unesenih brojeva. Ukoliko korisnik unese broj 5, te pet brojeva: 123, 434, 2345, 1, 98, program ispisuje zbir 1 + 4 + 2 + 1 + 9.

n = int(input())

suma_prvih_cifara = 0
for i in range(n): 
    broj = int(input())
    cifra = 0
    while broj != 0:
        cifra = broj % 10
        broj //= 10
    suma_prvih_cifara += cifra 
print(suma_prvih_cifara)