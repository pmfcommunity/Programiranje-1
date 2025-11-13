# Poznat je da se za izracun drugog korijena nekog broja (u ovom slucaju a) moze koristiti iterativna formula: 
# Sn+1 = 1 / 2 * (Sn + a / Sn)
# Napraviti program koji zahtijeva unos floating point broja a, i broj iteracija n, i koji nakon n iteracija ispisuje dobijenu vrijednost
# Sn+1 kao i vrijednost sqrt(a) dobijenu omocu funkcije iz matematematicke biblioteke.

from math import sqrt 

a = float(input())
n = int(input())

Sn = a 
for i in range(2, n + 1):
    Sn = (1 / 2) * (Sn + (a / Sn))

print(f"Korijen iz {a} putem funkcije sqrt: {sqrt(a)}")
print(f"Korijen iz {a} putem iterativne formule: {Sn}")